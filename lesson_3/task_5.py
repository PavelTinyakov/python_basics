# student Pavel Tinyakov

def cycle_inp_sum_number():
    text = 'Введите числа через пробел. Для выхода введите любой символ: '
    result = 0
    try:
        while True:
            for i in map(int, input(text).split()):
                result += i
            print(result)
    except ValueError:
        print(result)


cycle_inp_sum_number()
