from pydantic import BaseModel


class Response(BaseModel):
    status_code: int
    detail: str
    data: dict | None = None
