import logging
import os

logger = logging.getLogger("masks")

os.makedirs("logs", exist_ok=True)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


# 7000792289606361 - входной аргумент
# 7000 79** **** 6361 - выход функции


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    try:
        card_str = str(card_number)

        if len(card_str) < 16:
            logger.error(f"Номер карты слишком короткий: {len(card_str)}")
            raise ValueError("Номер карты слишком короткий")

        card_code = ""
        for i in card_str[7:14]:
            card_code += "*"
        result = card_str[:4] + " " + card_str[4:6] + card_code[2:4] + " " + card_code[3:] + " " + card_str[-4:]

        logger.info("Номер карты успешно замаскирован")
        return result

    except Exception as e:
        logger.error(f"Ошибка при маскировке карты: {e}")
        raise


total_card = get_mask_card_number(7000792289606361)
print(total_card)


# 73654108430135874305 - входной аргумент
# ** 4305 - выход функции


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    try:
        account_str = str(account_number)

        if len(account_str) < 4:
            logger.error(f"Номер счета слишком короткий: {len(account_str)}")
            raise ValueError("Номер счета слишком короткий")

        result = f"** {account_str[-4:]}"
        logger.info("Номер счета успешно замаскирован")
        return result

    except Exception as e:
        logger.error(f"Ошибка при маскировке счета: {e}")
        raise


total_account = get_mask_account(73654108430135874305)
print(total_account)

if __name__ == "__main__":

    print("Тестируем маскировку карты:")
    card = get_mask_card_number(7000792289606361)
    print(card)

    print("\nТестируем маскировку счета:")
    account = get_mask_account(73654108430135874305)
    print(account)

    print("Логи должны быть в папке logs")
