import re


def find_people_by_phone_code(data: list[str], phone_code: str) -> list[list[str]]:

    """
       Ищет людей по указанному коду города в номере телефона.

       :param data: Список строк с данными.
       :param phone_code: Код города для поиска.
       :return: Список анкет людей, чей номер телефона начинается с указанного кода.
       """
    people = []
    people_tmp = []

    phone_pattern = rf"\+7 {phone_code} \d{{3}}-\d{{2}}-\d{{2}}"

    for line in data:
        line = line.strip()
        people_tmp.append(line)
        if len(people_tmp) == 8:

            phone = people_tmp[5]
            if re.search(phone_pattern, phone):
                people.append(people_tmp)
            people_tmp = []
    if len(people_tmp) == 7:
        people.append(people_tmp)
        people_tmp = []
    return people
