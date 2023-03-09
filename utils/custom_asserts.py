"""Модуль содержит методы кастомных assert"""
def compare_dict(dict1: dict, dict2: dict, exlude_list: list, msg: str):
    """
    Функция для кастомного assert
    dict1 - первый словарь
    dict2 - второй словарь
    exlude_list - список ключей, которые не будут сравниваться
    """
    for keys in dict1:
        if keys not in exlude_list:
            assert dict1[keys] == dict2[keys], msg
