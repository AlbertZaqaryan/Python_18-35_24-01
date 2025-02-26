# tuple # immutable ()
# list # mutable []

# x = [1, 2, 3, 4] -> list
# x = (1, 2, 3, 4) -> tuple

# x = ('a', 'b', 'c')

# x = ['a', 'b', 'c']


# users = ('Hakob', 'Tigran', 1, True, 35, 8.5, 'Karen')
# users = ['Hakob', 'Tigran', 1, True, 35, 8.5, 'Karen']
# print(users)

# --------------------- list methods ----------------------
# mylist = ['a', 'b', 'c']
# mylist[2] = 'Ճ'
# print(mylist)
# print(mylist[:2])
# mylist += ['e']
# mylist.append('e')
# mylist.append('d')
# mylist.append('f')
# print(mylist)
# mylist.insert(1, 'Ճ')
# print(mylist)
# mylist.remove('b')
# del mylist[1:]
# mylist.pop(1)
# print(mylist)

# mylist = [7, 4, 1, 2, 6]
# mylist.sort(reverse=True)
# print(mylist)

# mylist = ['e', 'd', 'a', 'g', 'b', 'f']
# mylist.sort()
# print(mylist)

# mylist = ['python', 'java', 'programming', 'hello']
# mylist.sort(key=len, reverse=True)
# print(mylist)

# list1 = [1, 2, 3]
# list2 = list1.copy()
# list2.append(4)
# print(list1)


# a = 5
# b = a
# b += 10
# print(a)


# mylist = ['python', 'java', 'programming', 'hello']
# mylist.clear()
# print(mylist)


# mylist = [7, 4, 5, 1, 2, 5, 9, 8, 7, 7, 7, 4, 1, 2, 5, 6]
# print(mylist.count(5))


# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
# print(list1 + list2)
# list1.extend(list2)
# print(list1)

# mylist = ['python', 'java', 'programming', 'hello']
# print(mylist.index("hello")) 


# mylist = []
# while True:
#     number = int(input('Enter number:  '))
#     if number == 0:
#         break
#     else:
#         mylist.append(number)
# mylist.sort()
# print(mylist)


# text = 'python'
# mylist = []
# for i in text:
#     mylist.append(i)
# print(mylist)


# text = 'python'
# print(list(text))

# text = 'python'
# print([i for i in text])

# mylist = [7, 10, 45, 89, 63, 51, 88, 75]
# newlist = []
# for i in mylist:
#     if i % 2 == 0:
#         newlist.append(i)
# print(newlist)


# mylist = [7, 10, 45, 89, 63, 51, 88, 75]
# print([i for i in mylist if i % 2 == 0])


# mylist = [7, 10, 45, 89, 63, 51, 88, 75]
# newlist = []
# for i in mylist:
#     if i % 2 == 0:
#         newlist.append('Even')
#     else:
#         newlist.append('Odd')
# print(newlist)


# mylist = [7, 10, 45, 89, 63, 51, 88, 75]
# print(['Even' if i % 2 == 0 else 'Odd' for i in mylist])


# text = 'p-y-t-h-o-n'
# mylist = text.split('-')
# print(mylist)

# mylist = ['python', 'programming']
# print(' | '.join(mylist))

# mylist = [None]
# print(len(mylist * 10))

# text = 'python'
# print(text[:7])

# list1 = [1, 2, 3]
# list2 = list1
# list2.append(4)
# print(list1)


# print([None] * 10)

# text = 'python'
# print(text[:10])
# ----------------------------------------------
# import random


# tver = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# master = ['♥', '♦', '♣', '♠']
# kalod = [i + j for i in tver for j in master]
# nor_kalod = []
# while kalod != []:
#     random_kart = random.choice(kalod)
#     nor_kalod.append(random_kart)
#     kalod.remove(random_kart)
# xaxacoxner = [input(f"User {i + 1} anuny:  ") for i in range(4)]
# for i in xaxacoxner:
#     print(f'{i} --- {nor_kalod[:8]}')
#     del nor_kalod[:8]
# ----------------------------------------------
# n = int(input('Enter number: '))
# print([i for i in range(1, n) if n % i == 0])
# ----------------------------------------------
# mylist = []
# while True:
#     n = input('Enter number: ')
#     if n == '':
#         break
#     else:
#         mylist.append(int(n))
# print([i for i in mylist if i < 0], [i for i in mylist if i == 0], [i for i in mylist if i > 0])
# ----------------------------------------------
# list1 = [[5, 18], [28, 38], [50, 70], [95, 98]]
# list2 = [[1, 9], [14, 25], [30, 48], [55, 75], [78, 83], [92, 97]]
# meeting = 8