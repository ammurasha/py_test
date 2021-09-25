import math
import re

a = 10
for i in range(1, 7):
    print(i)
    a = a * i
    print(a)


def ttt():
    print('ttt')


def ttt1():
    print('ttt1')


ttt()
ttt1()
ttt()

result = re.findall(r'\w+', 'AV is largest Analytics community of India')
print(result)

emails = re.findall(r'@(\w+.\w+)', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print(emails)