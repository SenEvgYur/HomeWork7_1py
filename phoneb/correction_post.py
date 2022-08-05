def correction_post(text):       # корректировка Должности
    global contacts
    persons = []
    for i in contacts:
        if text in i:
            persons.append(i)
            print('\nНапишите новую должность:\n')
            i = input()
    for person in persons:
        contacts[person]['Должность'] = i