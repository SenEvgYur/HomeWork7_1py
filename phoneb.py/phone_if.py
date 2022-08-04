def phone_if(text):       # печать ФИО и телефона по указанным буквам
    persons = []
    for i in contacts:
        if text in i:
            persons.append(i)
    for person in persons:
        print('\nФИО: ', person, '       Номер телефона: ',
              contacts[person]['Телефон'])