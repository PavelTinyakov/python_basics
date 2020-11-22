# Pavel Tinyakov

from json import dump

with open('task_7.txt', encoding='utf-8') as data:
    count = 0
    profit_all = 0
    d_all = {}
    for line in data:
        count += 1
        name, owner, revenue, cost = line.split()
        profit = int(revenue) - int(cost)
        print(f'Прибыль {owner} {name} составляет {profit}')
        d_all[name] = profit
        if profit > 0:
            profit_all += profit
result = [d_all, {'average_profit': round(profit_all / count, 2)}]

with open('task_7.json', 'w', encoding='utf-8') as data_w:
    dump(result, data_w, ensure_ascii=False, indent=4)
