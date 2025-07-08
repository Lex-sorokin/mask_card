from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_csv_excel import read_csv, read_excel
from src.utils import open_json_file, search_transaction
from src.widget import get_date, mask_account_card


def main():
    """
    Функция, которая объединяет все модули проекта.
    """
    transaction_data: list[dict] = []
    print("""
    Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    """)
    print("""Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """)
    user_choice = input('Введите номер пункта меню: ')
    while user_choice not in ("1", "2", "3"):
        print("Неверный ввод. Пожалуйста выберите один из предложенных пунктов меню.")
        user_choice = input('Введите номер пункта меню: ')

    if user_choice == '1':
        transaction_data = open_json_file("data/operations.json")
        print("Для обработки выбран JSON-файл.")
    elif user_choice == '2':
        transaction_data = read_csv("data/transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif user_choice == '3':
        transaction_data = read_excel("data/transactions_excel.xlsx")
        print("Для обработки выбран EXCEL-файл.")

    user_input = input("""Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    Введите статус: """).upper()
    while user_input not in ("EXECUTED", "CANCELED", "PENDING"):
        print(f"Статус операции {user_input} недоступен.")
        user_input = input("""
        Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
        """).upper()
    transaction_data = filter_by_state(transaction_data, state=user_input)
    print(f'Операции отфильтрованы по статусу {user_input}')

    print("Отсортировать операции по дате? Да/Нет")

    user_input = input().upper()
    while user_input not in ("ДА", "НЕТ"):
        print("Выберите только из вариантов Да/Нет")

        print("Отсортировать по возрастанию или по убыванию?")
        user_input = input().upper()
        while user_input not in ("ПО ВОЗРАСТАНИЮ", "ПО УБЫВАНИЮ"):
            print("Выберите только из вариантов 'по возрастанию'/'по убыванию'")
            if user_input == "ПО ВОЗРАСТАНИЮ":
                sorting = False
                transaction_data = sort_by_date(transaction_data, sorting)
            else:
                sorting = True
                transaction_data = sort_by_date(transaction_data, sorting)

    user_input = input('Выводить только рублевые транзакции? Да/Нет: ').lower()
    if user_input == 'да':
        transaction_data = list(filter_by_currency(transaction_data, "RUB"))

    user_input = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ').upper()
    if user_input == 'ДА':
        user_input = input('Введите слово для поиска: ')
        transaction_data = search_transaction(transaction_data, user_input)

    print('Распечатываю итоговый список транзакций...')
    print(f"Всего банковских операций в выборке: {len(transaction_data)}")
    for i in transaction_data:
        from_ = mask_account_card(i.get('from')) + ' -> ' if i.get('from') else ""
        date_ = i.get('date') or 'по умолчанию'
        description_ = i.get('description') or 'по умолчанию'
        amount_ = i.get('operationAmount', {}).get('amount') or i.get('amount')
        to_ = i.get('to') or 'по умолчанию'
        currency_code_ = i.get('currency_code') or i.get('operationAmount', {}).get('currency', {}).get('name')

        print(f"{get_date(date_)} {description_}\n"
              f"{from_}{mask_account_card(to_)}\n"
              f"Сумма: {amount_} {currency_code_}\n")


if __name__ == "__main__":
    main()
