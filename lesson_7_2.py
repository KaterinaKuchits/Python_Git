# 2. *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей
# структурой:
# |--my_project
# |--settings
# | |--__init__.py
# | |--dev.py
# | |--prod.py
# |--mainapp
# | |--__init__.py
# | |--models.py
# | |--views.py
# | |--templates
# | |--mainapp
# | |--base.html
# | |--index.html
# |--authapp
# | |--__init__.py
# | |--models.py
# | |--views.py
# | |--templates
# © geekbrains.ru 27
# | |--authapp
# | |--base.html
# | |--index.html


import os

settings = {}
with open('config.yaml') as f:
    lines = dict(map(str.split, f.readlines()))

basedir = lines.pop('base')
for k, v in lines.items():
    os.makedirs(os.path.join(os.curdir, basedir, k), exist_ok=True)
    print(f'Создан каталог: {k}')
    for i in v.split(','):
        with open(os.path.join(os.curdir, basedir, k, i), 'w') as f:
            print(f'Создан файл: {i} в каталоге {k}')