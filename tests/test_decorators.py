import os
import tempfile

import pytest

from src.decorators import log


def test_log_console_success():
    """
    Проверяем, что декоратор правильно логирует в консоль
    """
    @log()
    def add_numbers(a, b):
        return a + b
    result = add_numbers(5, 3)
    assert result == 8


def test_log_console_error(capsys):
    """
    Проверяем, что декоратор правильно логирует ошибки в консоль.
    """
    @log()
    def divide_numbers(a, b):
        return a / b
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)
    captured = capsys.readouterr()
    assert "divide_numbers error: ZeroDivisionError" in captured.out
    assert "Inputs: (10, 0), {}" in captured.out


def test_log_file_success():
    """
    Тест 3: Проверяем, что декоратор правильно записывает логи в файл
    при успешном выполнении функции.
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp_file:
        filename = tmp_file.name

    try:
        @log(filename=filename)
        def multiply_numbers(a, b):
            return a * b
        result = multiply_numbers(4, 5)
        assert result == 20
        with open(filename, 'r') as f:
            log_content = f.read().strip()
        assert log_content == "multiply_numbers ok"
    finally:
        # Удаляем временный файл
        if os.path.exists(filename):
            os.unlink(filename)


def test_log_file_error():
    """
    Проверяем, что декоратор правильно записывает ошибки в файл.
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp_file:
        filename = tmp_file.name
    try:
        @log(filename=filename)
        def get_list_element(my_list, index):
            return my_list[index]
        with pytest.raises(IndexError):
            get_list_element([1, 2, 3], 10)
        with open(filename, 'r') as f:
            log_content = f.read().strip()
        assert "get_list_element error: IndexError" in log_content
        assert "Inputs: ([1, 2, 3], 10), {}" in log_content

    finally:
        if os.path.exists(filename):
            os.unlink(filename)


def test_log_with_kwargs(capsys):
    """
    Проверяем, что декоратор работает с именованными аргументами.
    """
    @log()
    def greet(name, greeting="Привет"):
        return f"{greeting}, {name}!"
    result = greet("Вася", greeting="Здравствуй")
    assert result == "Здравствуй, Вася!"
    captured = capsys.readouterr()
    assert "greet ok" in captured.out


def test_log_preserves_function_name():
    """
    Тест 6: Проверяем, что декоратор не меняет имя функции.
    """
    @log()
    def my_special_function():
        """Это моя особенная функция"""
        return 42
    assert my_special_function.__name__ == "my_special_function"
    assert my_special_function.__doc__ == "Это моя особенная функция"


def test_log_multiple_calls(capsys):
    """
    Тест 7: Проверяем, что декоратор работает при нескольких вызовах.
    """
    @log()
    def say_hello():
        return "Hello!"
    say_hello()
    say_hello()
    say_hello()
    captured = capsys.readouterr()
    assert captured.out.count("say_hello ok") == 3


def test_log_different_functions(capsys):
    """
    Тест 8: Проверяем, что декоратор работает с разными функциями.
    """

    @log()
    def func1():
        return 1

    @log()
    def func2():
        return 2

    func1()
    func2()

    captured = capsys.readouterr()

    assert "func1 ok" in captured.out
    assert "func2 ok" in captured.out


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),  # Первый тест: 1 + 2 = 3
    (5, 5, 10),  # Второй тест: 5 + 5 = 10
    (0, 0, 0),  # Третий тест: 0 + 0 = 0
])
def test_log_parametrized(capsys, a, b, expected):
    """
    Тест 9: Параметризованный тест - запускается несколько раз с разными данными.
    Проверяем, что декоратор работает с разными входными параметрами.
    """
    @log()
    def add(a, b):
        return a + b

    result = add(a, b)

    assert result == expected

    captured = capsys.readouterr()

    assert "add ok" in captured.out


def test_log_file_append_mode():
    """
    Тест 10: Проверяем, что логи ДОБАВЛЯЮТСЯ в файл, а не перезаписывают его.
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp_file:
        filename = tmp_file.name

    try:
        @log(filename=filename)
        def test_func(x):
            return x * 2
        test_func(2)  # Первый лог
        test_func(4)  # Второй лог
        test_func(6)  # Третий лог
        with open(filename, 'r') as f:
            lines = f.readlines()
        assert len(lines) == 3
        assert lines[0].strip() == "test_func ok"
        assert lines[1].strip() == "test_func ok"
        assert lines[2].strip() == "test_func ok"

    finally:
        if os.path.exists(filename):
            os.unlink(filename)
