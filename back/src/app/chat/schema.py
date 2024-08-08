from pydantic import BaseModel
from src.core.validator import ValidId


class SearchUser(BaseModel):
    user_id: ValidId

