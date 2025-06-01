from typing import Union

_oper = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(operations: Union[list], state: str = "EXECUTED") -> list:
    """
    Фильтрует операции по статусу
    :param operations: список словарей (транзакций)
    :param state: статус операции для фильтрации
    :return: отфильтрованный список операций по статусу
    """
    result = []
    for operation in operations:
        if operation["state"] == state:
            result.append(operation)
    return result


def sort_by_date(operations: Union[list], sorting: bool = True) -> list:
    """Функция, которая сортирует списки словарей по дате."""
    result = sorted(operations, key=lambda operation: operation.get("date"), reverse=sorting)
    return result


if __name__ == "__main__":
    print(filter_by_state(_oper))
    print(sort_by_date(_oper))
