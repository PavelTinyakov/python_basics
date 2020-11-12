# Pavel Tinyakov

from functools import reduce


ls = [i for i in range(100, 1001, 2)]
result = reduce(lambda x, y: x * y, ls)
print(result)
