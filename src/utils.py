import json
import os


def load_transactions(file_path):
    """
    Загружает список транзакций из JSON файла
    """

    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Файл содержит не список")
            return []

        clean_transactions = []
        for transaction in data:
            if transaction:  # если словарь не пустой
                clean_transactions.append(transaction)

        print(f"Загружено {len(clean_transactions)} транзакций")
        return clean_transactions

    except json.JSONDecodeError:
        print("Ошибка: файл не является валидным JSON")
        return []
    except Exception as error:
        print(f"Неожиданная ошибка: {error}")
        return []
