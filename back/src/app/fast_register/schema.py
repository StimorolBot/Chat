from pydantic import BaseModel, model_validator


class CreateUser(BaseModel):
    user_name: str
    ttl: int = 1800


"""
    @model_validator(mode="after")
    @classmethod
    def valid_user_name(cls):
        ...

   @field_validator('a')
        @classmethod
        def check_a(cls):
            return 'a'
"""

