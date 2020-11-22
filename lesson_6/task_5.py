# Pavel Tinyakov

class Stationary:
    def __init__(self, title='руками'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        self.title = 'ручкой'
        print(f'Рисуем {self.title}')


class Pencil(Stationary):
    def draw(self):
        self.title = 'карандашом'
        print(f'Рисуем {self.title}')


class Handle(Stationary):
    def draw(self):
        self.title = 'маркером'
        print(f'Рисуем {self.title}')


stat = Stationary()
pen = Pen()
pencil = Pencil()
handle = Handle()

stat.draw()
pen.draw()
pencil.draw()
handle.draw()
