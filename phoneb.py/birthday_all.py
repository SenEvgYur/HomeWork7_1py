def birthday_all():         # печать ФИО и Даты рождения всего справочника
    persons = []
    for i in contacts:
        persons.append(i)
    for person in persons:
        print('\nФИО: ', person, '     День рождения: ',
              contacts[person]['Дата рождения'])