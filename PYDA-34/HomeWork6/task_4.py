DEFAULT_USER_COUNT = 3


def delete_and_return_last_user(region, default_list=['A100', 'A101', 'A102']):
    """
    Удаляет из списка default_list последнего пользователя
    и возвращает ID нового последнего пользователя.
    """
    element_to_delete = default_list[-1]
    default_list.remove(element_to_delete)
    print(default_list)
    return default_list[DEFAULT_USER_COUNT - 2]


delete_and_return_last_user(1)

delete_and_return_last_user(1)

# IndexError: list index out of range ошибка при попытке получить элемент списка,
# которого нет (выход за пределы длинны списка)
# в строке с return пытается во-второй раз получить элемент с индексом 1, которого нет,
# т.к. после первого выполнения осталось ['A100', 'A101'] и после удаления ['A100'], т.е. длина списка - 1 элемент
# максимальный индекс [0]