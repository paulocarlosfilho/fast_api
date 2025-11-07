from fastapi import FastAPI
from datetime import datetime, timezone
from typing import Optional 

app = FastAPI()

# Simulação de um banco de dados
fake_db = [
    {
        'title': 'Criando uma aplicação com Django.',
        'date': datetime.now(timezone.utc),
        'status': 'published'
    },
    {
        'title': 'Internalizando uma app FastApi',
        'date': datetime.now(timezone.utc),
        'status': 'published'
    },
    {
        'title': 'Internalizando uma app Flask',
        'date': datetime.now(timezone.utc),
        'status': 'draft'
    },
    {
        'title': 'Internalizando uma app Starlett',
        'date': datetime.now(timezone.utc),
        'status': 'published'
    }
]

# Rota /posts - Implementação de Paginação (skip/limit) e Filtragem (status)
@app.get("/posts")
def read_posts(skip: int = 0, limit: Optional[int] = None, status: Optional[str] = 'published'):
    
    # 1. FILTRAGEM: Cria uma lista filtrada com base no status fornecido
    if status:
        filtered_posts = [post for post in fake_db if post.get('status') == status]
    else:
        filtered_posts = fake_db

    # 2. DEFINIÇÃO DO LIMITE: Se 'limit' não for fornecido, usa o tamanho da lista filtrada
    limit_val = limit if limit is not None else len(filtered_posts)
    
    # 3. PAGINAÇÃO: Aplica o slicing na lista filtrada
    return filtered_posts[skip : skip + limit_val]
    
# Rota /posts/{framework}
@app.get("/posts/{framework}")
async def read_framework_posts(framework: str):
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

# Rota /items/{item_id}
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}