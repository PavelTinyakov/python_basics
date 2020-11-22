# Pavel Tinyakov


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


position1 = Position('Василий', 'Ивановов', 'логист', 100, 30)
position2 = Position('Петр', 'Сидоров', 'офис менеджер', 80, 10)
position2.name = 'Артем'

print(f'{position1.get_full_name()} оплата в месяц {position1.get_total_income()} руб.')
print(f'{position2.get_full_name()} оплата в месяц {position2.get_total_income()} руб.')
