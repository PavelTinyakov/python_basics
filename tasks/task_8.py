# student Pavel Tinyakov

user_list = list(input('Введите произвольный набор символов: '))
new_list = []
for i in range(1, len(user_list), 2):
    new_list += user_list[i] + user_list[i - 1]
if len(user_list) % 2 != 0:
    new_list.append(user_list[-1])
print(new_list)
