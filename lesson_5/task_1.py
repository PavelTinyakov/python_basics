# Pavel Tinyakov

with open('task_1.txt', 'w', encoding='utf-8') as data:
    while True:
        str_in = input()
        if not str_in:
            break
        data.write(f'{str_in}\n')
