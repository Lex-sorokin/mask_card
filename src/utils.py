import json

from loger import module_logger
from src.external_api import converter

logger = module_logger(__name__)


def open_json_file(path: str) -> list[dict]:
    """Функция, которая преобразует JSON-объект в Pyton-объект"""
    logger.info('Функция open_json_file запущена')
    try:
        with open(path, "r", encoding="utf-8") as f:
            logger.info('Функция преобразовала JSON-объект в Pyton-объект')
            return json.load(f)
    except json.JSONDecodeError:
        logger.error('Ошибка формата JSON-объекта')
        return []
    except Exception as e:
        logger.error(f'Ошибка: {e}')
        return []


def transaction_amount(transaction: dict) -> float:
    """Функция, которая конвертирует валюту в рубли"""
    logger.info('Функция transaction_amount запущена')
    try:
        if transaction['operationAmount']["currency"]["code"] == "RUB":
            logger.info('Функция вернула сумму в рублях')
            return float(transaction['operationAmount']["amount"])
        else:
            currency = transaction['operationAmount']["currency"]["code"]
            amount = transaction['operationAmount']["amount"]
            logger.info('Функция вернула конвертированную сумму в рублях')
            return float(converter(currency, amount))
    except (KeyError, ValueError) as d:
        logger.error(f'Ошибка: {d}')
        return 0.0
