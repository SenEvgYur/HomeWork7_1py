def phone_all():       # печать ФИО и телефонов всего справочника
    global contacts
    persons = []
    for i in contacts:
        persons.append(i)
    for person in persons:
        print('\nФИО: ', person, '       Номер телефона: ',
              contacts[person]['Телефон'])