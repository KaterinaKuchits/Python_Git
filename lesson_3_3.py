#  Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
#  в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся
#  с соответствующей буквы.
#  Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
#  Можно ли использовать словарь в этом случае?

def thesaurus(*args):
    names_dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter in names_dict:
            names_dict[letter] += [i]
        else:
            names_dict[letter] = [i]
    return names_dict

print(thesaurus("Иван", "Мария", "Пётр", "Илья", "Никита", "Николай", "Арина", "Катя", "Алиса"))