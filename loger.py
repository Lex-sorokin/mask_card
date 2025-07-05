import logging
import os.path

from config import ROOT_DIR

# Попытался создать декоратор для логера, получилось сомнительно, пока решил не использовать.

# def logger_decorator(name):
#     print(name)


#     def wrapper(func):
#         logger = module_logger(name)
#         @wraps(func)


#         def inner(*args, **kwargs):
#             logger.info(f'Функция {func.__name__} с аргументами {args}, {kwargs} запущена')
#             try:
#                 result = func(*args, **kwargs)
#                 logger.info(f'Функция {func.__name__} успешно завершена')
#                 return result
#             except Exception as e:
#                 logger.error(f'[{func.__name__}] завершен с ошибкой {e}')
#             return None
#         return inner
#     return wrapper

def module_logger(name):
    logger = logging.getLogger(name)
    path = str(os.path.join(ROOT_DIR, 'logs', name.split('.')[1] + '.log'))
    file_handler = logging.FileHandler(path, "w", "utf-8")
    file_formatter = logging.Formatter(f'%(asctime)s %(filename)s %(levelname)s: модуль {name} %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger
