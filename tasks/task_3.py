# student Pavel Tinyakov

number = input('Введите положительное целое число: ')
print(int(number) + int(number * 2) + int(number * 3))

# неоднозначно понял задание, поэтому вариант 2.
number = int(input('и еще раз: '))
count = 0
result = 0
while count != number:
    count += 1
    result += int(str(number) * count)
print(result)
