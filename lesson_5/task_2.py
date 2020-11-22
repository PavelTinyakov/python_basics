# Pavel Tinyakov

with open('task_2.txt', encoding='utf-8') as data:
    lines = data.readlines()

print(f'В файле {len(lines)} строк')
for ind, line in enumerate(lines, 1):
    print(f'Слов в {ind} строке - {len(line.split())}')
