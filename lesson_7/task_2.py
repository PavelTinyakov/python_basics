# Pavel Tinyakov

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, size, height):
        self.name = name
        self.size = size
        self.height = height

    def __str__(self):
        return f'Ткани на {self.name} {self.consumption}'

    def __add__(self, other):
        return f'Всего ткани {self.consumption + other.consumption}'

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    @property
    def consumption(self):
        return round(self.height * 2 + 0.3, 2)


coat = Coat('пальто красивое', 52, 1.98)
suit = Suit('костюм деловой', 52, 1.98)
print(coat)
print(suit)
print(coat + suit)

# чтобы было :)
print(coat.consumption)
print(suit.consumption)
