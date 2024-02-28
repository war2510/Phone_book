from logger import input_data, print_data


def interface():
    print("Добрый день! Вы работаете со справочником телефонов. Выберите необходимое действие: \n"
          " 1 - добавить абонента в справочник \n"
          " 2 - отобазить весь справочник \n"
          " 3 - удалить абонента из справочника \n"
          " 4 - изменить данные по абоненту \n"
          " 5 - найти абонента по любому параметру \n"
          " 6 - сохранить файл в текстовом фомате \n"
          " 7 - копирование данных из одного справочника в другой \n"
          " 8 - закончить работу")
    command = int(input('Введите число '))

    while command not in range(1,9):
        print('Неправильный ввод')
        command = int(input('Введите число '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        del_data()
    elif command == 4:
        chenge_data()
    elif command == 5:
        search_data()
    elif command == 6:
        txt_data()
    elif command == 7:
        copy_data()
    elif command == 8:
        exit()