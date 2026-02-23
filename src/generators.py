from typing import List, Dict, Any, Iterator, Generator


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str = "USD") -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по валюте в аргументе 'currency':
    Проверяем, есть ли в транзакции поле operationAmount с валютой.
    Если она совпадает с искомой в 'currency', возвращаем транзакцию"""

    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        currency_info = operation_amount.get("currency", {})
        transaction_currency = currency_info.get("code")

        if transaction_currency == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Генератор, который возвращает описания каждой транзакции по очереди"""
    for transaction in transactions:
        description = transaction.get("description", "")
        if description:
            yield description


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генератор номеров банковских карт в диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    for num in range(start, stop + 1):
        num_str = str(num).zfill(16)
        card_number = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"
        yield card_number
