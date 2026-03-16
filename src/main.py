from src.file_readers import read_csv_file, read_excel_file
from src.processing import filter_by_state, sort_by_date
from src.search import filter_by_description
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


def main():
    """Главная функция программы"""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    transactions = []

    if choice == "1":
        print("\nДля обработки выбран JSON-файл.")
        transactions = load_transactions("data/operations.json")
    elif choice == "2":
        print("\nДля обработки выбран CSV-файл.")
        transactions = read_csv_file("data/transactions.csv")
    elif choice == "3":
        print("\nДля обработки выбран XLSX-файл.")
        transactions = read_excel_file("data/transactions_excel.xlsx")
    else:
        print("\nНеверный выбор. Загружаем JSON-файл.")
        transactions = load_transactions("data/operations.json")

    if not transactions:
        print("Не удалось загрузить транзакции. Программа завершена.")
        return

    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные статусы: EXECUTED, CANCELED, PENDING")

        status = input("Пользователь: ")
        status = status.upper()

        if status in valid_statuses:
            print(f'\nОперации отфильтрованы по статусу "{status}"')
            transactions = filter_by_state(transactions, status)
            break
        else:
            print(f'Статус "{status}" недоступен.')

    print("\nОтсортировать операции по дате? Да/Нет")
    sort_choice = input("Пользователь: ")
    sort_choice = sort_choice.lower()

    if sort_choice == "да" or sort_choice == "yes" or sort_choice == "д":
        print("\nОтсортировать по возрастанию или по убыванию?")
        order = input("Пользователь: ")
        order = order.lower()

        if "убыв" in order:
            transactions = sort_by_date(transactions, reverse=True)
        else:
            transactions = sort_by_date(transactions, reverse=False)

    print("\nВыводить только рублевые транзакции? Да/Нет")
    rub_choice = input("Пользователь: ")
    rub_choice = rub_choice.lower()

    if rub_choice == "да" or rub_choice == "yes" or rub_choice == "д":
        rub_transactions = []
        for t in transactions:
            try:
                op_amount = t.get("operationAmount", {})
                currency = op_amount.get("currency", {}).get("code", "")
                if currency == "RUB":
                    rub_transactions.append(t)
            except Exception:
                pass
        transactions = rub_transactions

    print("\nОтфильтровать по слову в описании? Да/Нет")
    search_choice = input("Пользователь: ")
    search_choice = search_choice.lower()

    if search_choice == "да" or search_choice == "yes" or search_choice == "д":
        print("\nВведите слово для поиска:")
        search_word = input("Пользователь: ")
        transactions = filter_by_description(transactions, search_word)

    print("\nРаспечатываю итоговый список транзакций...")

    if not transactions:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"\nВсего банковских операций в выборке: {len(transactions)}")
    print()

    for t in transactions:
        # Дата
        date_str = t.get("date", "")
        if date_str:
            formatted_date = get_date(date_str)
        else:
            formatted_date = "Неизвестная дата"

        description = t.get("description", "")

        from_info = t.get("from", "")
        to_info = t.get("to", "")

        # Сумма
        try:
            op_amount = t.get("operationAmount", {})
            amount = op_amount.get("amount", "0")
            currency = op_amount.get("currency", {}).get("code", "RUB")
            amount_display = f"{amount} {currency}"
        except Exception:
            amount_display = "Сумма неизвестна"

        print(f"{formatted_date} {description}")

        if from_info and to_info:
            print(f"{mask_account_card(from_info)} -> {mask_account_card(to_info)}")
        elif to_info:
            print(f"{mask_account_card(to_info)}")

        print(f"Сумма: {amount_display}")
        print()


if __name__ == "__main__":
    main()
