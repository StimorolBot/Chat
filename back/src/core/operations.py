import json
from uuid import uuid4
from src.config import redis
from datetime import timedelta


def generate_uuid() -> str:
    return str(uuid4())


def get_seconds(minutes: int) -> int:
    return int(timedelta(minutes=minutes).total_seconds())


async def set_redis(name: str, data: dict, ttl: int = 1800): # исправить ttl
    data_str = json.dumps(data)
    await redis.set(name=name, value=data_str, ex=ttl)


async def get_redis(key: str) -> dict | None:
    data_dict = await redis.get(key)
    if not data_dict:
        return None
    return json.loads(data_dict)


async def save_msg(user_id: str, msg: str, msg_id: int):
    user = await get_redis(user_id)
    chat_id = user["chat_dict"].get(user_id)
    if not chat_id:
        raise KeyError(f"Не удалось найти чат для: {user_id}")

    chat = await get_redis(chat_id)
    chat[chat_id].append({"user_id": user_id, "id": msg_id, "msg": msg})
    await set_redis(chat_id, chat)
