import requests, os
from dotenv import load_dotenv

load_dotenv()

def converter(currency: str, sum_operation: str) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях."""
    for_currency = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={for_currency}&from={currency}&amount={sum_operation}"

    payload = {}
    headers= {
      "apikey": os.getenv("API_KEY")
    }

    response = requests.get( url, headers=headers, data = payload)

    return response.json()['result']
