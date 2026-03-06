import json
import os

from src.utils import load_transactions


def test_load_transactions_file_exists():
    """Тест: файл существует"""
    with open("test_data.json", "w") as f:
        json.dump([{"id": 1}, {"id": 2}], f)

    result = load_transactions("test_data.json")
    assert len(result) == 2

    os.remove("test_data.json")


def test_load_transactions_file_not_found():
    """Тест: файла нет"""
    result = load_transactions("no_file.json")
    assert result == []


def test_load_transactions_empty_file():
    """Тест: пустой файл"""
    with open("empty.json", "w") as f:
        pass

    result = load_transactions("empty.json")
    assert result == []

    os.remove("empty.json")


def test_load_transactions_with_empty_dicts():
    """Тест: есть пустые словари"""
    with open("test.json", "w") as f:
        json.dump([{"id": 1}, {}, {"id": 2}], f)

    result = load_transactions("test.json")
    assert len(result) == 2

    os.remove("test.json")
