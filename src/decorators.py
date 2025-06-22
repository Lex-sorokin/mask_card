from typing import Any, Callable, Optional


def write_log(message: str, filename: Optional[str] = None) -> None:
    """
    Функция, которая записывает результат выполнения функции foo() в файл.
    """
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message)
    else:
        print(message)


def log(filenane: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования функции с настройками.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} - OK - {result}\n"
                write_log(message, filenane)
                return result
            except Exception as e:
                message = f"{func.__name__} - {type(e)} - args: {args} - kwargs: {kwargs}\n"
                write_log(message, filenane)
                raise
        return wrapper
    return decorator


@log()
def foo(x: int, y: int) -> int:
    return x + y
