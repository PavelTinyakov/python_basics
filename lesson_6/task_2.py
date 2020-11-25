# Pavel Tinyakov

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_calc(self, weight, height):
        return self._length * self._width * weight * height / 1000


road = Road(5000, 20)
print(f'Для покрытия всего дорожного полотна неободимо {road.weight_calc(25, 5)} тонн асфальта')
