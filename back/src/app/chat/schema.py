from pydantic import BaseModel


class AddUser(BaseModel):
    user_id: str
    user_name: str | None = None

