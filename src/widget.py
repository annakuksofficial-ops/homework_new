# Пример для карты
#Visa Platinum 7000792289606361  входной аргумент
#Visa Platinum 7000 79** **** 6361  выход функции

# Пример для счета
#Счет 73654108430135874305  входной аргумент
#Счет **4305  выход функции


def mask_account_card(number_card_or_account: str) -> str:
    """Функция принимает тип и номер карты или счета"""
    name_type = ""
    disguise_card_or_account = ""
    for symbol in number_card_or_account:
        if not symbol.isdigit():
            name_type += symbol
    if name_type == "Счет ":
        for symbol in number_card_or_account:
            account_number = "**" + number_card_or_account[-4:]
        disguise_card_or_account += account_number
    else:
        card_number = (number_card_or_account[-16:-12] + " " + number_card_or_account[-12:-10] + "** **** "
                     + number_card_or_account[-4:])
        disguise_card_or_account += card_number
    return name_type + disguise_card_or_account


if __name__ == "__main__":
    total_account = mask_account_card("Счет 35383033474447895560")
    print(total_account)