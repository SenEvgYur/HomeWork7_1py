def correction_city(text):       # корректировка Города
    global contacts
    persons = []
    for i in contacts:
        if text in i:
            persons.append(i)
            print('\nНапишите новый город:\n')
            i = input()
    for person in persons:
        contacts[person]['Город'] = i