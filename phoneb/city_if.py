def city_if(text):         # печать ФИО и Города по указанным буквам
    global contacts
    persons = []
    for i in contacts:
        if text in i:
            persons.append(i)
    for person in persons:
        print('\nФИО: ', person, '     Город: ',
              contacts[person]['Город'])