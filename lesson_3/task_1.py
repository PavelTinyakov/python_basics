# student Pavel Tinyakov

def division2(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'


print(division2(10, 0))
