from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_works(sample_card_data: List[Dict[str, Any]]) -> None:
    """Проверяем, что фильтрация работает"""
    result = filter_by_state(sample_card_data, "EXECUTED")
    assert len(result) == 2
    assert result[0]["state"] == "EXECUTED"
    assert result[1]["state"] == "EXECUTED"


def test_filter_by_state_no_matches(sample_card_data: List[Dict[str, Any]]) -> None:
    """Проверяем, когда нет совпадений"""
    result = filter_by_state(sample_card_data, "PENDING")
    assert result == []


def test_filter_by_state_empty(empty_list: List) -> None:
    """Проверяем с пустым списком"""
    result = filter_by_state(empty_list, "EXECUTED")
    assert result == []


def test_sort_by_date_descending(sample_card_data: List[Dict[str, Any]]) -> None:
    """Проверяем сортировку от новых к старым"""
    result = sort_by_date(sample_card_data, reverse=True)
    assert result[0]["date"] == "2019-07-03T18:35:29.512364"
    assert result[-1]["date"] == "2018-06-30T02:08:58.425572"


def test_sort_by_date_ascending(sample_card_data: List[Dict[str, Any]]) -> None:
    """Проверяем сортировку от старых к новым"""
    result = sort_by_date(sample_card_data, reverse=False)
    assert result[0]["date"] == "2018-06-30T02:08:58.425572"
    assert result[-1]["date"] == "2019-07-03T18:35:29.512364"


def test_sort_by_date_default(sample_card_data: List[Dict[str, Any]]) -> None:
    """Проверяем значение по умолчанию"""
    result = sort_by_date(sample_card_data)
    assert result[0]["date"] == "2019-07-03T18:35:29.512364"


def test_sort_by_date_empty(empty_list: List) -> None:
    """Проверяем сортировку пустого списка"""
    result = sort_by_date(empty_list)
    assert result == []


def test_filter_by_state_with_none_values() -> None:
    """Тест фильтрации с None значениями в state"""
    data = [
        {"id": 1, "state": None, "date": "2023-01-01"},
        {"id": 2, "state": "EXECUTED", "date": "2023-01-02"},
        {"id": 3, "state": "CANCELED", "date": "2023-01-03"}]
    result = filter_by_state(data, "EXECUTED")
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_by_state_missing_state_key() -> None:
    """Тест фильтрации когда у некоторых словарей нет ключа state"""
    data = [
        {"id": 1, "date": "2023-01-01"},
        {"id": 2, "state": "EXECUTED", "date": "2023-01-02"},
        {"id": 3, "date": "2023-01-03"}]
    result = filter_by_state(data, "EXECUTED")
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_by_state_with_different_state_values() -> None:
    """Тест фильтрации с разными значениями state"""
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "PENDING"},
        {"id": 4, "state": "EXECUTED"},
    ]
    result = filter_by_state(data, "EXECUTED")
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 4

    result = filter_by_state(data, "PENDING")
    assert len(result) == 1
    assert result[0]["id"] == 3


def test_sort_by_date_with_same_dates() -> None:
    """Тест сортировки когда даты одинаковые"""
    data = [
        {"id": 1, "date": "2023-01-01"},
        {"id": 2, "date": "2023-01-01"},
        {"id": 3, "date": "2023-01-01"}]
    result = sort_by_date(data, reverse=True)
    assert len(result) == 3
    ids = [item["id"] for item in result]
    assert 1 in ids
    assert 2 in ids
    assert 3 in ids


def test_sort_by_date_with_missing_dates() -> None:
    """Тест сортировки когда у некоторых нет даты"""
    data = [
        {"id": 1, "date": "2023-01-03"},
        {"id": 2},
        {"id": 3, "date": "2023-01-01"},
        {"id": 4},
        {"id": 5, "date": "2023-01-02"}]
    result = sort_by_date(data, reverse=False)
    assert result[0]["id"] in [2, 4]
    assert result[1]["id"] in [2, 4]
    assert result[2]["id"] == 3
    assert result[3]["id"] == 5
    assert result[4]["id"] == 1


def test_sort_by_date_with_invalid_date_format() -> None:
    """Тест сортировки с некорректным форматом даты"""
    data = [
        {"id": 1, "date": "2023-01-01"},
        {"id": 2, "date": "неправильная дата"},
        {"id": 3, "date": "2023/01/02"},
        {"id": 4, "date": "2023-01-03"},]
    result = sort_by_date(data)
    assert len(result) == 4


@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 1),
    ("PENDING", 0)])
def test_filter_by_state_parametrized(sample_card_data: List[Dict[str, Any]], state: str, expected_count: int) -> None:
    """Параметризованный тест фильтрации"""
    result = filter_by_state(sample_card_data, state)
    assert len(result) == expected_count


@pytest.mark.parametrize("reverse, first_id, last_id", [(True, 41428829, 939719570), (False, 939719570, 41428829)])
def test_sort_by_date_parametrized(sample_card_data: List[Dict[str, Any]],
                                   reverse: bool,
                                   first_id: int,
                                   last_id: int) -> None:
    """Параметризованный тест сортировки"""
    result = sort_by_date(sample_card_data, reverse=reverse)
    assert result[0]["id"] == first_id
    assert result[-1]["id"] == last_id


def test_filter_by_state_with_complex_data() -> None:
    """Тест фильтрации со сложными данными"""
    data = [
        {"id": 1, "state": "EXECUTED", "amount": 100},
        {"id": 2, "state": "CANCELED", "amount": 200, "comment": "test"},
        {"id": 3, "state": "EXECUTED", "amount": 300, "tags": ["a", "b"]}]
    result = filter_by_state(data, "EXECUTED")
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3
