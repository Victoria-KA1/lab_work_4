import time
from functools import wraps


def timer(func):
    """Декоратор, который замеряет время выполнения функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Функция '{func.__name__}' выполнялась {end - start:.6f} секунд")
        return result
    return wrapper


@timer
def slow_function():
    """Искусственно медленная функция для демонстрации."""
    total = 0
    for i in range(1_000_000):
        total += i
    return total


@timer
def fast_function():
    return sum(range(100))


def main():
    print("Запуск slow_function...")
    slow_function()

    print("\nЗапуск fast_function...")
    fast_function()


if __name__ == "__main__":
    main()
    input("Нажмите Enter для выхода...")