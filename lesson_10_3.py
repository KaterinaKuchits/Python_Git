# Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо
# создать класс «Клетка». В его конструкторе инициализировать параметр, соответствующий
# количеству ячеек клетки (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться
# только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого
# числа деления клеток соответственно.



class Cell:
    def __init__(self, wol):
        self.wol = wol

    def __add__(self, other):
        return Cell(self.wol + other.wol)

    def __sub__(self, other):
        return Cell(self.wol - other.wol) if self.wol - other.wol >= 0 \
            else f'Операция не допустима, Разность меньше нуля'

    def __mul__(self, other):
        return Cell(self.wol * other.wol)

    def __floordiv__(self, other):
        return Cell(self.wol // other.wol)

    def __truediv__(self, other):
        return Cell(self.wol // other.wol)

    def make_order(self, n):
        for _ in range(self.wol // n):
            print('*' * n)
        print('*' * (self.wol % n))

a = Cell(12)
b = Cell(13)
c = Cell(5)

print((a + b).wol)
print((a - b))
print((a - c).wol)
print((a * b).wol, type(a * b))
print((a / c).wol, type(a / c))
print((a // c).wol, type(a / c))

a.make_order(5)
