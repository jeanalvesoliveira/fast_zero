from http import HTTPStatus

from fastapi import FastAPI, HTTPException

# módulo responsável por permitir
# que o FastAPI retorne páginas HTML
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserDb, UserList, UserPublic, UserSchema

app = FastAPI()

# banco de dados fake
database = []


# especificando explicitamente qual código HTTP
# esta requição deve retornar
# por padrão o FastAPI retorna somente JSON
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
async def read_root() -> dict[str, str]:
    return {'message': 'Olá Mundo'}


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
async def create_user(user: UserSchema) -> UserDb | None:
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


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
async def read_users() -> dict[str, list[UserPublic]]:
    return {'users': database}


@app.get('/users/{user_id}', response_model=UserPublic)
async def read_one_user(user_id: int) -> UserPublic | None:
    # validação para o caso do ID não existir
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    return database[user_id - 1]


@app.put('/users/{user_id}', response_model=UserPublic)
async def update_users(user_id: int, user: UserSchema) -> UserDb | None:
    # validação para o caso do ID não existir
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDb(id=user_id, **user.model_dump())

    # como ainda é um banco fake
    # o índice é o ID - 1
    # exemplo: Id = 1, o índice na lista é 0
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
async def delete_user(user_id: int) -> dict[str, str]:
    # validação para o caso do ID não existir
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    # remove o usuário da lista
    database.pop(user_id - 1)

    return {'message': 'User deleted'}
