from typing import Dict
from fastapi import WebSocket
from src.core.logger_conf import ws_logger


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str: WebSocket] = {}

    async def connect(self, user_id: str, websocket: WebSocket):
        await websocket.accept()
        if not self.active_connections.get(user_id):
            self.active_connections[user_id] = websocket
            ws_logger.debug(msg=f"Подключился: {user_id}")

    def disconnect(self, user_id: str):
        if self.active_connections.get(user_id):
            del self.active_connections[user_id]
            ws_logger.debug(msg=f"Отключился: {user_id}")

    async def send_personal_message(self, message: str, chat_id: str):
        websocket = self.active_connections.get(chat_id)
        if websocket:
            await websocket.send_text(message)
            ws_logger.debug(f"Сообщение {message} успешно отправлено")

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()
