def add_id():
    global contacts
    my_str = input('\nВведите ФИО\n')
    contacts[my_str] = {}
    contacts[my_str]['Телефон'] = input('\nВведите телефон\n')
    contacts[my_str]['Дата рождения'] = input('\nВведите дату рождения\n')
    contacts[my_str]['Должность'] = input('\nВведите должность\n')
    contacts[my_str]['Город'] = input('\nВведите дату рождения\n')