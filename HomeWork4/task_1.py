documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


# Common

def enter_commands():
    """
    Ввод команд
    :return:
    """
    return input("Введите команду: ")


def find_shelve_by_doc_number(doc_num):
    """
    Поиск на полках
    :param doc_num:
    :return:
    """
    result = False
    for shelve, docs in directories.items():
        if doc_num in docs:
            result = shelve
    return result

def delete_doc_in_shelve(doc_num):
    """
    Поиск на полках
    :param doc_num:
    :return:
    """
    for shelve, docs in directories.items():
        if doc_num in docs:
            directories[shelve] = list(filter(lambda x: x != doc_num, docs))

def find_documents_by_key(**param):
    search_val = param['search']
    search_key = param['key']
    return next((index for (index, d) in enumerate(documents) if d[search_key] == search_val), False)


check_shelve = lambda new_shelve: True if new_shelve not in directories.keys() else False


def print_text_shelves(text):
    print(f"{text}Текущий перечень полок: {', '.join(list(directories.keys()))} ")


def enter_values():
    values = {}
    structure = [
        ("type", "Введите тип документа: "),
        ("number", "Введите номер документа: "),
        ("name", "Введите владельца документа: "),
    ]
    for enter_val in structure:
        values[enter_val[0]] = input(enter_val[1])
    shelve = input('Введите полку для хранения: ')
    return {'value': values, 'shelve': shelve}


# Command func()

def command_i():
    for item in documents:
        doc_num = item['number']
        shelve = find_shelve_by_doc_number(doc_num)
        print(f"тип: {item['type']}, владелец: {item['name']}, полка хранения: {shelve}, №: {doc_num}")


def command_s():
    search_doc = input('Введите номер документа: ')
    result = find_shelve_by_doc_number(search_doc)

    if result:
        print("Документ хранится на полке:", result)
    else:
        print("Документ не найден в базе")


def command_p():
    search_doc = input('Введите номер документа: ')
    result = find_documents_by_key(key='number', search=search_doc)
    if result:
        print(documents[result]['name'])
    else:
        print("Документ не найден в базе")


def command_ads():
    new_shelve = input("Введите номер полки: ")
    if check_shelve(new_shelve):
        directories[new_shelve] = []
        print_text_shelves("Полка добавлена.")
    else:
        print_text_shelves("Такая полка уже существует.")


def command_ds():
    shelve = input("Введите номер полки: ")
    if shelve in directories.keys() and len(directories[shelve]) == 0:
        del directories[shelve]
        print_text_shelves("Полка удалена.")
    else:
        print_text_shelves("На полке есть документа, удалите их перед удалением полки.")


def command_ad():
    result = enter_values()
    shelve = result['shelve']
    new_doc = result['value']

    if check_shelve(shelve):
        print("Такой полки не существует. Добавьте полку командой as. Текущий список документов:")
        command_i()
    else:
        documents.append(new_doc)
        directories[shelve].append(new_doc['number'])
        print('Документ добавлен. Текущий список документов:')
        command_i()


def command_d():
    search_doc = input('Введите номер документа: ')
    result = find_documents_by_key(key='number', search=search_doc)

    if result:
        del_doc_number = documents[result]['number']
        delete_doc_in_shelve(del_doc_number)
        del documents[result]
        command_i()
        print(directories, documents)
    else:
        print("Документ не найден в базе")
        command_i()

def command_m():
    doc_number = input("Введите номер документа:")
    result = find_documents_by_key(key='number', search=doc_number)
    shelve_number = input("Введите номер полки:")
    if check_shelve(shelve_number):
        print_text_shelves("Такой полки не существует.")
    elif result:
        delete_doc_in_shelve(doc_number)
        directories[shelve_number].append(doc_number)
        print("Документ перемещен. Текущий список документов:")
        command_i()
    else:
        print("Документ не найден в базе. Текущий список документов:")
        command_i()

def main():
    command = enter_commands()
    while command != 'q':
        if command == 'p':
            command_p()
        elif command == 's':
            command_s()
        elif command == 'i':
            command_i()
        elif command == 'ads':
            command_ads()
        elif command == 'ds':
            command_ds()
        elif command == 'ad':
            command_ad()
        elif command == 'd':
            command_d()
        elif command == 'm':
            command_m()
        else:
            print("Неизвестная команда, введите еще раз")
        command = enter_commands()


main()
