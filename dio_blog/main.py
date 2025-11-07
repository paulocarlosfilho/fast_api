from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()

# A rota deve aceitar o 'framework' como argumento para que o URL funcione
@app.get("/posts/{framework}")
async def read_posts(framework: str):
    # A resposta deve ser uma lista de dicionários [{}, {}]
    return {
        "posts": [
            {
                'title': f'Criando uma aplicação com {framework}',
                'date': datetime.now(timezone.utc)
            },
            {
                'title': f'Internalizando uma app {framework}',
                'date': datetime.now(timezone.utc)
            }
        ]
    }

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
