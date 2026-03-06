import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGERATES_API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_currency(transaction):
    """
    Переводит сумму транзакции в рубли
    """

    try:
        op_amount = transaction["operationAmount"]
        summa = float(op_amount["amount"])
        valuta = op_amount["currency"]["code"]

        if valuta == "RUB":
            return summa

        if valuta == "USD" or valuta == "EUR":
            result = convert_to_rub(summa, valuta)
            return result

        return 0.0

    except (KeyError, ValueError):
        return 0.0


def convert_to_rub(amount, currency):
    """
    Конвертирует доллары или евро в рубли через API.
    """

    if not API_KEY:
        print("Нет API ключа! Проверьте файл .env")
        return 0.0

    headers = {"apikey": API_KEY}

    params = {"from": currency, "to": "RUB", "amount": amount}

    try:
        response = requests.get(API_URL, params=params, headers=headers)

        if response.status_code != 200:
            return 0.0

        data = response.json()
        result = data.get("result")

        if result is None:
            return 0.0

        return float(result)

    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return 0.0
