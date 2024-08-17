from typing import Annotated

from src.core.response import Response
from src.rmq.publisher import publisher
from src.core.logger_conf import user_logger
from src.core.operations import set_redis, get_redis, generate_uuid, save_msg

from src.core.validator import ValidId
from src.app.chat.schema import SearchUser
from src.app.chat.connection_manager import manager

from fastapi_cache.decorator import cache
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Cookie, status, HTTPException, Depends

chat_router = APIRouter(tags=["chat"])


async def get_cookie(user_cookie: Annotated[ValidId, Cookie()] = None) -> str:
    user_logger.debug(f"{user_cookie=}")
    if not user_cookie:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь не авторизирован")
    return user_cookie


@chat_router.get("/")
async def get_user_info(user_cookie: str = Depends(get_cookie)) -> Response:
    user_info = await get_redis(user_cookie)
    user_logger.debug(f"{user_info=}")
    try:
        return Response(
            status_code=status.HTTP_200_OK, detail="Информация о пользователе",
            data={"user_id": user_info.get("user_id"), "chat_list": user_info.get("chat_list")})
    except AttributeError as e:
        user_logger.error(f"Внутренняя ошибка сервера: {e}")
        await publisher(f"Error: INTERNAL SERVER ERROR: {e}.\n User cookie: {user_cookie}".encode())
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Внутренняя ошибка сервера")


@chat_router.get("/chat/{chat_id}")
@cache(namespace="msg", expire=360)
async def get_msg(chat_id: ValidId, user_cookie: str = Depends(get_cookie)) -> Response:
    user_info = await get_redis(user_cookie)
    chat_id_list = user_info["chat_dict"]

    if chat_id_list:
        chat_uuid = chat_id_list.get(chat_id)
        chat = await get_redis(chat_uuid)
        return Response(status_code=status.HTTP_200_OK, detail="История сообщений", data={"msg": chat[chat_uuid]})


@chat_router.post("/")
async def add_chat(chat: SearchUser, user_cookie: str = Depends(get_cookie)) -> Response:
    user = await get_redis(chat.user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Пользователь не найден")
    elif user_cookie in user["chat_dict"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Чат уже добавлен")

    chat_id = generate_uuid()
    user["chat_dict"][user_cookie] = chat_id

    cookie = await get_redis(user_cookie)
    cookie["chat_dict"][chat.user_id] = chat_id

    cookie["chat_list"].append({"chat_name": user["user_name"], "chat_id": chat.user_id})
    user["chat_list"].append({"chat_name": cookie["user_name"], "chat_id": user_cookie})

    await set_redis(user_cookie, cookie)
    await set_redis(chat.user_id, user)
    await set_redis(chat_id, {chat_id: []})
    user_logger.debug(f"{chat_id=}")

    return Response(status_code=status.HTTP_201_CREATED,
                    data={"chat_id": chat.user_id, "chat_name": user["user_name"]},
                    detail="Чат успешно создан")


@chat_router.websocket("/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: ValidId, user_cookie: str = Depends(get_cookie)):
    await manager.connect(user_cookie, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            await manager.send_personal_message(data["data"], chat_id)
            await save_msg(user_id=user_cookie, chat_id=chat_id, msg=data["data"], msg_id=data["id"])
    except WebSocketDisconnect:
        manager.disconnect(user_cookie)
