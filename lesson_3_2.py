#  (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
#  реализовать корректную работу с числительными,
#  начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
#  Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate(num):
    if num.islower():
        return print(dictionary.get(num))
    else:
        return print(dictionary.get(num.lower()).title())

dictionary = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

num_translate(input('Введите число от 0 до 10 на английском языке: '))
