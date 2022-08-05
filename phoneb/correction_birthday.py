def correction_birthday(text):       # корректировка дня рождения
    global contacts
    persons = []
    for i in contacts:
        if text in i:
            persons.append(i)
            print('\nНапишите новую дату рождения:\n')
            i = input()
    for person in persons:
        contacts[person]['Дата рождения'] = i