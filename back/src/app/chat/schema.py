from uuid import UUID
from fastapi import status, HTTPException
from pydantic import BaseModel, field_validator
from src.core.validator import ValidUserName


class AddUser(BaseModel):
    user_id: str
    user_name: ValidUserName

    @field_validator("user_id")
    @classmethod
    def valid_user_id(cls, id_) -> str:
        try:
            UUID(id_)
            return id_
        except ValueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Некорректный id")
