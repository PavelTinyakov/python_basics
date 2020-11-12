# Pavel Tinyakov

from itertools import count, cycle

for i in count(3):
    if i > 10:
        break
    print(i, end=' ')

print()

ls = ['one', 'two', 'three']
count = 0
for i in cycle(ls):
    count += 1
    if count > 6:
        break
    print(i, end=' ')
