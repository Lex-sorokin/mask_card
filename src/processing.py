def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list:
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


def sort_by_date(operations: list, sorting: bool = True) -> list:
    """Функция, которая сортирует списки словарей по дате."""
    result = sorted(operations, key=lambda operation: operation.get("date"), reverse=sorting)
    return result

