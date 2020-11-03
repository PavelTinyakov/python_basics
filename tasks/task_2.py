# student Pavel Tinyakov

user_sec = int(input('Введите время в секундах: '))

hour = user_sec // 3600
minute = (user_sec % 3600) // 60
second = (user_sec % 3600) % 60

if hour < 10:
    hour = '0' + str(hour)
if minute < 10:
    minute = '0' + str(minute)
if second < 10:
    second = '0' + str(second)

print(f'{hour}:{minute}:{second}')
