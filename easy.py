import os
import sys

# Ex. 1

if __name__ == '__main__':
    cur_dir = os.getcwd()
    count = 1
    while count < 10:
        try:
            os.mkdir(os.path.join(cur_dir, f'dir{count}'))
        except FileExistsError:
            print('Такая директория уже существует!')
        count += 1

    for i in range(1,10):
        path_dir = os.path.join(cur_dir,f'dir{i}')
        try:
            os.rmdir(path_dir)
        except FileNotFoundError:
            print('Такой директории не существует!')

# Ex.2
    for file in os.listdir(cur_dir):
        if not os.path.isfile(os.path.join(cur_dir,file)):
            print(file)

# Ex.3
    filename = sys.argv[0]
    # Windows
    if os.name == 'nt':
        os.system(f'copy {filename} copy_{filename}')
    else:
    # Unix - OS
        os.system(f'cp {filename} copy_{filename}')

# Functions
def move(cur_dir,new_path):
    go_path = os.path.join(cur_dir,new_path)
    if os.path.exists(go_path) and os.path.isdir(go_path):
        print('Вы успешно перешли в папку!')
        return go_path
    else:
        print('Не удалось перейти в папку!')
        return cur_dir

def view_dir(cur_dir):
    print('Содержимое папки:\n')
    for file in os.listdir(cur_dir):
        if os.path.isfile(file):
            print(f'[File]: {file}')
        else:
            print(f'[Dir]: {file}')

def create_dir(cur_dir,new_dir):
    new_dir = os.path.join(cur_dir,new_dir)
    if os.path.exists(new_dir):
        print('Данная папка уже существует!')
    else:
        print(f'Папка {new_dir} создана!')
        os.mkdir(new_dir)

def del_dir(cur_dir, name_del_dir):
    path_dir = os.path.join(cur_dir, name_del_dir)
    if os.path.exists(path_dir):
        print(f'Папка {name_del_dir} успешно удалена!')
        os.rmdir(path_dir)
    else:
        print('Данной папки не существует!')
