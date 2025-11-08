from fastapi import FastAPI, Header, status, Cookie, Response
from typing import Annotated

from datetime import datetime, timezone
from typing import Optional 
from pydantic import BaseModel


app = FastAPI()

# Simulação de um banco de dados (usa 'status': 'published' ou 'draft')
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


# Pydantic Model (usa 'published: bool')
class Post(BaseModel):
    title: str
    date: datetime = datetime.now(timezone.utc)
    published: bool = False
    author: str = "John Doe"

    
@app.post("/post/", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    # LÓGICA: Converte o booleano 'published' do Pydantic para o string 'status' do DB
    post_data = post.model_dump()
    post_data['status'] = 'published' if post.published else 'draft'
    
    # Remove a chave 'published' para evitar conflito com a estrutura do fake_db
    del post_data['published'] 
    
    fake_db.append(post_data)
    return post

# Rota /posts
@app.get("/posts/")
def read_posts(
    response: Response,
    published: bool,
    limit: int,
    skip: int = 0,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None
):
    # 1. TRADUÇÃO: Traduz o parâmetro booleano (published) para a string do DB (status_str)
    status_str = 'published' if published else 'draft'
    
    # 2. FILTRAGEM: Filtra usando a chave 'status' que existe no fake_db
    filtered_posts = [
        post for post in fake_db 
        if post.get('status') == status_str
    ]

    response.set_cookie(key='user', value='gui.ifsp11@gmail.com')
    
    print(f"Cookie: {ads_id}")
    print(f"Cookie: {user_agent}")

    # 3. PAGINAÇÃO: Aplica o slicing na lista filtrada
    return filtered_posts[skip : skip + limit]

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