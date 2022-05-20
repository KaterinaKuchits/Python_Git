import sys

with open('sales.txt', 'r+', encoding='utf-8') as f:
    values = (value for value in f.readlines())
    count_strings = int(sys.argv[1])
    cursor_place = 0
    for value in values:
        if count_strings == 1:
            f.seek(cursor_place)
            f.writelines(sys.argv[2])
            break
        else:
            cursor_place += len(value)
            count_strings -= 1
            continue
    if count_strings >1:
        print('Такой строчки не существует')
