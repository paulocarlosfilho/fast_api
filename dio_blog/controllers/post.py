from fastapi import Header, status, Cookie, Response
from typing import Annotated

from datetime import datetime, timezone

from schemas.post import Foo, PostIn
from views.post import PostOut

from main import app

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


@app.post("/post/", status_code=status.HTTP_201_CREATED, response_model=PostIn)
def create_post(post: PostIn):
    # LÓGICA: Converte o booleano 'published'
    #  do Pydantic para o string 'status' do DB
    post_data = post.model_dump()
    post_data['status'] = 'published' if post.published else 'draft'
    # Remove a chave 'published' para evitar
    #  conflito com a estrutura do fake_db
    del post_data['published']

    fake_db.append(post_data)
    return post


# Rota /posts
@app.get("/posts/", response_model=list(PostOut))
def read_posts(
    response: Response,
    published: bool,
    limit: int,
    skip: int = 0,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None
):
    # 1. TRADUÇÃO: Traduz o parâmetro booleano
    #  (published) para a string do DB (status_str)
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
    return filtered_posts[skip: skip + limit]


@app.get("/posts/{framework}", reponse_model=PostIn)
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


# Foobar - usando o dict
@app.get("/foobar/", response_model=Foo)
def foobar() -> dict[str, str]:
    return {"bar": "foo", "mensagem": "Azul"}


# Rota /items/{item_id}
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
