from fastapi import APIRouter, status, Response

from src.core.logger_conf import user_logger
from src.core.response import Response as ResponseSchema

from src.core.operations import generate_uuid
from src.core.operations import set_redis, set_limit_request

from src.app.fast_register.schema import CreateUser

register_router = APIRouter(prefix="/register", tags=["register"])


@register_router.post("/")
@set_limit_request(time_limit=30, max_calls=3)
async def register_user(user_create: CreateUser, response: Response) -> ResponseSchema:
    user_id = generate_uuid()
    user_logger.info(f"Пользователь '{user_id}' создан")

    await set_redis(
        name=user_id, ttl=user_create.ttl,
        data={
            "user_id": user_id, "user_name": user_create.user_name,
            "chat_dict": {}, "chat_list": []
        }
    )
    # исправить
    response.set_cookie(key="user_cookie", value=user_id, samesite='none', expires=user_create.ttl)

    return ResponseSchema(
        status_code=status.HTTP_201_CREATED,
        detail="Пользователь успешно создан",
        data={
            "user_id": user_id,
            "user_name": user_create.user_name,
            "ttl": user_create.ttl
        }
    )
