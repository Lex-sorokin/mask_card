import re
from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: Union[str]) -> str:
    """Функция, которая принимает тип и номер карты или счета и возвращает строку с замаскированным номером"""

    match = re.match(r"([^\d]+)(\d+)", card_info, re.UNICODE)

    if match:
        type = match.group(1).strip()  # "Visa Platinum"
        number = match.group(2)  # "7000792289606361"
    else:
        print("Строка не соответствует формату")

    if type == "Счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{type} {masked_number}"


def get_date(date: Union[str]) -> str:
    """Функция, которая принимает строку с датой в кривом формате и возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    correct_date = date[8:10] + "." + date[5:7] + "." + date[:4]
    return correct_date


print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))
