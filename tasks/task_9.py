# student Pavel Tinyakov

number = int(input('Введите месяц в виде целого числа: '))

season_list = [['зима', 1, 2, 12], ['весна', 3, 4, 5], ['лето', 6, 7, 8], ['осень', 9, 10, 11]]
for i in season_list:
    if number in i:
        print(i[0])

season_dict = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for k, v in season_dict.items():
    if number in v:
        print(k)
