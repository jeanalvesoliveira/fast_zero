import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


@pytest.fixture
def client() -> TestClient:
    # 01. Fase de organização (arrange)
    return TestClient(app)  # Criando o cliente de testes
