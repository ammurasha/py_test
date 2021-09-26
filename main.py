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

result = re.findall(r'\w+', 'AV is largest Analyt1cs commun1ty of India')
print(result)

emails = re.findall(r'\b((\S+(?=@))@((?<=@)\S+))\b', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print(emails)

pattern = r'((\d)(\d))((\d)(\d))'
string = r'123456789'
match = re.search(pattern, string)
print(f'Найдена подстрока >{match[0]}< с позиции {match.start(0)} до {match.end(0)}')
for i in range(0, 7):
    print(f'Группа №{i} >{match[i]}< с позиции {match.start(i)} до {match.end(i)}')