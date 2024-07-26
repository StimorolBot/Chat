from typing import Annotated

from src.core.logger import ws_logger
from src.core.response import Response
from src.core.operations import set_redis, get_redis

from src.app.chat.schema import AddChat
from src.app.chat.connection_manager import manager

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Cookie, status, HTTPException

chat_router = APIRouter(tags=["chat"])


@chat_router.get("/")
async def get_user_info(user_cookie: Annotated[str, Cookie()] = None):
    if not user_cookie:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь не авторизирован")
    user_info = await get_redis(user_cookie)
    return Response(status_code=status.HTTP_200_OK, detail="Информация пользователя", data=user_info)


@chat_router.post("/")
async def add_chat(search: AddChat, user_cookie: Annotated[str | None, Cookie()] = None) -> Response:
    if not user_cookie:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь не авторизирован")

    chat = await get_redis(user_cookie)
    if not chat:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Пользователь не найден")

    chat["chat"].append(str(search.user_id))
    await set_redis(user_cookie, chat, 1800)  # исправить ttl

    return Response(status_code=status.HTTP_200_OK, detail="Чат найден")


@chat_router.websocket("/{chat_id}")
async def websocket_endpoint(
        websocket: WebSocket,
        user_cookie: Annotated[str | None, Cookie()] = None):
    if not user_cookie:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователь не авторизирован"
        )
    ws_logger.info(msg=f"Подключился: {user_cookie}")
    await manager.connect(user_cookie, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            await manager.send_personal_message(data["data"], data["chat_id"])
    except WebSocketDisconnect:
        manager.disconnect(user_cookie)
