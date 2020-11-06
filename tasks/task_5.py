# student Pavel Tinyakov

revenue = int(input('Укажите выручку фирмы: '))
cost = int(input('Укажите издержки фирмы: '))
margin = revenue - cost
if margin == 0:
    print('Вы нашли свою точку безубыточности')
elif margin > 0:
    print(f'Вы в плюсе. Рентабельность {round(margin / revenue * 100, 2)}% ')
    pers = int(input('Сколько людей в компании: '))
    print(f'Прибыль фирмы в расчете на сотрудника: {round(margin / pers, 2)}')
else:
    print('Вы в минусе. Займитесь чем-то другим')
