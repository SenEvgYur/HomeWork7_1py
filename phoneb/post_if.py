def post_if(text):         # печать ФИО и Должности по указанным буквам
    global contacts
    persons = []
    for i in contacts:
        if text in i:
            persons.append(i)
    for person in persons:
        print('\nФИО: ', person, '     Должность: ',
              contacts[person]['Должность'])