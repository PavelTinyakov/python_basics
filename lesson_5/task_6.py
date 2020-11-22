# Pavel Tinyakov

from re import findall

with open('task_6.txt', encoding='utf-8') as data:
    d = {}
    for line in data.readlines():
        ls_line = line.split(': ')
        d[ls_line[0]] = ls_line[1]

for k, v in d.items():
    v = findall(r'\d+', v)
    d[k] = sum(map(int, v))
print(d)
