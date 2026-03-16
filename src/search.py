import re
from collections import Counter
from typing import Any, Dict, List


def filter_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Фильтрует транзакции по наличию строки поиска в описании.
    """
    result = []

    for transaction in transactions:
        description = transaction.get("description", "")
        if re.search(search_string, description, re.IGNORECASE):
            result.append(transaction)

    return result


def count_transactions_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций по заданным категориям.
    """
    descriptions = [t.get("description", "") for t in transactions]

    counter = Counter()

    for category in categories:
        count = 0
        for desc in descriptions:
            if re.search(category, desc, re.IGNORECASE):
                count += 1
        counter[category] = count

    return dict(counter)
