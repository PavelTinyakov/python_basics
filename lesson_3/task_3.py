# student Pavel Tinyakov

def max3_sum(a, b, c):
    return max(b + c, max(a + b, a + c))


print(max3_sum(-5, 7, 2))
