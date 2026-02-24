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
    new_sort = sorted(new_dict, key=lambda x: x.get("date", ""), reverse=reverse)
    return new_sort
