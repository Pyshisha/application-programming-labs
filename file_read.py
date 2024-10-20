def read_file(filename: str) -> list[str]:
    """
        Читает файл и возвращает содержимое в виде списка строк.

        :param filename: Имя файла.
        :return: Список строк из файла.
        """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()
