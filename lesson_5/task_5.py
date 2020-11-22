# Pavel Tinyakov

from random import randrange

n = int(input('Сколько чисел записывать в файл: '))

with open('task_5.txt.', 'w+', encoding='utf-8') as data:
    for i in range(n):
        data.write(f'{randrange(1, 1000)} ')
    data.seek(0)
    ls_num = data.readline().split()

res = sum(map(int, ls_num))
print('Сумма чисел в файле:', res)
