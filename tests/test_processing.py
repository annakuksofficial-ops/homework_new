from typing import Any, Dict, List

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
