# student Pavel Tinyakov

user_list = input('Введите нескольких слов, разделённых пробелами: ').split()

for ind, el in enumerate(user_list, 1):
    if len(el) > 10:
        el = el[:10]
    print(ind, el)
