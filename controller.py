from data import contacts
import phoneb 
from phoneb import user_id
from phoneb import user_id_if
from phoneb import phone_all
from phoneb import phone_if
from phoneb import birthday_all
from phoneb import birthday_if
from phoneb import correction_birthday
from phoneb import correction_id
from phoneb import correction_phone
from phoneb import add_id
from phoneb import end_menu
from phoneb import post_all
from phoneb import post_if
from phoneb import correction_post
from phoneb import city_all
from phoneb import city_if
from phoneb import correction_city


def main_screen():    # запуск программы с выбором 
    print(
        '\nВыберите интересующий пункт меню: \n'
        '1. Проcмотр информации\n'
        '2. Исправление информации\n'
        '3. Запись новой информации'
    )
    x = int(input())
    while x < 1 or x > 3:
        x = int(input())
    if x == 1:
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
                '2. дни рождения\n'
                '3. должность\n'
                '4. город\n'
                )
            x = int(input())
            while x < 1 or x > 4:
                x = int(input())
            if x == 1: 
                phone_all()
            elif x == 2:
                birthday_all()
            elif x == 3:
                post_all()
            else:
                city_all
        if x == 2:
            print('\nВведите буквы контакта, который ищите: ')
            my_text = input()
            user_id_if(my_text)
            print(
                '\nЕсли хотите увидеть записанную информацию \n'
                '1. телефоны \n'
                '2. дни рождения\n'
                '3. должность\n'
                '4. город\n'
            )
            x = int(input())
            while x < 1 or x > 2:
                x = int(input())
            if x == 1: 
                phone_if(my_text)
            elif x == 2:
                birthday_if(my_text)
            elif x == 3:
                post_if(my_text)
            else:
                city_if(my_text) 
    if x == 2:
        print('\nВведите буквы контакта, который ищите: ')
        my_text = input()
        user_id_if(my_text)
        print(
            '\nВыберите, что хотите исправить:\n'
            '1. ФИО\n'
            '2. телефон\n'
            '3. день рождения\n'
            '4. должность\n'
            '5. город\n'
            '6. всю информацию'
            )
        x = int(input())
        while x < 1 or x > 6:
            x = int(input())
        if x == 1:
            correction_id(my_text)
        elif x == 2:
            correction_phone(my_text)
        elif x == 3:
            correction_birthday(my_text)
        elif x == 4:
            correction_post(my_text)
        elif x == 5:
            correction_city(my_text)
        else:
            correction_id(my_text)
            correction_phone(my_text)
            correction_birthday(my_text)
            correction_post(my_text)
            correction_city(my_text)
    if x == 3:
        add_id()   
    end_menu()
    print()
