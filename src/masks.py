# 7000792289606361 - входной аргумент
# 7000 79** **** 6361 - выход функции


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    card_str = str(card_number)
    card_code = ""
    for i in card_str[7:14]:
        card_code += "*"
    result = card_str[:4] + " " + card_str[4:6] + card_code[2:4] + " " + card_code[3:] + " " + card_str[-4:]
    return result


total_card = get_mask_card_number(7000792289606361)
print(total_card)


# 73654108430135874305 - входной аргумент
# ** 4305 - выход функции


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    account_str = str(account_number)
    return f"** {account_str[-4:]}"


total_account = get_mask_account(73654108430135874305)
print(total_account)
