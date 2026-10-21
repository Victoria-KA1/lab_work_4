def generate_filtered_lines(filename, keyword):
    """Генератор строк из файла, содержащих ключевое слово."""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if keyword.lower() in line.lower():
                yield line


def create_sample_file():
    """Создаёт тестовый файл, если его нет."""
    lines = [
        "Python — это язык программирования.",
        "Git помогает управлять версиями.",
        "Java тоже язык, но другой.",
        "Python удобен для анализа данных.",
        "Декораторы — мощный инструмент Python.",
    ]
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


def main():
    create_sample_file()

    keyword = input("Введите ключевое слово для поиска: ")
    print(f"Строки, содержащие '{keyword}':")
    for line in generate_filtered_lines("sample.txt", keyword):
        print(f"  → {line}")


if __name__ == "__main__":
    main()
    input("Нажмите Enter для выхода...")