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


def myfc():
    while True:
        com = input('Введите команду: ')
        if com == 'q': break
        if com == 'p': com_people()
        if com == 's': com_shelf()
        if com == 'l':
            com_list()
        else:
            print('Неверная команда')
    return None


def com_people():
    num1 = input('Введите номер документа: ')
    for document in documents:
        if num1 == document['number']:
            print(document['name'])
            myfc()
    print('Нет такого документа')
    myfc()


def com_shelf():
    num2 = input('Введите номер документа: ')
    for an in directories.items():
        for an1 in an[1]:
            if num2 == an1:
                print(f'Полка номер: {an[0]}')
                myfc()
    print('Нет такого документа')
    myfc()


def com_list():
    for docs in documents:
        print(type(docs))
        myfc


myfc()