# student Pavel Tinyakov

def exp_var1(x, y):
    return x ** y


def exp_var2(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y < 0:
        return 1 / result
    return result


print(exp_var1(5, -3))
print(exp_var2(5, -3))
