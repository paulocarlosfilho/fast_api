from controllers import post
from fastapi import FastAPI

app = FastAPI()
app.include_router(post.router)
