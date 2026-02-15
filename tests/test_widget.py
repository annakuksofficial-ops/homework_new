import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ],
)
def test_mask_account_card(input_str: str, expected: str) -> None:
    """Тестирование маскировки карт и счетов"""
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Счет 11112222333344445555", "Счет **5555"),
    ],
)
def test_mask_account_card_accounts(input_str: str, expected: str) -> None:
    """Тестирование маскировки только счетов"""
    assert mask_account_card(input_str) == expected


def test_mask_account_card_invalid_input() -> None:
    """Тест с некорректным входным данными"""
    result = mask_account_card("123")
    assert result is not None


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        ("2025-01-01T00:00:00.000000", "01.01.2025"),
    ],
)
def test_get_date(input_date: str, expected: str) -> None:
    """Тестирование форматирования даты"""
    assert get_date(input_date) == expected


def test_get_date_invalid_format() -> None:
    """Тест с некорректным форматом даты"""
    result = get_date("2024/03/11")
    assert result is not None
