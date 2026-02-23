import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from typing import List, Dict, Any

transactions: List[Dict[str, Any]] = [
    {
        "id": 939719570,
        "description": "Перевод организации",
        "operationAmount": {
            "currency": {
                "code": "USD"
            }
        }
    },
    {
        "id": 142264268,
        "description": "Перевод со счета на счет",
        "operationAmount": {
            "currency": {
                "code": "EUR"
            }
        }
    },
    {
        "id": 873106923,
        "description": "Перевод с карты на карту",
        "operationAmount": {
            "currency": {
                "code": "USD"
            }
        }
    },
    {
        "id": 214024827,
        "description": "Перевод с карты на карту",
        "operationAmount": {
            "currency": {
                "code": "RUB"
            }
        }
    }
]

empty_list: List = []


@pytest.mark.parametrize("currency, expected_count, expected_ids", [
    ("USD", 2, [939719570, 873106923]),
    ("EUR", 1, [142264268]),
    ("RUB", 1, [214024827]),
    ("GBP", 0, []),
])
def test_filter_by_currency_parametrized(currency: str, expected_count: int, expected_ids: List[int]) -> None:
    """Тест фильтрации по разным валютам"""
    result = list(filter_by_currency(transactions, currency))
    assert len(result) == expected_count
    if expected_count > 0:
        for i, transaction in enumerate(result):
            assert transaction["id"] == expected_ids[i]


def test_filter_by_currency_empty_list() -> None:
    """Проверяем с пустым списком"""
    result = list(filter_by_currency(empty_list, "USD"))
    assert result == []


def test_filter_by_currency_default() -> None:
    """Проверяем значение по умолчанию"""
    result = list(filter_by_currency(transactions))
    assert len(result) == 2
    assert result[0]["id"] == 939719570
    assert result[1]["id"] == 873106923


def test_transaction_descriptions_normal() -> None:
    """Проверяем получение описаний"""
    result = list(transaction_descriptions(transactions))

    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод с карты на карту"
    ]

    assert result == expected


def test_transaction_descriptions_empty_list() -> None:
    """Проверяем с пустым списком"""
    result = list(transaction_descriptions(empty_list))
    assert result == []


def test_transaction_descriptions_missing_description() -> None:
    """Проверяем, когда нет поля description"""
    test_data = [
        {"id": 1},
        {"id": 2, "description": "Есть описание"},
        {"id": 3},
    ]

    result = list(transaction_descriptions(test_data))
    assert result == ["Есть описание"]


def test_transaction_descriptions_empty_description() -> None:
    """Проверяем с пустыми описаниями"""
    test_data = [
        {"id": 1, "description": ""},
        {"id": 2, "description": "Описание 2"},
        {"id": 3, "description": ""},
        {"id": 4, "description": "Описание 4"},
    ]

    result = list(transaction_descriptions(test_data))
    assert result == ["Описание 2", "Описание 4"]


@pytest.mark.parametrize("test_list, expected", [
    ([], []),
    ([{"description": "Тест"}], ["Тест"]),
    ([{"description": "A"}, {"description": "B"}], ["A", "B"]),
])
def test_transaction_descriptions_parametrized(test_list: List[Dict[str, Any]], expected: List[str]) -> None:
    """Тест описаний с разными данными"""
    result = list(transaction_descriptions(test_list))
    assert result == expected


def test_card_number_generator_small() -> None:
    """Проверяем генерацию маленьких номеров"""
    result = list(card_number_generator(1, 5))

    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]

    assert result == expected
