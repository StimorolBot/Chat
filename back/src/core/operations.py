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


async def save_msg():
    ...
