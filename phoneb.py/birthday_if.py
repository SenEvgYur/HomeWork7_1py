def birthday_if(text):         # печать ФИО и Даты рождения по указанным буквам
    persons = []
    for i in contacts:
        if text in i:
            persons.append(i)
    for person in persons:
        print('\nФИО: ', person, '     День рождения: ',
              contacts[person]['Дата рождения'])