# Pavel Tinyakov

with open('task_3.txt', encoding='utf-8') as data:
    lines = data.readlines()

print('Сотрудники с зарплатой менее 20000:')
total = 0
for line in lines:
    name, salary = line.split()
    total += float(salary)
    if float(salary) < 20000:
        print(name)
print('Средняя зарплата по всем сотрудникам:', round(total / len(lines), 2))
