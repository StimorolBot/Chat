from fastapi import APIRouter, status, HTTPException

from src.config import redis
from src.core.response import Response
from src.core.logger import user_logger
from src.core.operations import generate_uuid, get_seconds

from src.app.fast_register.schema import CreateUser


register_router = APIRouter(prefix="/register", tags=["register"])


# ограничить количество запросов
@register_router.post("/")
async def register_user(user_create: CreateUser):
    user_id = generate_uuid()
    ttl = get_seconds(minutes=user_create.ttl)
    user_logger.info(f"Пользователь '{user_id}' создан")
    await redis.set(name=user_id, value=user_id, ex=ttl)

    return Response(
        status_code=status.HTTP_201_CREATED,
        detail="Пользователь успешно создан",
        data={
            "user_id": user_id,
            "user_name": user_create.user_name,
            "ttl": ttl
        }
    )
