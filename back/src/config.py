from redis import asyncio as aioredis

redis = aioredis.from_url("redis://localhost", encoding="utf8")
