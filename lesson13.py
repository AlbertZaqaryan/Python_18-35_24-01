# x = {'a':10, 'b':20}
# y = {1, 2, 3}
# print(type(x))
# print(type(y))
# ----------------------------------------------
# x = set()
# print(type(x))
# ----------------------------------------------
# x = {1, 8, 5, 1, 1, 16, 4, 7, 8, 5, 6}
# print(x)
# ----------------------------------------------
# mylist = [7, 4, 1, 4, 5, 6, 9, 8, 7, 4, 4, 4, 4, 4]
# print(set(mylist))
# ----------------------------------------------
# set1 = {1, 2, 4}
# for i in range(0, len(set1)):
#     print(set1[i])
# ----------------------------------------------
# set1 = {1, 2, 4}
# set1.add(5)
# set1.discard(2)
# print(set1)
# ----------------------------------------------
# A = {1, 2, 3, 6, 5, 8, 7, 4}
# B = {-10, 1, 2, 3, 5, -5, 0}
# print(A.isdisjoint(B))
# print(A.union(B))
# print(A.difference(B))
# print(B.difference(A))
# print(A.intersection(B))
# ----------------------------------------------
# print(2 ** 20)
# mylist = [7, 4, 1, 5, 10, 2, 5]
# for i in range(10):
#     mylist.append(i)

# for i in range(10):
#     mylist.insert(1, i)

# for i in mylist:
#     if mylist.count(i) > 1:
#         print(i)

import random

bingo = {
    "B":random.sample(range(1, 15), 5),
    "I":random.sample(range(16, 30), 5),
    "N":random.sample(range(31, 45), 5),
    "G":random.sample(range(46, 60), 5),
    "O":random.sample(range(61, 75), 5),
}
state = True
while state:
    input('Enter for generate new number: ')
    random_number = random.randint(1, 75)
    print(f'-------------> {random_number} <-----------------')
    for i in bingo:
        if random_number in bingo[i]:
            bingo[i][bingo[i].index(random_number)] = 'X'
        print(f'{i}: {bingo[i]}')
        if bingo[i].count('X') == 5:
            state = False
        

# import random
# import msvcrt
# import os

# monkey = '🐒'
# banana = '🍌'

# monkey_i = random.randint(1, 20)
# monkey_j = random.randint(1, 20)
# banana_i = random.randint(1, 20)
# banana_j = random.randint(1, 20)

# while True:

#     for i in range(1, 21):
#         for j in range(1, 21):
#             if i == monkey_i and j == monkey_j:
#                 print(monkey, end=' ')
#             elif i == banana_i and j == banana_j:
#                 print(banana, end=' ')
#             else:
#                 print(' .', end=' ')
#         print()
#     step = msvcrt.getwch()
#     if step == 'w':
#         monkey_i -= 1
#     elif step == 'q':
#         break



#     os.system('cls')

# import time

# n = 5
# while True:
#     time.sleep(n)
#     print('🐒')
#     n -= 1