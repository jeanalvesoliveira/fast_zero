from http import HTTPStatus
from typing import Dict, Any

from fastapi import FastAPI

# módulo responsável por permitir
# que o FastAPI retorne páginas HTML
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserSchema, UserPublic

app = FastAPI()


# especificando explicitamente qual código HTTP
# esta requição deve retornar
# por padrão o FastAPI retorna somente JSON
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root() -> dict[str, str]:
    return {'message': 'Olá Mundo', 'arroz': '20'}


# exemplo de uma requisição que retorna HTML
@app.get('/pagina',
         status_code=HTTPStatus.OK,
         response_class=HTMLResponse
         )
def read_pagina() -> str:
    return """
    <html>
        <head>
            <title>Nosso outro olá mundo!</title>
        </head>
        <body>
            <h1>Olá Mundo!</h1>
            <h2>Agora com muito mais estilo ;)</h2>
        </body>
    </html>
    """


@app.post('/users/', response_model=UserPublic)
def create_user(user: UserSchema) -> Any:
    return user
