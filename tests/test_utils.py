from unittest.mock import mock_open, patch

from src.utils import open_json_file, transaction_amount


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
