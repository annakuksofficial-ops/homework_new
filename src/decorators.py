import functools


def log(filename=None):
    """
    Декоратор для логирования вызовов функций.
    Если указан filename - записывает логи в файл.
    Если filename не указан - выводит логи в консоль.
    """

    def decorator(func):
        """
        Внутренняя функция-декоратор, которая оборачивает нашу функцию.
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Обертка вокруг функции, которая добавляет логирование.
            """
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                return result

            except Exception as error:
                message = f"{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                raise

        return wrapper

    return decorator
