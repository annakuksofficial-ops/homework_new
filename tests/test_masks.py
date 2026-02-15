import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (7000792289606361, "7000 79** **** 6361"),
        (1234567890123456, "1234 56** **** 3456"),
        (1111222233334444, "1111 22** **** 4444"),
    ],
)
def test_get_mask_card_number(card_number: int, expected: str) -> None:
    """Тестирование маскировки номера карты"""
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_short_card() -> None:
    """Тест с коротким номером карты"""
    with pytest.raises(ValueError, match="Номер карты слишком короткий"):
        get_mask_card_number(123)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        (73654108430135874305, "** 4305"),
        (12345678901234567890, "** 7890"),
        (11112222333344445555, "** 5555"),
    ],
)
def test_get_mask_account(account_number: int, expected: str) -> None:
    """Тестирование маскировки номера счета"""
    assert get_mask_account(account_number) == expected


def test_get_mask_account_short_account() -> None:
    """Тест с коротким номером счета"""
    with pytest.raises(ValueError, match="Номер счета слишком короткий"):
        get_mask_account(123)
