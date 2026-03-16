from src.search import count_transactions_by_category, filter_by_description


def test_filter_by_description_finds_something():
    """Тест: ищем слово и находим транзакции"""

    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
    ]

    result = filter_by_description(transactions, "перевод")

    assert len(result) == 2
    assert result[0]["description"] == "Перевод организации"
    assert result[1]["description"] == "Перевод с карты на карту"


def test_filter_by_description_finds_nothing():
    """Тест: ищем слово, которого нет"""

    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
    ]

    result = filter_by_description(transactions, "вклад")

    assert len(result) == 0
    assert result == []


def test_filter_by_description_ignores_case():
    """Тест: поиск работает без учета регистра"""

    transactions = [
        {"description": "ПЕРЕВОД ОРГАНИЗАЦИИ"},
        {"description": "перевод с карты на карту"},
        {"description": "Открытие вклада"},
    ]

    result = filter_by_description(transactions, "перевод")

    assert len(result) == 2
    assert result[0]["description"] == "ПЕРЕВОД ОРГАНИЗАЦИИ"
    assert result[1]["description"] == "перевод с карты на карту"


def test_count_transactions_by_category_works():
    """Тест: подсчет по категориям"""

    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
        {"description": "Перевод со счета на счет"},
    ]

    categories = ["Перевод", "Вклад"]
    result = count_transactions_by_category(transactions, categories)

    assert result["Перевод"] == 3
    assert result["Вклад"] == 1


def test_count_transactions_by_category_empty():
    """Тест: пустой список транзакций"""

    transactions = []
    categories = ["Перевод", "Вклад"]

    result = count_transactions_by_category(transactions, categories)

    assert result["Перевод"] == 0
    assert result["Вклад"] == 0
