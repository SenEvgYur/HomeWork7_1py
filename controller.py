import data
import phoneb




def main_screen():    # запуск программы с выбором 
    print(
        '\nВыберите интересующий пункт меню: \n'
        '3. Проcмотр информации'
    )
    x = int(input())
    while x < 1 or x > 3:
        x = int(input())
    if x == 3:
        print(
        '\nВыберите интересующий пункт меню: \n'
        '1. Проcмотр всеx контактов \n'
        '2. Поиск контакта'
        )
        x = int(input())
        while x < 1 or x > 2:
            x = int(input())
        if x == 1:
            user_id()
            print(
                '\nЕсли хотите увидеть записанную информацию \n'
                '1. телефоны \n'
                '2. дни рождения'
                )
            x = int(input())
            while x < 1 or x > 2:
                x = int(input())
            if x == 1: 
                phone_all()
            else:
                birthday_all()
        if x == 2:
            print('\nВведите буквы контакта, который ищите: ')
            my_text = input()
            user_id_if(my_text)
            print(
                '\nЕсли хотите увидеть записанную информацию \n'
                '1. телефоны \n'
                '2. дни рождения'
            )
            x = int(input())
            while x < 1 or x > 2:
                x = int(input())
            if x == 1: 
                phone_if(my_text)
            else: 
                birthday_if(my_text)
    print()

main_screen()
