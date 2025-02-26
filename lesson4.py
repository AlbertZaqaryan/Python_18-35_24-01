# ------------------------------------------------------
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# print((a > b) * a + (a <= b) * b)
# print(min(a, b))
# print(max(a, b))
# print(sum((a, b)))
# ------------------------------------------------------
# number = int(input('Enter number: ')) # 632
# count_200 = number // 200 # 3
# number %= 200 # 32
# count_100 = number // 100 # 0
# number %= 100 # 32
# count_25 = number // 25 # 1
# number %= 25 # 7
# count_10 = number // 10 # 0
# number %= 10 # 7
# count_5 = number // 5 # 1
# number %= 5 # 2
# count_1 = number // 1 # 2
# print(f'200 ({count_200})\n100 ({count_100})\n25 ({count_25})\n10 ({count_10})\n5 ({count_5})\n1 ({count_1})')

# ------------------------------------------------------
# number = input('Enter number: ')
# print(int(number[0]) + int(number[1]) + int(number[2]) + int(number[3]))

# number = int(input('Enter number: '))
# print(number % 10 + number // 10 % 10 + number // 100 % 10 + number // 1000)
# ------------------------------------------------------
# count = int(input('Enter count: '))
# price = 3.49
# disc_price = 3.49 - 3.49 * 60 / 100
# print(f'price = ${count * price}\ndiscount price = ${round(count * disc_price, 2)}')
# ------------------------------------------------------
# r = 500
# print(3.14 * r ** 2)

# import matem
# r = 500
# print(matem.PI * r ** 2)


# import math

# print(math.pi)
# print(math.e)
# print(math.tau)

# x = 7.25
# print(round(x))


# x = 7.025
# print(math.ceil(x))

# x = 8.69
# print(math.floor(x))

# print(math.pow(5, 6))
# 5 ** 6

# print(math.sqrt(64))
# print(64 ** 0.5)

# print(math.factorial(5))

# -------------------------------------------------------
# import calendar

# print(calendar.calendar(2025))
# -------------------------------------------------------
# import datetime
# print(datetime.datetime.now())
# -------------------------------------------------------
# import time

# print(3)
# time.sleep(2)
# print(2)
# time.sleep(2)
# print(1)
# time.sleep(2)
# print('Start game')

# st = time.time()
# print([i ** 2 for i in range(100000)])
# et = time.time()
# print(et - st)
# -------------------------------------------------------
# import random

# random.seed(43)
# print(random.randint(1, 19))

# print(random.random())
# print(random.randint(-100, 56))
# print(random.randrange(0, 19, 2))
# text = 'python'
# print(random.choice(text))


# tarberakner = 'Qar', 'Mkrat', 'Tuxt'
# print(random.choice(tarberakner))

# -------------------------------------------------------
# import math
# from math import *

# print(pi)
# print(e)
# print(sqrt())
# print(math.pi)

# from math import pi, sqrt

# print(pi)

# import math as m

# print(m.pi)
# -------------------------------------------------------
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))

# x = int(input('Enter x: '))
# y = int(input('Enter y: '))

# if a > b:
#     print('a is max')
# elif a < b:
#     print('b is max')
# else:
#     print('a == b')
# -------------------------------------------------------

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))

# x = int(input('Enter x: '))
# y = int(input('Enter y: '))

# if a > b:
#     print('a is max')
# if x > y:
#     print('x is max')
# -------------------------------------------------------
# andzrev = input('Andzrev galis e te voch: ')
# if andzrev == 'Ha':
#     print('Mna tany')
# else:
#     meqenan = input('Lvanal meqenen?  ')
#     if meqenan == 'Ha':
#         print('Gnacir de meqenayi hetevic')
#     else:
#         print('Andzrev chi bayc du tann es')
# -------------------------------------------------------
# dog_age = int(input('Enter dog age: '))
# if dog_age <= 2:
#     print(f'Human age = {dog_age * 10.5}')
# else:
#     print(f'Human age = {21 + (dog_age - 2) * 4}')
# -------------------------------------------------------
# letter = input('Enter letter: ').lower()
# if letter in 'aeiou':
#     print('vowel')
# else:
#     print('consonant')
# -------------------------------------------------------
# year = int(input('Enter year: '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('Leap')
# else:
#     print('No Leap')
# -------------------------------------------------------
# number = int(input('Enter number: '))
# if number % 2 == 0:
#     print('Even')
# else:
#     print('Odd')