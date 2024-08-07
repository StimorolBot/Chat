from pydantic import WrapValidator
from typing_extensions import Annotated
from fastapi import status, HTTPException


def valid_user_name(name: str, handler) -> str:
    if not name.isalnum():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Имя пользователя может содержать только буквы или цифры")
    elif 2 > len(name) or len(name) > 20:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Имя пользователя слишком короткое/длинное")
    return name


ValidUserName = Annotated[str, WrapValidator(valid_user_name)]
