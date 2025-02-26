# ---------------------------------------------------------------
# import random
# import time


# start = input('Ready?\nYes or No===> ')
# if start == 'Yes':
#     print(3)
#     time.sleep(1)
#     print(2)
#     time.sleep(1)
#     print(1)
#     time.sleep(1)
#     print('START GAME!!!!')
#     pc = random.randint(0, 5)
#     user = int(input('Enter number in range(0, 5):  '))
#     user_points = 0
#     pc_points = 0
#     #-------------------- ROUND 1 --------------------
#     if user == pc: # user = 1, pc = 0
#         user_points += 1
#         print(f'--->Win user<---\nUser = {user}, Pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#         # ------------------- ROUND 2 ----------------------
#         pc = random.randint(0, 5)
#         user = int(input('Enter number in range(0, 5):  '))
#         if user == pc: # user = 2, pc = 0 END GAME WIN USER
#             user_points += 1
#             print(f'--->Win user<---\nUser = {user}, Pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#             print('------------------ WIN USER END GAME -------------------')
#         else: # user = 1, pc = 1, EQUAL
#             pc_points += 1
#             print(f'--->Win pc<---\nUser = {user}, Pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#             # ------------------- ROUND 3 ----------------------
#             pc = random.randint(0, 5)
#             user = int(input('Enter number in range(0, 5):  '))
#             if user == pc: # user = 2, pc = 1 END GAME WIN USER
#                 user_points += 1
#                 print(f'--->Win user<---\nUser = {user}, Pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#                 print('------------------ WIN USER END GAME -------------------')
#             else: # user = 1, pc = 2 END GAME WIN PC
#                 pc_points += 1
#                 print(f'--->Win pc<---\nUser = {user}, Pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#                 print('------------------ WIN PC END GAME -------------------')
#     #-------------------- ROUND 1 --------------------
#     else: # pc = 1, user = 0
#         pc_points += 1
#         print(f'--->Win pc<---\nUser = {user}, Pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#         # ---------------------- ROUND 2 -----------------------
#         pc = random.randint(0, 5)
#         user = int(input('Enter number in range(0, 5):  '))
#         if user == pc: # pc = 1, user = 1
#             user_points += 1
#             print(f'--->Win user<---\nUser = {user}, Pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#             # ---------------------- ROUND 3 -----------------------
#             pc = random.randint(0, 5)
#             user = int(input('Enter number in range(0, 5):  '))
#             if user == pc: # pc = 1, user = 2 END GAME WIN USER
#                 user_points += 1
#                 print(f'--->Win user<---\nUser = {user}, Pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#                 print('------------------ WIN USER END GAME -------------------')
#             else: # pc = 2, user = 1 END GAME WIN PC
#                 pc_points += 1
#                 print(f'--->Win pc<---\nUser = {user}, Pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#                 print('------------------ WIN PC END GAME -------------------')
#         else: # pc = 2, user = 0 END GAME WIN PC
#             pc_points += 1
#             print(f'--->Win pc<---\nUser = {user}, Pc = {pc}\nuser points = {user_points}, pc points = {pc_points}')
#             print('------------------ WIN PC END GAME -------------------')
# else:
#     print('EXIT!!!')
# ---------------------------------------------------------------
# cord = input('Enter cord: ')
# letter = cord[0]
# number = int(cord[1])
# if letter in 'aceg' and number % 2 != 0 or letter in 'bdfh' and number % 2 == 0:
#     print('Black')
# elif letter in 'aceg' and number % 2 == 0 or letter in 'bdfh' and number % 2 != 0:
#     print('White')
# ---------------------------------------------------------------
# for x in range(1, 10):
#     print(x)
# ---------------------------------------------------------------

# for i in range(6):
#     print(i)
# ---------------------------------------------------------------

# n = int(input('Enter n: '))
# for i in range(n):
#     if i % 2 == 0:
#         print(i)
# ---------------------------------------------------------------

# n = int(input('Enter n: '))
# for i in range(0, n, 2):
#     print(i)
# ---------------------------------------------------------------

# for i in range(1, 10):
#     if i == 5:
#         break
#     else:
#         print(i)
# ---------------------------------------------------------------

# for i in range(1, 10):
#     if i == 5:
#         continue
#     print(i)
# ---------------------------------------------------------------

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# if a > b:
#     for i in range(a, (a * b) + 1, a):
#         if i % b == 0:
#             print(i)
#             break
# elif b > a:
#     for i in range(b, (a * b) + 1, b):
#         if i % a == 0:
#             print(i)
#             break
# else:
#     print(a)
# ---------------------------------------------------------------

# n = int(input('Enter number: '))
# f = 1
# for i in range(1, n + 1):
#     f *= i
# print(f)
# ---------------------------------------------------------------


# n = int(input('Enter number: '))
# count = 0
# for i in range(1, n + 1):
#     if i % 5 == 0:
#         count += 1
# print(count)
# ---------------------------------------------------------------


# count = 0
# for i in range(10):
#     number = int(input('Enter number: '))
#     if number % 2 == 0 and number >= 0:
#         count += 1
# print(count)
# ---------------------------------------------------------------


# a = int(input('Enter a:  '))
# b = int(input('ENter b:  '))
# count = 0
# summ = 0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         count += 1
#         summ += i
# print(summ / count)
# ---------------------------------------------------------------
