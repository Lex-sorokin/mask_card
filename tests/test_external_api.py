from unittest.mock import patch
import pytest
from src.external_api import converter


def test_currency_convertor():
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"result": 7860.9512}
        result = converter("USD", 100.0)
        assert result == 7860.9512