# student Pavel Tinyakov

goods_list = []
count = 0
stop = 'да'
while stop != 'нет':
    count += 1
    goods_list.append((count, {'Название': input('Название товара: '), 'Цена': float(input('Цена товара: ')),
                               'Количество': int(input('Количество товара: ')),
                               'Ед. измерения': input('Ед. измерения товара: ')}))
    stop = input('Добавляем еще товар? Введите "да" или "нет" >>> ')
print(goods_list)

a_n = []
a_c = []
a_q = []
a_u = []
a_dict = {}
for i in range(len(goods_list)):
    for k, v in goods_list[i][1].items():
        if k == 'Название':
            a_n.append(v)
            a_dict[k] = a_n
        if k == 'Цена':
            a_c.append(v)
            a_dict[k] = a_c
        if k == 'Количество':
            a_q.append(v)
            a_dict[k] = a_q
        if k == 'Ед. измерения':
            a_u.append(v)
            a_dict[k] = a_u
print(a_dict)
