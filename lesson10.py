# 113, 116, 117, 133, 134,
# -------------------------------------------------------------
# mylist = []
# while True:
#     word = input('Enter word: ')
#     if word == '':
#         break
#     elif word not in mylist:
#         mylist.append(word)
# print(mylist)
# -------------------------------------------------------------
# for n in range(1, 10001):
#     n_list = [i for i in range(1, n // 2 + 1) if n % i == 0]
#     if sum(n_list) == n:
#         print(n)
# -------------------------------------------------------------
# text = "Contr.actions!, ?include: (don’t), isn’t, and wouldn’t."
# text = text.split(' ')
# for i in range(len(text)):
#     while True:
#         if not text[i][0].isalpha():
#             text[i] = text[i][1:]
#         elif not text[i][-1].isalpha():
#             text[i] = text[i][:-1]
#         else:
#             break
# print(' '.join(text))
# -------------------------------------------------------------
# mylist = [1, 2, 3, 4]
# newlist = [[]]
# [[], [1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3], [2, 3, 4], [1, 2, 3, 4]]
# for i in range(len(mylist)):
#     for j in range(i + 1, len(mylist) + 1):
#         newlist.append(mylist[i:j])
# print(newlist)
# -------------------------------------------------------------
# mylist = [1, 2, 3, 4]
# print([mylist[i:j] for i in range(len(mylist)) for j in range(i + 1, len(mylist) + 1)])
# -------------------------------------------------------------
# import random

# users_1 = ['Edo', 'Gugo', 'Lyov', 'Karo', 'Anna']
# random.shuffle(users_1)
# for i in range(0, len(users_1) - 1):
#     print(users_1[i], users_1[i + 1])
# print(users_1[-1], users_1[0])

# -------------------------------------------------------------
# users_1 = ['Edo', 'Gugo', 'Lyov', 'Karo', 'Anna']
# users_2 = ['Edo', 'Gugo', 'Lyov', 'Karo', 'Anna']
# final = []
# while users_1 != []:
#     user1 = random.choice(users_1)
#     user2 = random.choice(users_2)
#     if len(users_1) == 1 and len(users_2) == 1 and users_1 == users_2:
#         users_1 = ['Edo', 'Gugo', 'Lyov', 'Karo', 'Anna']
#         users_2 = ['Edo', 'Gugo', 'Lyov', 'Karo', 'Anna']
#         final = []
#     if user1 == user2:
#         continue
#     else:
#         final.append(f'{user1} -> {user2}')
#         users_1.remove(user1)
#         users_2.remove(user2)
# for i in final:
#     print(i)
# -------------------------------------------------------------

# import random
# name_list=[input('Enter name: ') for i in range(5)]
# couples=[]
# for i in name_list:
#     couples.append([i])
# j=0
# while j!=5:
#     name=random.choice(name_list)
#     if name!=couples[j][0]:
#         couples[j].append(name)
#         name_list.remove(name)
#         j+=1
# print(couples)
# -------------------------------------------------------------
# list1 = [[5, 18], [28, 38], [50, 70], [95, 98]]
# list2 = [[1, 9], [14, 25], [30, 48], [55, 75], [78, 83], [92, 97]]
# meeting = 8
# -------------------------------------------------------------
# mylist = [7, 4, 1, -6, 0, 8, 18, 36, 2]
# for i in range(len(mylist)):
#     for j in range(len(mylist)):
#         if mylist[i] < mylist[j]:
#             mylist[i], mylist[j] = mylist[j], mylist[i]
# print(mylist)


# mylist = [4, 10, 15, 27, 30, 36, 40, 52, 64, 78, 125, 223, 358, 445]
# n = 223
# for i in range(len(mylist)):
#     if mylist[i] == n:
#         print(i)


text = 'ssbbsbsbsbbssssssssssbsbsssssbsbsbsbsbs'
# 10