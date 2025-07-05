from unittest.mock import patch

from src.read_csv_excel import read_csv, read_excel


@patch("pandas.read_csv")
def test_read_csv(mock_read_csv):
    operations = [
        {
            'id': 1245327.0,
            'state': 'PENDING',
            'date': '2021-03-09T00:56:48Z',
            'amount': 24252.0,
            'currency_name': 'Somoni',
            'currency_code': 'TJS',
            'from': 'Discover 3233958335206913',
            'to': 'Visa 6269545625045856',
            'description': 'Перевод с карты на карту'
        }
    ]
    mock_read_csv.return_value.to_dict.return_value = operations
    result = read_csv("test.csv")
    assert result == operations


@patch("pandas.read_excel")
def test_read_excel(mock_read_excel):
    operations = [
        {
            'id': 1245327.0,
            'state': 'PENDING',
            'date': '2021-03-09T00:56:48Z',
            'amount': 24252.0,
            'currency_name': 'Somoni',
            'currency_code': 'TJS',
            'from': 'Discover 3233958335206913',
            'to': 'Visa 6269545625045856',
            'description': 'Перевод с карты на карту'
        }
    ]
    mock_read_excel.return_value.to_dict.return_value = operations
    result = read_excel("test.xlsx")
    assert result == operations
