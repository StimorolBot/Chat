from uuid import uuid4
from datetime import timedelta


def generate_uuid() -> str:
    return str(uuid4())


def get_seconds(minutes: int) -> int:
    return int(timedelta(minutes=minutes).total_seconds())
