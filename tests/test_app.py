from http import HTTPStatus

# fixture é uma função cujo retorno
# é passado para as funções de testes
# aplicando o princípio DRY (Não se repita)
# geralmente os fixtures ficam em um arquivo chamado conftest.py
# @pytest.fixture()
# def client() -> TestClient:
# 01. Fase de organização (arrange)
#     return TestClient(app)  # Criando o cliente de testes


def test_read_root_deve_retornar_ok_e_ola_mundo(client) -> None:
    # 02. Fase de ação (act)
    # Requisitando o recurso localizado no endpoint '/'
    response = client.get('/')

    # 03. Fase de afirmação (assert)
    # Garantir que retornou status code OK (200)
    assert response.status_code == HTTPStatus.OK

    # Garantir que retornou um JSON com o conteúdo certo
    assert response.json() == {'message': 'Olá Mundo'}


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
    # enviando um JSON através do verbo POST para o endpoint '/users/'
    response = client.post(
        '/users/',
        json={
            'username': 'testeusername',
            'email': 'teste@test.com',
            'password': 'password',
        },
    )

    # 03. Fase de afirmação (assert)
    # Garantir que retornou status code CREATED (201)
    assert response.status_code == HTTPStatus.CREATED

    # Garantir que retornou os dados corretos
    # Validar UserPublic
    assert response.json() == {
        'username': 'testeusername',
        'email': 'teste@test.com',
        'id': 1,
    }


def test_read_users(client) -> None:
    # 02. Fase de ação (act)
    # Requisitando o recurso localizado
    # no endpoint '/users/' através do verbo GET
    response = client.get('/users/')

    # 03. Fase de afirmação (assert)
    # Garantir que retornou status code OK (200)
    assert response.status_code == HTTPStatus.OK

    # Garantir que retornou um JSON com o conteúdo certo
    assert response.json() == {
        'users': [
            {
                'username': 'testeusername',
                'email': 'teste@test.com',
                'id': 1,
            }
        ]
    }


def test_read_one_user(client) -> None:
    response = client.get('/users/1')

    assert response.json() == {
        'username': 'testeusername',
        'email': 'teste@test.com',
        'id': 1,
    }


def test_verifica_se_retorna_codigo_404_ao_tentar_retornar_um_usuario(
    client,
) -> None:
    # 02. Fase de ação (act)
    # Realizando uma requisição PUT
    # passando o endpoint e o json
    # com um ID invalido
    response = client.get('/users/0')

    # 03. Fase de afirmação (assert)
    # Garantir que retornou status code NOT FOUND (404)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_users(client) -> None:
    # 02. Fase de ação (act)
    # Realizando uma requisição PUT
    # passando o endpoint e o json
    response = client.put(
        '/users/1',
        json={
            'password': '123456',
            'username': 'testeusername2',
            'email': 'teste@test.com',
            'id': 1,
        },
    )

    # 03. Fase de afirmação (assert)
    # Garantir que retornou um JSON com o conteúdo certo
    assert response.json() == {
        'username': 'testeusername2',
        'email': 'teste@test.com',
        'id': 1,
    }


def test_verifica_se_retorna_codigo_404_ao_tentar_atualizar(client) -> None:
    # 02. Fase de ação (act)
    # Realizando uma requisição PUT
    # passando o endpoint e o json
    # com um ID invalido
    response = client.put(
        '/users/0',
        json={
            'password': '123456',
            'username': 'testeusername2',
            'email': 'teste@test.com',
            'id': 1,
        },
    )

    # 03. Fase de afirmação (assert)
    # Garantir que retornou status code NOT FOUND (404)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client) -> None:
    # 02. Fase de ação (act)
    # Realizando uma requisição DELETE
    response = client.delete('/users/1')

    # 03. Fase de afirmação (assert)
    # Garantir que retornou um JSON com o conteúdo certo
    assert response.json() == {'message': 'User deleted'}


def test_verifica_se_retorna_codigo_404_ao_tentar_deletar(client) -> None:
    # 02. Fase de ação (act)
    # Realizando uma requisição DELETE
    # com um ID invalido
    response = client.delete('/users/0')

    # 03. Fase de afirmação (assert)
    # Garantir que retornou status code NOT FOUND (404)
    assert response.status_code == HTTPStatus.NOT_FOUND
