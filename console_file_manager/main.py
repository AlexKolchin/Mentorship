import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, game, change_dir, current_dir

save_info('Start')
try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду. help')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Нужно ввести имя файла и название копии')
        else:
            copy_file(name, new_name)
    elif command == 'change_dir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название директории')
        else:
            change_dir(name)
    elif command == 'pwd':
        current_dir()
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
        print('change_dir - изменение директории')
        print('pwd - текущая директория')
        print('game - игра угадай число')
    elif command == 'game':
        game()
    save_info('End')
