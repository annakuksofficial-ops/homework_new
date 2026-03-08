import csv
from typing import Any, Dict, List

import pandas as pd


def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает CSV файл и возвращает список транзакций.
    """
    transactions = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                clean_row = {k: v for k, v in row.items() if v != ""}
                transactions.append(clean_row)

        return transactions

    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
        return []
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
        return []


def read_excel_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает Excel файл и возвращает список транзакций.
    """
    try:
        df = pd.read_excel(file_path)

        transactions = df.to_dict("records")

        clean_transactions = []
        for transaction in transactions:
            clean_transaction = {k: v for k, v in transaction.items() if pd.notna(v)}
            clean_transactions.append(clean_transaction)

        return clean_transactions

    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
        return []
    except Exception as e:
        print(f"Ошибка при чтении Excel: {e}")
        return []
