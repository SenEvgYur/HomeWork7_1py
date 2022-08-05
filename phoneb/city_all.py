def city_all():         # печать ФИО и Города всего справочника
    global contacts
    persons = []
    for i in contacts:
        persons.append(i)
    for person in persons:
        print('\nФИО: ', person, '     Город: ',
              contacts[person]['Город'])