from controller import main_screen


def end_menu():
    print(
        '\nХотите ли продолжить ?\n'
        '1. Да\n'
        '2. Нет\n'
    )
    x = int(input())
    if x == 1:
        main_screen()
    else:
        print('\nДо новых встреч !')