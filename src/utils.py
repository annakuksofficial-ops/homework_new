import json
import logging
import os

logger = logging.getLogger("utils")

os.makedirs("logs", exist_ok=True)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_transactions(file_path):
    """
    Загружает список транзакций из JSON файла
    """
    logger.info(f"Начинаем загрузку файла: {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"Файл не найден: {file_path}")
        print(f"Файл {file_path} не найден")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info(f"Файл загружен, размер: {len(data)} записей")

        if not isinstance(data, list):
            logger.error(f"Файл содержит не список, а {type(data)}")
            print("Файл содержит не список")
            return []

        clean_transactions = []
        for transaction in data:
            if transaction:  # если словарь не пустой
                clean_transactions.append(transaction)

        logger.info(f"Загружено {len(clean_transactions)} транзакций")
        print(f"Загружено {len(clean_transactions)} транзакций")
        return clean_transactions

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка парсинга JSON: {e}")
        print("Ошибка: файл не является валидным JSON")
        return []
    except Exception as error:
        logger.error(f"Неожиданная ошибка: {error}")
        print(f"Неожиданная ошибка: {error}")
        return []
