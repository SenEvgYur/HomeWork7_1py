def correction_phone(text):       # корректировка телефона
    global contacts
    persons = []
    for i in contacts:
        if text in i:
            persons.append(i)
            i = input()
    for person in persons:
        contacts[person]['Телефон'] = i