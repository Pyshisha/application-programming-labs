import argparse
from file_read import read_file
from people_with_927 import find_people_by_phone_code


def main() -> None:
    """
        Главная функция программы. Обрабатывает аргументы командной строки и выводит результаты.
    """
    parser = argparse.ArgumentParser(description="Найти людей с кодом города 927.")
    parser.add_argument("filename", type=str, help="Имя файла с анкетами")
    args = parser.parse_args()

    try:
        data = read_file(args.filename)
        people_with_code_927 = find_people_by_phone_code(data, "927")

        if people_with_code_927:
            print("Найденные анкеты с кодом города 927:")
            for person in people_with_code_927:
                print('\n'.join(person))
        else:
            print("Люди с кодом города 927 не найдены.")

    except FileNotFoundError:
        print("Ошибка: файл не найден.")
    except PermissionError:
        print("Не хватает прав доступа")


if __name__ == "__main__":
    main()

