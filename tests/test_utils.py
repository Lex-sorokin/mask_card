from unittest.mock import mock_open, patch

from src.utils import open_json_file, process_bank_operation, search_transaction, transaction_amount


# Тест при верной и неверной (неполной) структуре JSON-файла
def test_open_json_file():
    with patch("builtins.open", mock_open(read_data='{"1" : "2"}')):
        assert open_json_file("") == {"1": "2"}
    with patch("builtins.open", mock_open(read_data='{"1" : "2"')):
        assert open_json_file("") == []
    assert open_json_file("") == []


def test_transaction_amount():
    assert transaction_amount(
        {"operationAmount": {"amount": "100", "currency": {"name": "RUB", "c": "RUB"}}}
    ) == 0.0
    assert transaction_amount(
        {"operationAmount": {"amount": "100", "currency": {"name": "RUB", "code": "RUB"}}}
    ) == 100
    with patch("requests.get") as r_mock:
        r_mock.return_value.json.return_value = {"result": 95}
        assert transaction_amount(
            {"operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}}}
        ) == 95


def test_search_transaction(transactions):
    assert search_transaction(transactions, 'Пере') == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "amount": "79114.93",
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "amount": "56883.54",
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "amount": "67314.70",
            "currency_name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_process_bank_operation(transactions):
    assert process_bank_operation(transactions, ["Перевод с карты на карту"]) == {
        'Перевод с карты на карту': 1
    }
