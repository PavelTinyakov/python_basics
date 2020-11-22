# Pavel Tinyakov

from random import randrange
from time import sleep


class Car:
    def __init__(self, model, color, speed, is_police=False):
        self.model = model
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(
            (f'ТС: модель {self.model}, цвет {self.color}',
             f'Полицейское авто, модель {self.model}')[is_police is True])

    def go(self):
        try:
            self.speed = randrange(1, self.speed)
        except ValueError:
            self.speed = randrange(1, 100)
        i = 0
        while i != self.speed:
            sleep(0.1)
            i += 1
            print('\r', end='')
            print(f'Поехали! Набираем скорость: {i} км/ч', end='')
        print()

    def turn(self, direction):
        print(('Зачем ты поворачиваешь стоя на месте?', f'Поварачиваем на{direction}...')[self.speed > 0])
        sleep(3)

    def stop(self):
        i = self.speed
        while i != 0:
            sleep(0.05)
            i -= 1
            print("\r", end='')
            print(f'Пора останавливаться! Снижаем скорость: {i} км/ч', end='')
        self.speed = i
        print()

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/ч')


class TownCar(Car):
    def go(self):
        super().go()
        if self.speed >= 60:
            print(f'Превышаешь! Не гони!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def go(self):
        super().go()
        if self.speed >= 40:
            print(f'Превышаешь! Не гони!')


class PoliceCar(Car):
    pass


police_car = PoliceCar('Фокус', 'синий', 150, True)
police_car.go()
police_car.show_speed()
police_car.stop()
police_car.turn('лево')
police_car.go()
police_car.turn('лево')
police_car.stop()
print()
town_car = TownCar('Смарт', 'красный', 120)
town_car.go()
town_car.turn('право')
town_car.stop()
