from unittest.mock import patch

from src.external_api import convert_currency, convert_to_rub


def test_convert_currency_rub():
    """Тест: транзакция уже в рублях"""
    transaction = {"operationAmount": {"amount": "123.45", "currency": {"code": "RUB"}}}

    result = convert_currency(transaction)

    assert result == 123.45


def test_convert_currency_usd():
    """Тест: конвертация долларов"""
    with patch("src.external_api.convert_to_rub") as mock_convert:
        mock_convert.return_value = 7500.0

        transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}

        result = convert_currency(transaction)

        mock_convert.assert_called_once_with(100.0, "USD")

        assert result == 7500.0


def test_convert_currency_eur():
    """Тест: конвертация евро"""
    with patch("src.external_api.convert_to_rub") as mock_convert:
        mock_convert.return_value = 9000.0

        transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "EUR"}}}

        result = convert_currency(transaction)

        mock_convert.assert_called_once_with(100.0, "EUR")
        assert result == 9000.0


def test_convert_currency_missing_amount():
    """Тест: в транзакции нет поля amount"""
    transaction = {"operationAmount": {"currency": {"code": "USD"}}}

    result = convert_currency(transaction)
    assert result == 0.0


def test_convert_currency_wrong_currency():
    """Тест: неподдерживаемая валюта"""
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "JPY"}}}

    result = convert_currency(transaction)
    assert result == 0.0


def test_convert_currency_bad_amount():
    """Тест: сумма не число"""
    transaction = {"operationAmount": {"amount": "сто рублей", "currency": {"code": "RUB"}}}  # Не число

    result = convert_currency(transaction)
    assert result == 0.0


@patch("requests.get")
def test_convert_to_rub_connection_problem(mock_get):
    """Тест: проблемы с соединением"""
    mock_get.side_effect = Exception("Нет интернета")

    result = convert_to_rub(100.0, "USD")
    assert result == 0.0


def test_convert_to_rub_no_key():
    """Тест: нет API ключа"""
    with patch("src.external_api.API_KEY", None):
        result = convert_to_rub(100.0, "USD")
        assert result == 0.0
