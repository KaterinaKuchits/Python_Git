# (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать путь к обоим исходным файлам и путь к выходному
# файлу со словарём. Проверить работу скрипта для случая,
# когда все файлы находятся в разных папках.

import sys

users, hobby, combined = sys.argv[1:]
if __name__ == '__main__':
    from itertools import zip_longest
    with open('users.csv', 'r', encoding="utf-8") as name, \
            open('hobby.csv', 'r', encoding="utf-8") as hobby:
        names = name.read().splitlines()
        hobbys = hobby.read().splitlines()

    users_hobbys_gen =((names, hobbys) for names, hobbys in zip_longest(names, hobbys, fillvalue=None))

    with open(combined, 'w') as f:
        for user_hobby in users_hobbys_gen:
            f.write(f'{user_hobby[0]}: {user_hobby[1]}\n')
    exit()