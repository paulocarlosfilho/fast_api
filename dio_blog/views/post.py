from pydantic import BaseModel
from datetime import datetime, timezone


class PostOut(BaseModel):
    title: str
    author: str
    published_at: datetime
