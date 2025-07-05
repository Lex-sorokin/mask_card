# Виджет банковских операций клиента.

## Данный виджет предназначен для банковских операций клиента:
1. Маскировка номера карты клиента;
2. Маскировка номера счета клиента;
3. Умеет принимать на вход строку с датой в одном и
возвращает строку с датой в формате "ДД.ММ.ГГГГ"



Установка


1. Клонируйте репозиторий:

git clone
git@github.com:Lex-sorokin/mask_card.git

2. Перейдите в директорию проекта:

C:\Users\Admin\PycharmProjects\package-roman


3. Установите необходимые зависимости:

poetry install


Использование

Примеры использования функций:

from src.masks import get_mask_account, get_mask_card_number

# Пример использования get_mask_card_number

print(get_mask_card_number("1234567812345678"))

# Пример использования get_mask_account

print(get_mask_account("123456"))


from src.processing import filter_by_state, sort_by_date

# Пример использования filter_by_state
print(
filter_by_state(
[
{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
)
)

# Пример использования sort_by_date
print(
sort_by_date(
[
{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
)
)
# Пример работы генератора filter_by_currency
assert next(generator) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }

# Пример работы генератора test_transaction_descriptions
assert next(generator) == "Перевод организации"

# Пример работы генератора test_card_number_generator
assert next(gen) == "0000 0000 0000 0005"

## Cоздан модуль decorators
Реализован декоратор log
Декоратор может логировать работу функции и ее результат как в файл, 
так и в консоль.

## Созданы модули utils, external_api
Функция open_json_file в модуле utils преобразует JSON-объект в Pyton-объект.
Функция transaction_amount в модуле utils конвертирует валюту в рубли.
Функция converter в модуле external_api принимает на вход транзакцию и возвращает сумму транзакции в рублях.

## Созданы логеры для функций из модулей utils и masks.
Результаты работы логеров находятся в файлах logs/masks.log и logs/utils.log

## Тесты

Структура тестов:

```
tests/
├── test_masks.py # Тесты масок (проверены 2 функции)
├── test_processing.py # Тесты обработки (проверены 2 функции)
├── test_widget.py # Тесты виджетов (5 параметризованных тестов, 2 теста функций)
├── test_generators.py # Тесты генераторов (тест 1 функции фикстурой, 2 теста функций)
├── test_decorators.py # Тесты декораторов (3 теста декоратора)
├── test_utils.py # Тесты функций, в том числе с помощью метода "Mock"
└── test_external_api.py # Тест конвертора
```
Покрытие тестами 100%