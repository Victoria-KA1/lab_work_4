def filter_even(numbers):
    """Возвращает список только чётных чисел."""
    return list(filter(lambda x: x % 2 == 0, numbers))


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 21, 30]
    print(f"Исходный список: {numbers}")
    print(f"Чётные числа:    {filter_even(numbers)}")


if __name__ == "__main__":
    main()
    input("Нажмите Enter для выхода...")