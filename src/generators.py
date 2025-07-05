from typing import Generator


def filter_by_currency(transactions_list: list, currency: str) -> Generator[list]:
    """
    Функция, которая принимает на вход список транзакций, и возвращает генератор выдающий списки транзакций по валюте
    """
    for transaction in transactions_list:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions_list: list) -> Generator[str]:
    """Функция, которая принимает на вход список транзакций, и возвращает описание каждой операции по очереди"""
    for transaction in transactions_list:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for i in range(start, end + 1):
        formatted = f"{i:016d}"
        formatted_with_spaces = " ".join([formatted[i:i + 4] for i in range(0, 16, 4)])
        yield formatted_with_spaces
