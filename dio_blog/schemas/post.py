from pydantic import BaseModel
from datetime import datetime, timezone


class PostIn(BaseModel):
    title: str
    date: datetime = datetime.now(timezone.utc)
    published: bool = False
    author: str = "John Doe"


class Foo(BaseModel):
    bar: str
