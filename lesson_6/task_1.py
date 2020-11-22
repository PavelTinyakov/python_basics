# Pavel Tinyakov

from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = 'red', 'yellow', 'green'

    def running(self, time_red=7, time_yellow=2, time_green=7):
        colors = cycle(self.__color)
        periods = cycle((time_red, time_yellow, time_green))
        while True:
            print(next(colors))
            sleep(next(periods))


tr_light = TrafficLight()
tr_light.running(time_green=5)

