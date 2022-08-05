def correction_id(my_text):  # корректировка ФИО
    global contacts
    for i in contacts:
        if my_text in i:
            i = input()