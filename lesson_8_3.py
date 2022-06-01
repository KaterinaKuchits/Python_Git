# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
# ...
# @type_logger
# def calc_cube(x):
# return x ** 3
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
# ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
# аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
# функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)



def ex_decorator(func):
    def wrapper(*args, **kwargs):
        for i in args:
            print(f'{str(func).split()[1]}({i}: {type(i)})')
        for i in kwargs:
            print(f'{str(func).split()[1]}([ARG: {i}] = {kwargs[i]}: {type(kwargs[i])})')
        return func(*args, **kwargs)
    return wrapper

@ex_decorator
def function_with_arguments(a, b, c, d):
    try:
        b = int(b)
        b = b ** 3
    except:
        b = 0
    return b

print(f'Результат функции, обернутой декоратором: {function_with_arguments(a="TEXT", b=3, c=333, d={1: "2"})}')