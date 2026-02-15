import pytest


@pytest.fixture
def sample_card_data() -> list:
    """Фикстура с тестовыми данными для карт"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def empty_list() -> list:
    """Фикстура с пустым списком"""
    return []
