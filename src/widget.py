# Пример для карты
# Visa Platinum 7000792289606361  входной аргумент
# Visa Platinum 7000 79** **** 6361  выход функции

# Пример для счета
# Счет 73654108430135874305 входной аргумент
# Счет **4305 выход функции


def mask_account_card(number_card_or_account: str) -> str:
    """Функция принимает тип и номер карты или счета"""
    name_type = ""
    disguise_card_or_account = ""
    for symbol in number_card_or_account:
        if not symbol.isdigit():
            name_type += symbol
    if name_type == "Счет ":
        account_number = "**" + number_card_or_account[-4:]
        disguise_card_or_account += account_number
    else:
        card_number = (
            number_card_or_account[-16:-12]
            + " "
            + number_card_or_account[-12:-10]
            + "** **** "
            + number_card_or_account[-4:]
        )
        disguise_card_or_account += card_number
    return name_type + disguise_card_or_account


# "2024-03-11T02:26:18.671407" выход
# "ДД.ММ.ГГГГ"/"11.03.2024" выход


def get_date(client_date: str) -> str:
    """Принимает на вход дату и форматирует"""
    date_format = ""
    for item in client_date:
        date_format = client_date[8:10] + "." + client_date[5:7] + "." + client_date[:4]
    return date_format
