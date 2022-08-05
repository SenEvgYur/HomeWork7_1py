def user_id_if(text):   # печать ФИО по указанным буквам
    global contacts
    for i in contacts:
        if text in i:
            print('\nФИО: ', i)