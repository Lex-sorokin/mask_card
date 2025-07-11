from typing import Union

from loger import module_logger

logger = module_logger(__name__)


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску"""
    logger.info('Функция get_mask_card_number запущена')
    card_number = card_number.replace(" ", "")
    masked_card_number = " ".join(card_number[i:i + 4] for i in range(0, len(card_number), 4))
    masked_card_number_list = list(masked_card_number)

    for i in range(len(masked_card_number_list)):
        if 7 <= i <= 13 and masked_card_number_list[i] != " ":
            masked_card_number_list[i] = "*"

    masked_card_number = "".join(masked_card_number_list)
    logger.info('Функция get_mask_card_number вернула замаскированный номер карты')
    return masked_card_number


def get_mask_account(card_number: Union[str]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    logger.info('Функция get_mask_account запущена')
    card_number = card_number.replace(" ", "")

    last_part = str(card_number[-4:])
    logger.info('Функция get_mask_account вернула замаскированный номер счёта')
    return f"**{last_part}"
