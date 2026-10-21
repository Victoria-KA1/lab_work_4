def my_reduce(function, iterable, initializer=None):
    """Собственная реализация functools.reduce."""
    iterator = iter(iterable)

    if initializer is None:
        try:
            accumulator = next(iterator)
        except StopIteration:
            raise TypeError("reduce() пустой последовательности без начального значения")
    else:
        accumulator = initializer

    for item in iterator:
        accumulator = function(accumulator, item)

    return accumulator


def main():
    numbers = [1, 2, 3, 4, 5]

    # Сумма
    total = my_reduce(lambda a, b: a + b, numbers)
    print(f"Сумма {numbers} = {total}")

    # Произведение
    product = my_reduce(lambda a, b: a * b, numbers)
    print(f"Произведение {numbers} = {product}")

    # С начальным значением
    total_with_initial = my_reduce(lambda a, b: a + b, numbers, 100)
    print(f"Сумма {numbers} с начальным 100 = {total_with_initial}")

    # Максимум
    maximum = my_reduce(lambda a, b: a if a > b else b, numbers)
    print(f"Максимум в {numbers} = {maximum}")


if __name__ == "__main__":
    main()
    input("Нажмите Enter для выхода...")