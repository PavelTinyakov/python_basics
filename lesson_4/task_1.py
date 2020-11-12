# Pavel Tinyakov

from sys import argv

pay, hour, prize = argv[1:]
print('выработка в часах:', pay)
print('ставка в час:', hour)
print('премия:', prize)
print('к оплате:', int(pay) * int(hour) + int(prize))
