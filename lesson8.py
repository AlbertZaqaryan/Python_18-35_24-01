# -------------------------------------------------
# for i in range(0, 6): # i = 2
#     for j in range(i, 11 + i, 2):
#         print(f'{j:>4}', end=' ')
#     print()

# -------------------------------------------------
# n = int(input('Enter size: '))
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end=' ')
#     print()
# -------------------------------------------------
# l = int(input('Enter l: '))
# w = int(input('Enter w: '))
# for i in range(l + 1):
#     for j in range(w + 1):
#         if j == 0 or j == w:
#             print('|', end=' ')
#         elif i == 0 or i == l:
#             print('-', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# -------------------------------------------------
# n = int(input('Enter number count: '))
# count = 0
# for i in range(n):
#     number = int(input('Enter number:  '))
#     for j in range(2, int(number ** 0.5) + 1):
#         if number % j == 0:
#             break
#     else:
#         count += 1
# print(count)
# -------------------------------------------------
# n = int(input('Enter number: '))
# summ = 0
# for i in range(1, n + 1):

#     fact = 1
#     for j in range(1, i + 1):
#         fact *= j
#     summ += fact

# print(summ)
# -------------------------------------------------
# n = int(input('Enter number count: '))
# max_sum = 0
# max_number = 0
# for i in range(n):
#     summ = 0
#     number = int(input('Enter number: '))
#     for i in str(number):
#         summ += int(i)
#     if summ > max_sum:
#         max_sum = summ
#         max_number = number
# print(max_sum, max_number)
# -------------------------------------------------
# text = 'python'

# 'p'
# 'py'
# 'pyt'
# 'pyth'
# 'pytho'
# 'python'
# 'pytho'
# 'pyth'
# 'pyt'
# 'py'
# 'p'

# -------------------------------------------------

# n = int(input('Enter size: '))
# for i in range(1, n + 1):
#     for j in range(1, 2 * n):
#         print('.', end=' ')
#     print()
# -------------------------------------------------

# for

#     for

#     for
# -------------------------------------------------


# n1 = 0
# n2 = 1
# n = int(input('Enter n: '))
# for i in range(n + 1):
#     print(n1)
#     n1, n2 = n2, n1 + n2

# -------------------------------------------------

# n = int(input('Enter number: '))
# print(3 - n)
# -------------------------------------------------

# a = 5
# b = 7
# a = a + b # 12
# b = a - b # 5
# a = a - b # 7
# # a, b = b, a
# print(a, b)
# -------------------------------------------------
