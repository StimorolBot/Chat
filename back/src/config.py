from redis import asyncio as aioredis
from pydantic_settings import BaseSettings


class FastReg(BaseSettings):
    min_ttl: int = 300
    ttl: int = 1800
    max_ttl: int = 7200


fast_register = FastReg()
redis = aioredis.from_url("redis://localhost", encoding="utf8")
