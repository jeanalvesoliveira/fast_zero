from http import HTTPStatus

from fastapi import FastAPI

app = FastAPI()


# especificando explicitamente qual código HTTP
# esta requição deve retornar
@app.get('/', status_code=HTTPStatus.OK)
async def read_root() -> dict[str, str]:
    return {'message': 'Olá Mundo'}
