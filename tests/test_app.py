from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo() -> None:
    # 01. Fase de organização (arrange)
    client = TestClient(app)  # Criando o cliente de testes

    # 02. Fase de ação (act)
    # Requisitando o recurso localizado no endpoint '/'
    response = client.get('/')

    # 03. Fase de afirmação (assert)
    # Garantir que retornou status code OK (200)
    assert response.status_code == HTTPStatus.OK

    # Garantir que retornou um JSON com o conteúdo certo
    assert response.json() == {'message': 'Olá Mundo', 'arroz': 20}


def test_read_pagina_deve_retornar_ok_e_ola_mundo_em_html() -> None:
    client = TestClient(app)

    response = client.get('/pagina')

    assert response.status_code == HTTPStatus.OK

    assert response.text == """
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
