                       #Задание 1
# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# a. до минуты: <s> сек;
# b. до часа: <m> мин <s> сек;
# c. до суток: <h> час <m> мин <s> сек;
# d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

one_minute = 60
one_hour = 3600
one_day = 86400
one_week = 604800

duration = int(input('Продолжительность времени в секундах: '))
if duration < one_minute:
    print('{} сек'.format(duration))
elif one_minute <= duration and one_hour > duration:
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} мин {} сек'.format(my_minute, my_second))
elif duration >= one_hour and duration < one_day:
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} час {} мин {} сек'.format(my_hour, my_minute, my_second))
elif duration >= one_day and duration < one_week:
    my_day = duration // one_day
    duration = duration % one_day
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} дн {} час {} мин {} сек'.format(my_day, my_hour, my_minute, my_second))


