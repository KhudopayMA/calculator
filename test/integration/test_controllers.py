import pytest
from fastapi.testclient import TestClient

from src.app import create_app
from src.controller import Operator

@pytest.fixture(scope="module")
def client() -> TestClient:
    return TestClient(create_app())

@pytest.mark.parametrize(
    "a,b,operator,expected",
    [
        (2, 2, Operator.ADD, 4),
        (6, 3, Operator.SUBTRACT, 3),
        (6, 6, Operator.MULTIPLY, 36),
        (81, 9, Operator.DIVIDE, 9),
        (2, 8, Operator.POWER, 256),
    ]
)

def test_controller(client: TestClient, a: int, b: int, operator: Operator, expected: int) -> None:
    response = client.post(
        "/api/calculate",
        json={
            "a": a,
            "b": b,
            "op": operator,
        }
    )
    assert response.json() == expected
    assert response.status_code == 200