import pytest
from typing import List, Dict, Any


@pytest.fixture
def sample_card_data() -> List[Dict[str, Any]]:
    """Фикстура с тестовыми данными для карт"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def empty_list() -> List:
    """Фикстура с пустым списком"""
    return []

@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура с тестовыми транзакциями для генераторов"""
    return [
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


@pytest.fixture
def transactions_without_descriptions() -> List[Dict[str, Any]]:
    """Фикстура с транзакциями без описаний"""
    return [
        {"id": 1},
        {"id": 2, "description": "Есть описание"},
        {"id": 3},
    ]


@pytest.fixture
def transactions_with_empty_descriptions() -> List[Dict[str, Any]]:
    """Фикстура с пустыми описаниями"""
    return [
        {"id": 1, "description": ""},
        {"id": 2, "description": "Описание 2"},
        {"id": 3, "description": ""},
        {"id": 4, "description": "Описание 4"},
    ]
