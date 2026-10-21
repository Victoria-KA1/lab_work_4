def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime_generator(limit):
    """Генератор простых чисел от 2 до limit."""
    for number in range(2, limit + 1):
        if is_prime(number):
            yield number


def main():
    limit = int(input("Введите верхнюю границу: "))
    primes = list(prime_generator(limit))
    print(f"Простые числа до {limit}:")
    print(primes)


if __name__ == "__main__":
    main()
    input("Нажмите Enter для выхода...")