# student Pavel Tinyakov

def print_data_user(**kwargs):
    for v in kwargs.values():
        print(v, end=' ')


print_data_user(name='Петр', surname='Петров', city='Москва', email='mail@mail.ru', phone='84991234567')
