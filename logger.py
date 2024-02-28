from data_create import name_data, surname_data, phone_data, adress_data
import pandas as pd
import csv


def input_data():            # Добавление данных в телефонные справочники
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком формате записать данные? \n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{adress}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{adress}\n"
    f"Выберете вариант: "))

    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:       # Добавление новых данных в 1 файл
            f.writelines(f"\n\n{name}\n{surname}\n{phone}\n{adress}")
    elif var == 2:
        with open('data_second_variant.csv', 'a', newline='\n', encoding='utf-8') as f:      # Добавление новых данных во 2 файл
            csv_writer = csv.writer(f, delimiter=';')
            csv_writer.writerow([name, surname, phone, adress])


def print_data():          # Отображение всех справочников
    print('Вывожу данные из 1 файла: \n', end='-------- \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.read()  # Читаем весь файл в одну строку
        data_first_people = data_first.split('\n\n') # Разделяем строку на отдельные значения по двойному пробелу
        for i in data_first_people:
            print(i)
            print('--------')            

    print('Вывожу данные из 2 файла: \n')
    data_second = pd.read_csv('data_second_variant.csv', delimiter=';', encoding='utf-8', header=None)
    data_second.columns = ['Имя', 'Фамилия', 'Телефон', 'Адрес']  # Задаем имена столбцов

    # Форматирование для выравнивания данных и заголовков по левому краю
    column_width = 20
    formatters = {column: lambda x: str(x).ljust(column_width) for column in data_second.columns}
    headers = {column: column.ljust(column_width) for column in data_second.columns}

    # Выводим заголовки таблицы с пунктирной линией между столбцами
    header_row = '|'.join(headers.values())
    print(header_row)
    print('-' * len(header_row))  # Печатаем границу под заголовками

    # Выводим данные в виде таблицы с выравниванием по левому краю и пунктирной линией между столбцами
    for index, row in data_second.iterrows():
        print('|'.join([str(x).ljust(column_width) for x in row.values]))
        print('-' * len(header_row))  # Печатаем пунктирную границу между строками


def del_data():           # Удаление данных из телефонных справочников (пользуемся срезами)
    var = int(input("Введите, из какого файла надо удалить запись: \n"))

    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input('Введите корректный номер файла '))

    num = int(input("Введите номер строки, с которой надо удалить запись: \n"))

    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            data_del = data_first[:num-1] + data_first[num+4:]   # Удаляем от начала записи по человеку до конца, включая последний пробел (удаляем запись между пробелами начиная от указанной строки)
            with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
                f.writelines(data_del)                      # Перезаписываем файл без удаленной записи
            print('Запись удалена')
           
    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            num -= 1                                
            data_del = data_second[:num] + data_second[num+1:]    # Удаляем указанную строку
            with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
                f.writelines(data_del)                           # Перезаписываем файл без удаленной записи
            print('Запись удалена')


def chenge_data():       # Изменение данных в телефонных справочниках
    print('Введите новые данные для абонента')
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()

    var = int(input("Введите номер файла, в который надо внести изменения: \n"))

    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input('Введите корректный номер файла '))

    num = int(input("Введите номер записи, которую необходимо изменить: \n"))

    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            if 1 <= num <= len(data_first):
                data_first[num-1:num+3] = f"{name}\n{surname}\n{phone}\n{adress}\n"     # Меняем определенные строки, пользуясь срезами
                with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
                    f.writelines(data_first)                                       # Перезаписываем файл с учетом изменений
                print('Запись изменена')
            else:
                print('Некорректный номер записи')
           
    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            if 1 <= num <= len(data_second):
               data_second[num-1] = f"{name};{surname};{phone};{adress}\n"            # Меняем определенные строки, пользуясь срезами
               with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
                    f.writelines(data_second)                                          # Перезаписываем файл с учетом изменений
            print('Запись изменена')


def search_data():    # Поиск в стправочнике
    temp = input("Введите параметры для поиска: \n")

    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        # Ищем все слова с заданным параметром в строке
        data_first = f.read()  # Читаем весь файл в одну строку
        data_first_people = data_first.split('\n\n') # Разделяем строку на отдельные значения по двойному пробелу
        Flag1 = False               # Флаг, чтобы один раз выводить запись о найденных значениях
        for i in data_first_people:
            if temp in i:              # Если искомые параметры есть в данных по абоненту
                if Flag1 == False:
                    print('В первом справочнике найдены следующие записи: \n', end='-------- \n')
                print(i)
                print('--------')
                Flag1 = True

    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            Flag2 = False              # Флаг, чтобы один раз выводить запись о найденных значениях
            for i in f:
                if temp in i:          # Если искомые параметры есть в данных по абоненту
                    if Flag2 == False:
                        print('Во втором справочнике найдены следующие записи:')
                    print(i, end='') 
                    Flag2 = True

    if Flag1 == False and Flag2 == False:
        print('По данному параметру значения не найдены') 


def txt_data():       # Сохранение файлов в txt формате
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f_csv:
        data_first = f_csv.readlines()
        with open('data_first_variant.txt', 'w', encoding='utf-8') as f_txt:
            for i in data_first:
                f_txt.write(i)

    with open('data_second_variant.csv', 'r', encoding='utf-8') as f_csv:
        data_second = f_csv.readlines()
        with open('data_second_variant.txt', 'w', encoding='utf-8') as f_txt:
            for i in data_second:
                f_txt.write(i)
    
    print('Данные сохранены')


def copy_data():     # Копирование из одного файла в другой
    var = int(input('Введите номер файла, из которого нужно скопировать данные: \n'))
    
    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input('Введите корректный номер файла '))

    num = int(input("Введите номер записи, которую необходимо скопировать: \n"))

    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.read().split('\n\n')      # Чтение в одну строку и разделяем по пробелу
            if 1 <= num <= len(data_first):  # Проверяем, что номер записи в допустимом диапазоне
                data_first_only = data_first[num-1].replace('\n', ';')  # Заменяем перенос слов на разделитель ;
                with open('data_second_variant.csv', 'a', encoding='utf-8') as f1:
                    f1.write(data_first_only + '\n')
                print('Запись скопирована из 1 варианта файла во 2 вариант')
            else:
                print('Такого номера записи не существует')


    if var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            if 1 <= num <= len(data_second):  # Проверяем, что номер записи в допустимом диапазоне
                data_second_only = data_second[num-1].strip().split(';')  # Отделаяем слова по символу ;
                with open('data_first_variant.csv', 'a', encoding='utf-8') as f1:
                    k = 0
                    for j in data_second_only:
                        if k == 0:
                            f1.write(f'\n\n{j}')
                            k += 1
                        else:
                            f1.write(f'\n{j}')
                print('Запись скопирована из 2 варианта файла в 1 вариант')
            else:
                print('Такого номера записи не существует')