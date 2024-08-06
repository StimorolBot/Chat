from src.config import fast_register
from fastapi import status, HTTPException
from pydantic import BaseModel, field_validator


class CreateUser(BaseModel):
    user_name: str
    ttl: int = fast_register.ttl

    @field_validator("user_name")
    def valid_user_name(cls, name: str) -> str:
        if not name.isalnum():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Имя пользователя может содержать только буквы или цифры")
        elif 2 > len(name) or len(name) > 20:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Имя пользователя слишком короткое/длинное")
        return name

    @field_validator("ttl")
    def valid_ttl(cls, ttl) -> int:
        if ttl <= fast_register.min_ttl or ttl >= fast_register.max_ttl:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="'Время жизни' четной записи должно быть в пределах от "
                       f"{fast_register.min_ttl} до {fast_register.max_ttl} сек.")
        return ttl
