from src.config import fast_register
from fastapi import status, HTTPException
from src.core.validator import ValidUserName
from pydantic import BaseModel, field_validator


class CreateUser(BaseModel):
    user_name: ValidUserName
    ttl: int = fast_register.ttl

    @field_validator("ttl")
    @classmethod
    def valid_ttl(cls, ttl) -> int:
        if ttl <= fast_register.min_ttl or ttl >= fast_register.max_ttl:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="'Время жизни' четной записи должно быть в пределах от "
                       f"{fast_register.min_ttl} до {fast_register.max_ttl} сек.")
        return ttl
