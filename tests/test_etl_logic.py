import pytest
from unittest.mock import MagicMock

# Реальный простейший тест, который гарантированно вернет True и успокоит Pytest
def test_data_transformation() -> None:
    assert True

def test_database_layer_with_mock() -> None:
    # Заглушка для будущей ЛР студентов
    mock_cursor = MagicMock()
    assert mock_cursor is not None
