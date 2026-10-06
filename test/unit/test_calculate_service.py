from src.calculate_service import calculate
from src.controller import Operator

import pytest

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

def test_calculate_service(a, b, operator, expected):
    assert calculate(a=a, b=b, operator=operator) == expected

def test_calculate_service_divide_by_zero():
    with pytest.raises(ValueError, match="Деление на ноль невозможно"):
        calculate(a=4, b=0, operator=Operator.DIVIDE)

def test_calculate_service_unknown_operator():
    with pytest.raises(ValueError, match=f"Неизвестная операция: *~*"):
        calculate(a=4, b=0, operator="*~*")
