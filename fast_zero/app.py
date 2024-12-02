from http import HTTPStatus
from typing import Any

from fastapi import FastAPI

# módulo responsável por permitir
# que o FastAPI retorne páginas HTML
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserDb, UserPublic, UserSchema

app = FastAPI()

# banco de dados fake
database = []


# especificando explicitamente qual código HTTP
# esta requição deve retornar
# por padrão o FastAPI retorna somente JSON
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
async def read_root() -> dict[str, str]:
    return {'message': 'Olá Mundo', 'arroz': '20'}


# exemplo de uma requisição que retorna HTML
@app.get('/pagina', status_code=HTTPStatus.OK, response_class=HTMLResponse)
async def read_pagina() -> str:
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


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
async def create_user(user: UserSchema) -> Any:
    # abrindo o debugger
    # breakpoint()

    user_with_id = UserDb(
        # id fake auto-incremento
        id=len(database) + 1,
        # converte o objeto user (recebido)
        # em um dicionário: user.model_dump()
        # e extrai os pares chave->valor
        # em atributos: operador **
        **user.model_dump(),
    )

    # adicionando o usuario ao 'banco'
    database.append(user_with_id)

    return user_with_id
