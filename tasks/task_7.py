# student Pavel Tinyakov

list_ex = [3, 3.63, complex(5, 6), 'example str', ['example list'], ('example tuple', 4, 3), {'example set', 6, 5},
           frozenset('example frozenset'), {'example dict': 'text'}, True, b'example bytes',
           bytearray(b'example bytearray'), None]
for i in list_ex:
    print(f'{i} - {type(i)}')
