from unittest.mock import MagicMock, patch

from src import calculate_service
from src.calculate_service import calculate


def test_calculate_add_with_mock():
    fake_add = MagicMock(return_value=100)

    with patch.dict(calculate_service.OPERATIONS, {"+": fake_add}):
        result = calculate(2, "+", 3)

    assert result == 100
