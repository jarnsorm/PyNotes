import random
def game():
    my_num = random.randint(1, 10)
    print('Я загадал число. Угдай его')
    while my_num:
        number = int(input('Введи число: '))
        if number > my_num:
            print('Твое число больше загаданного')
        elif number < my_num:
            print('Твое число меньше загаданного')
        else:
            print('Молодец! Ты угадал число!')
            break

game()