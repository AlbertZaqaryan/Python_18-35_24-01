# -----------------------------------------------------------
# summ = 0
# count = 0
# while True:
#     number = int(input('Enter number: '))
#     if number == 0:
#         break
#     else:
#         summ += number
#         count += 1
# print(summ / count)
# -----------------------------------------------------------
# for i in range(5, 26, 5):
#     dicount_price = i - 0.05
#     price = round(dicount_price + dicount_price * 60 / 100, 2)
#     print(f'discount price -> {dicount_price}, price -> {price}')
# -----------------------------------------------------------
# kassa = 0
# while True:
#     age = input('Enter human age:  ')
#     if age == '':
#         break
#     else:
#         age = int(age)
#         if 2 >= age > 0:
#             continue
#         elif 12 >= age > 2:
#             kassa += 14
#         elif age > 65:
#             kassa += 18
#         else:
#             kassa += 23
# print(kassa)
# -----------------------------------------------------------

# binary_code = input('Enter binary code: ')
# if len(binary_code) == 8:
#     count = 0
#     for i in binary_code:
#         if i == '1':
#             count += 1
#         elif i == '0':
#             continue
#         else:
#             print('ERROR')
#             count = 0
#             break
#     if count != 0:
#         if count % 2 == 0:
#             print('Even bit')
#         else:
#             print('Odd bit')
# else:
#     print('ERROR')
# -----------------------------------------------------------


# pi = 3
# a = 2
# b = 3
# c = 4
# for i in range(0, 15):
#     pi += (4 / (a * b * c)) * ((-1) ** i)
#     a += 2
#     b += 2
#     c += 2
#     print(pi)
# -----------------------------------------------------------


# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('Fizz-Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)
# -----------------------------------------------------------


# number = int(input('Enter number: '))
# text = ''
# while number != 1:
#     text += str(number % 2) 
#     number //= 2
# print('1' + text[::-1])
# -----------------------------------------------------------


# import random

# summ = 0
# for i in range(10):
#     count_O = 0
#     count_P = 0
#     text = ''
#     while True:
#         if count_O == 3 or count_P == 3:
#             summ += len(text)
#             print(text, f"(попыток: {len(text)})")
#             break
#         money = random.choice('OP')
#         if money == 'O':
#             count_O += 1
#             count_P = 0
#         elif money == 'P':
#             count_P += 1
#             count_O = 0
#         text += money
# print(f"Среднее количество попыток: {summ / 10}.")
# -----------------------------------------------------------
# y = x3 + 2 x2 - 4 x + 1
# start = int(input('Enter start: '))
# stop = int(input('Enter stop: '))
# step = int(input('Enter step: '))
# for x in range(start, stop + 1, step):
#     print(f'x = {x} -> y = {x ** 3 + 2 * x ** 2 - 4 * x + 1}')
# -----------------------------------------------------------
# x = int(input('Enter boys number: '))
# y = int(input('Enter girls number: '))

# B = x # 5 # 3 # 1
# G = y # 3 # 2 # 1

# if B>=G and B/G<=2:
#     while B!=G:
#         print('BGB', end='')
#         B-=2
#         G-=1
#     while B!=0 and G!=0:
#         print('BG', end='')
#         B-=1
#         G-=1
# elif G>B and G/B<=2:
#     while G!=B:
#         print('GBG', end='')
#         G-=2
#         B-=1
#     while B!=0 and G!=0:
#         print('GB', end='')
#         B-=1
#         G-=1
# else:
#     print('No Way!')
# -----------------------------------------------------------
# for i in range(1, 3): # i = 1
#     for j in 'abc': # j = 'c'
#         print(i, j, end=' ')
#     print('$')
# -----------------------------------------------------------
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i * j:>4}', end='')
#     print()
# -----------------------------------------------------------

# for i in range(16, 100):
#     if i == 5:
#         print('5 ka')
#         break
# else:
#     print('5 chka')
# -----------------------------------------------------------


# if 0:
#     print('Python')
# -----------------------------------------------------------

# n = int(input('Enter size: '))
# for i in range(0, n + 1):
#     for j in range(0, n + 1):
#         if i == j or i + j == n:
#             print('^', end='')
#         else:
#             print(' ', end='')
#     print()

# -----------------------------------------------------------

