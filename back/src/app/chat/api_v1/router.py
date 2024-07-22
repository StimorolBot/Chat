from uuid import UUID
from typing import Annotated

from fastapi import (APIRouter, WebSocket, WebSocketDisconnect,
                     Cookie, status, HTTPException)

from src.core.logger import ws_logger
from src.app.chat.connection_manager import manager

chat_router = APIRouter(tags=["chat"])


@chat_router.websocket("/{user_id}")
async def websocket_endpoint(
        websocket: WebSocket, user_id: UUID,
        user_cookie: Annotated[str | None, Cookie()] = None):

    if not user_cookie:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователь не авторизирован"
        )
    elif UUID(user_cookie) != user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Не далось найти страницу"
        )

    ws_logger.info(msg=f"Подключился: {user_cookie}")
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            await manager.send_personal_message(data["data"], data["id"], websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

