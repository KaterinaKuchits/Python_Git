# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные
# (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.


class Matrix:
    def __init__(self, list_of_lists):
        self.mat = list_of_lists

    def __str__(self):
        string = ''
        for i in self.mat:
            for j in i:
                string = string + '%s\t' % (j)
            string = string[:-1]
            string = string + '\n'
        string = string[:-1]
        return string

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                summa = other.mat[i][j] + self.mat[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.mat[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


a = [[1, 2, 0], [7, 3, 0], [5, 6, 0]]
b = [[3, 5, 2], [2, 4, 6], [1, 4, 8]]
m = Matrix(a)
mm = Matrix(b)

print(m.__str__(), "\n")
print(mm.__str__(), "\n")
print(m + mm)