from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


# fixture é uma função cujo retorno
# é passado para as funções de testes
@pytest.fixture
def client() -> TestClient:
    # 01. Fase de organização (arrange)
    return TestClient(app)  # Criando o cliente de testes


def test_read_root_deve_retornar_ok_e_ola_mundo(client) -> None:
    # 02. Fase de ação (act)
    # Requisitando o recurso localizado no endpoint '/'
    response = client.get('/')

    # 03. Fase de afirmação (assert)
    # Garantir que retornou status code OK (200)
    assert response.status_code == HTTPStatus.OK

    # Garantir que retornou um JSON com o conteúdo certo
    assert response.json() == {'message': 'Olá Mundo', 'arroz': 20}


def test_read_pagina_deve_retornar_ok_e_ola_mundo_em_html(client) -> None:
    response = client.get('/pagina')

    assert response.status_code == HTTPStatus.OK

    assert (
        response.text
        == """
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
    )


def test_create_user(client) -> None:
    # 02. Fase de ação (act)
    # Requisitando o recurso localizado no endpoint '/users/'
    response = client.post(
        '/users/',
        json={
            'username': 'testeusername',
            'email': 'teste@test.com',
            'password': 'password'
        }
    )

    # 03. Fase de afirmação (assert)
    # Garantir que retornou status code CREATED (201)
    assert response.status_code == HTTPStatus.CREATED

    # Garantir que retornou os dados corretos
    # Validar UserPublic
    assert response.json() == {
            'username': 'testeusername',
            'email': 'teste@test.com',
            'id': 1
    }
