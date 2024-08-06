from typing import Annotated

from src.core.logger import ws_logger
from src.core.response import Response
from src.core.operations import set_redis, get_redis, generate_uuid, save_msg

from src.app.chat.schema import AddUser
from src.app.chat.connection_manager import manager

from fastapi_cache.decorator import cache
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Cookie, status, HTTPException, Depends

chat_router = APIRouter(tags=["chat"])


async def get_cookie(user_cookie: Annotated[str, Cookie()] = None) -> str:
    if not user_cookie:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь не авторизирован")
    return user_cookie


@chat_router.get("/msg")
@cache(namespace="msg", expire=120)
async def get_msg(user_cookie: str = Depends(get_cookie)) -> Response:
    user_info = await get_redis(user_cookie)
    chat_id_list = user_info["chat_dict"]
    if chat_id_list:
        chat_id = chat_id_list.get(user_cookie)
        chat = await get_redis(chat_id)
        return Response(status_code=status.HTTP_200_OK, detail="История сообщений", data={"msg": chat[chat_id]})


@chat_router.get("/")
async def get_user_info(user_cookie: str = Depends(get_cookie), msg: Response | None = Depends(get_msg)) -> Response:
    user_info = await get_redis(user_cookie)
    return Response(
        status_code=status.HTTP_200_OK, detail="Информация о пользователе",
        data={**user_info, "msg_list": msg}
    )


@chat_router.post("/")
async def add_chat(chat: AddUser, user_cookie: str = Depends(get_cookie)) -> Response:
    user = await get_redis(str(chat.user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Пользователь не найден")
    elif user_cookie in user["chat_dict"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Чат уже добавлен")

    chat_id = generate_uuid()
    user["chat_dict"][chat.user_id] = chat_id

    cookie = await get_redis(user_cookie)
    cookie["chat_dict"][user_cookie] = chat_id

    await set_redis(user_cookie, cookie)
    await set_redis(chat.user_id, user)
    await set_redis(chat_id, {chat_id: []})

    return Response(status_code=status.HTTP_200_OK,
                    data={"chat_id": chat.user_id, "chat_name": chat.user_name},
                    detail="Чат добавлен")


@chat_router.websocket("/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: str, user_cookie: str = Depends(get_cookie)):
    ws_logger.info(msg=f"Подключился: {user_cookie}")
    await manager.connect(user_cookie, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            await manager.send_personal_message(data["data"], chat_id)
            await save_msg(user_cookie, msg=data["data"], msg_id=data["id"])
    except WebSocketDisconnect:
        manager.disconnect(user_cookie)
