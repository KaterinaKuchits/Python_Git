# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.color} {self.name} повернула на{self.direction}')

    def show_speed(self):
        print(f'Скорость: {self.speed}')

    def check_police(self):
        print(f'Полицейская: {self.is_police}')

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'Скорость: {self.speed}') if self.speed <= 60 else print('Привышена допустимая скорость')

    def check_police(self):
        print(self.is_police)

class SportCar(TownCar):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'Скорость: {self.speed}') if self.speed <= 40 else print('Привышена допустимая скорость')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

    def check_police(self):
        print(f'Полицейская: {self.is_police}')

c, t, s, w, p = Car(40, 'Белая', 'Audi'), TownCar(70, 'Черная', 'BMW'), SportCar(40, 'Красная', 'Ferrari'),\
    WorkCar(40, 'Синяя', 'Lada'), PoliceCar(40, 'Серая', 'Mazda')

t.go(), t.turn('право'), t.stop()
t.show_speed(), t.check_police()
print(f'Марка: {c.name}, Цвет: {c.color}, Скорость: {c.speed}, Полицейская: {c.is_police} \n')