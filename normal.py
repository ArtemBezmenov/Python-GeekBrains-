import os
from easy import move, create_dir, del_dir, view_dir

cur_dir = os.getcwd()

while True:
    choice = int(input('Выберите пункт:\n'
                                   '1. Перейти в папку\n'
                                   '2. Просмотреть содержимое папки\n'
                                   '3. Создать папку\n'
                                   '4. Удалить папку\n'
                                   '5. Выход\n'
                                   '---------------------\n'
                                   'Ваш выбор:'))
    if choice == 1:
        new_path = input('Введите название папки: ')
        move(cur_dir,new_path)

    if choice == 2:
        view_dir(cur_dir)

    if choice == 3:
        new_dir = input('Введите название для новой папки: ')
        create_dir(cur_dir,new_dir)

    if choice == 4:
        dir_name = input('Введите название папки для удаления: ')
        del_dir(cur_dir,dir_name)

    if choice == 5:
        break

