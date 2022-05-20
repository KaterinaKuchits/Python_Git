# *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Только теперь не нужно создавать словарь с данными.
# Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt).
# Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

from itertools import  zip_longest

with open('users.csv', 'r', encoding="utf-8") as name, \
    open('hobby.csv', 'r', encoding="utf-8") as hobby:
    names = name.read().splitlines()
    hobbys = hobby.read().splitlines()

users_hobbys_gen = ((names, hobbys) for names, hobbys in zip_longest(names, hobbys, fillvalue=None))

with open('users_hobby.txt', 'w') as f:
    for user_hobby in users_hobbys_gen:
        f.write(f'{user_hobby[0]}: {user_hobby[1]}\n')
