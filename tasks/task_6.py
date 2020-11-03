# student Pavel Tinyakov

a = int(input('Введите результат в 1-й день (км): '))
b = int(input('Сколько км планируете пробежать: '))
print(f'1-й день: {a}')
day = 1
while a < b:
    day += 1
    a *= 1.1
    print(f'{day}-й день: {round(a, 2)}')
else:
    print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км')
