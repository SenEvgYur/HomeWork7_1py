def post_all():         # печать ФИО и Должности всего справочника
    global contacts
    persons = []
    for i in contacts:
        persons.append(i)
    for person in persons:
        print('\nФИО: ', person, '     Должность: ',
              contacts[person]['Должность'])