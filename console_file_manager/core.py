import os
import shutil
import datetime
import sys
import random


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже существует')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Folder exists')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def game():
    # компьютер загадывает случайное число от 1 до 100
    import random
    number = random.randint(1, 100)
    # print(number)
    print('Вас приветствует игра - "Угадай число!"')
    print('Компьютер загадывает число, которое Вам нужно угадать')
    user_number = None
    user_count = int(input('Введите количество игроков: '))
    users = []
    k = 1
    for i in range(user_count):
        user_name = input(f'Введите имя игрока {k}: ')
        users.append(user_name)
        k += 1
    count = 0
    levels = {1: 10, 2: 5, 3: 3}
    level = int(input('Выберите уровень сложности: 1 - 10 попыток, 2 - 5 попыток, 3 - 3 попытки: '))
    max_count = levels[level]

    is_winner = False
    winner_name = None

    while not is_winner:
        count += 1
        if count > max_count:
            print('Все игроки проиграли, исчерпав все попытки =(')
            break
        print(f'Попытка № {count}')
        for user in users:
            print(f'Ход игрока {user}: ')
            user_number = int(input('Введите число от 1 до 100: '))
            if user_number == number:
                is_winner = True
                winner_name = user
                break
            elif number < user_number:
                print('Вы не угадали, попробуйте меньше:')
            else:
                print('Вы не угадали, попробуйте больше')
    else:
        print(f'Поздравляем, {winner_name}! Вы выиграли! =)')


def current_dir():
    return os.getcwd()

def change_dir(name):
        if (os.path.exists(name)):
            if (os.path.isdir(name)):
                os.chdir(name)
                print('New place is: \n', current_dir())
            else:
                print('Incorrect')
        else:
            print('Incorrect')
