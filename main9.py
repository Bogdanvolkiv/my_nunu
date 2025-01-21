from functools import wraps
from time import sleep
from typing import Callable, Any


# Декоратор "Как дела?"
def how_are_you(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор, который спрашивает у пользователя 'Как дела?' и
    выводит предопределенное сообщение перед вызовом декорируемой функции.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        input('Как дела? ')  # Запрашиваем ответ у пользователя
        print('А у меня не очень! Ладно, держи свою функцию.')  # Печатаем сообщение
        return func(*args, **kwargs)  # Вызываем оригинальную функцию
    return wrapper


# Декоратор "Замедление"
def slowdown_2s(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор для замедления работы функции на 2 секунды.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        sleep(2)  # Задержка на 2 секунды
        return func(*args, **kwargs)  # Вызываем оригинальную функцию
    return wrapper


# Декоратор "Счётчик"
def counter(func: Callable) -> Callable:
    """
    Декоратор для подсчета количества вызовов функции.
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        wrapper.count += 1  # Увеличиваем счетчик
        print(f"Функцию '{func.__name__}' вызвали {wrapper.count} раз")
        return func(*args, **kwargs)
    
    wrapper.count = 0  # Инициализируем счетчик
    return wrapper


# Декоратор "Кэширование"
def cache_decorator(func):
    """
    Декоратор для кэширования результатов функции.
    """
    cache = {}  # Словарь для хранения кэшированных результатов

    def wrapper(number):
        if number in cache:
            return cache[number]  # Возвращаем результат из кэша, если он есть
        result = func(number)
        cache[number] = result  # Сохраняем результат в кэше
        return result

    return wrapper


# Пример применения всех декораторов

@how_are_you
@slowdown_2s
@counter
@cache_decorator
def fibonacci(number: int) -> int:
    """Вычисление числа Фибоначчи с использованием рекурсии."""
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Пример использования всех декораторов на одной функции
if __name__ == "__main__":
    print(fibonacci(10))  # Результат будет вычислен и закэширован
    print(fibonacci(10))  # Результат будет взят из кэша
    print(fibonacci(5))   # Результат будет вычислен и закэширован
