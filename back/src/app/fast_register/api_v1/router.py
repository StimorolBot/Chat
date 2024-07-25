from fastapi import APIRouter, status, Response

from src.core.logger import user_logger
from src.core.operations import set_redis
from src.core.response import Response as ResponseSchema
from src.core.operations import generate_uuid, get_seconds

from src.app.fast_register.schema import CreateUser

register_router = APIRouter(prefix="/register", tags=["register"])


# ограничить количество запросов
@register_router.post("/")
async def register_user(user_create: CreateUser, response: Response) -> ResponseSchema:
    user_id = generate_uuid()
    ttl = get_seconds(minutes=user_create.ttl)
    user_logger.info(f"Пользователь '{user_id}' создан")
    await set_redis(
        name=user_id,
        data={"user_id": user_id, "chat": []},
        ttl=ttl
    )
    response.set_cookie(
        key="user_cookie",
        value=user_id,
        samesite='none',
        expires=ttl
    )
    return ResponseSchema(
        status_code=status.HTTP_201_CREATED,
        detail="Пользователь успешно создан",
        data={
            "user_id": user_id,
            "user_name": user_create.user_name,
            "ttl": ttl
        }
    )
