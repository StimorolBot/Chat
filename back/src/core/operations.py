import time
import json
from uuid import uuid4
from datetime import timedelta

from functools import wraps
from fastapi import HTTPException, status

from src.config import redis
from src.config import fast_register
from src.core.logger import user_logger


def generate_uuid() -> str:
    return uuid4().hex


def get_seconds(minutes: int) -> int:
    return int(timedelta(minutes=minutes).total_seconds())


async def set_redis(name: str, data: dict, ttl: int = fast_register.ttl): # исправить ttl
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


def set_limit_request(time_limit: int, max_calls: int):
    def decorator(func):
        calls_list = []

        @wraps(func)
        async def wrapper(*args, **kwargs):
            print(args, kwargs)
            time_now = time.time()
            calls_in_time_limit = [call for call in calls_list if call > time_now - time_limit]
            if len(calls_in_time_limit) >= max_calls:
                user_logger.warning("Пользователь превысил лимит запросов")
                raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Превышен лимит запросов")
            calls_list.append(time_now)
            return await func(*args, **kwargs)

        return wrapper

    return decorator
