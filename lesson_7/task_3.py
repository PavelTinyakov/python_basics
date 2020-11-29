# Pavel Tinyakov

class Cell:
    def __init__(self, box):
        self.cell = int(box)

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        result = self.cell - other.cell
        return f'{result}' if result > 0 else 'Вычитание невозможно'

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return self.cell // other.cell

    def make_order(self, row):
        box_row = int(self.cell / row)
        result = ''
        for i in range(box_row):
            result += '*' * row + '\n'
        result += (self.cell - box_row * row) * '*'
        return result


c1 = Cell(37)
c2 = Cell(29)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)

print(c1.make_order(10))

