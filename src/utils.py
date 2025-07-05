import json

from src.external_api import converter


def open_json_file(path: str) -> list[dict]:
    """Функция, которая преобразует JSON-объект в Pyton-объект"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    except Exception:
        return []


def transaction_amount(transaction: dict) -> float:
    """Функция, которая конвертирует валюту в рубли"""
    # currency = transaction['operationAmount']["currency"]["code"]
    # amount = transaction['operationAmount']["amount"]
    try:
        if transaction['operationAmount']["currency"]["code"] == "RUB":
            return float(transaction['operationAmount']["amount"])
        else:
            currency = transaction['operationAmount']["currency"]["code"]
            amount = transaction['operationAmount']["amount"]
            return float(converter(currency, amount))
    except (KeyError, ValueError):
        return 0.0
