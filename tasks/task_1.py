# student Pavel Tinyakov

a = 3
b = 4.25
c = '*student*'
d = True
e = [a, b, c, d]
f = a, b, c, d
g = {a: b, c: d}

number = int(input('Введите целое число: '))
print('*--*' * number)
print(f'int {a}, float {b}, str {c}, bool {d} \n'
      f'list {e} \n'
      f'tuple {f} \n'
      f'dict {g}')
print('*--*' * number)

a = number
print(a > b)
e = a
print(e)
e += a
print(e)
e = str(e) + c
print(e)
e = [i for i in e]
print(e)
e = set(e)
print(e)
print(g.keys())
print(g.values())
