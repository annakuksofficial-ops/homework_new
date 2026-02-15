from typing import Any


def filter_by_state(new_list: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция фильтрует список словарей по значению ключа 'state'.
    Она принимает список словарей и параметр state, по которому
    происходит фильтрация. Далее возвращает новый список, содержащий
    только словари с указанным статусом"""
    update_list = []
    for item_dict in new_list:
        if item_dict.get("state") == state:
            update_list.append(item_dict)
    return update_list


def sort_by_date(new_dict: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция сортирует список словарей по значению ключа 'date'.
    Она принимает список словарей и параметр reverse для определения
    порядка сортировки. Возвращает отсортированный список"""
    new_sort = sorted(new_dict, key=lambda x: x["date"], reverse=reverse)
    return new_sort


if __name__ == "__main__":
    test_key = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    sorted_key = filter_by_state(test_key, state="EXECUTED")
    test_data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    sorted_data = sort_by_date(test_data, reverse=True)
    print(sorted_data)
