# Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное
# число». Реализовать перегрузку методов сложения и умножения комплексных чисел.
# Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
# выполнить сложение и умножение созданных экземпляров. Проверить корректность
# полученного результата.

class ComplexNumbers1:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'{self.r}'

    def __add__(self, other):
        return self.r + other.r

    def __mul__(self, other):
        return self.r * other.r


com_digit_1 = ComplexNumbers1(complex(1, 2))
com_digit_2 = ComplexNumbers1(complex(3, 4))

print('Даны два комплексных числа: ', com_digit_1, com_digit_2)
print('сложение ', end='')
print(com_digit_1 + com_digit_2)
print('умножение ', end='')
print(com_digit_1 * com_digit_2)
print()