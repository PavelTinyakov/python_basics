# student Pavel Tinyakov

number = int(input('Введите положительное целое число: '))
result = 0
if number < 10:
    result = number
else:
    while number > 10:
        n = number % 10
        number //= 10
        if n > result:
            result = n
print(f'Cамая большая цифра в числе {result}')
