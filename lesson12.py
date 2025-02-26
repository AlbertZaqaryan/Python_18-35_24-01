# x = {'D':56, 'E': 12, 'F':69, 'C': 45, 'B':23, 'A': 67}
# values = sorted(x.values(), reverse=True)[:3]
# keys = sorted(x, key=x.get, reverse=True)[:3]
# dict_ = {}
# for i in range(len(keys)):
#     dict_[keys[i]] = values[i]
# print(dict_)
# ---------------------------------------------------------------------------
# x = {'D':56, 'E': 12, 'F':69, 'C': 45, 'B':23, 'A': 67}
# print({i:x[i] for i in sorted(x, key=x.get, reverse=True)[:3]})
# ---------------------------------------------------------------------------

# students_dict = {
#     'Student_1': 4,
#     'Student_2': 7,
#     'Student_3': 3,
#     'Student_4': 5,
#     'Student_5': 10,
#     'Student_6': 6,
#     'Student_7': 8,
#     'Student_8': 2,
#     'Student_9': 9,
#     'Student_10': 1
# }
# mean_score = sum(students_dict.values()) / len(students_dict)
# good_students = [i for i in students_dict if students_dict[i] >= mean_score]
# bad_students = [i for i in students_dict if students_dict[i] < mean_score]
# print(good_students)
# print(bad_students)
# ---------------------------------------------------------------------------

# s = 'a,2,b,5,c,8,a,4,e,11'
# s = s.split(',')
# dict_ = {}
# for i in range(0, len(s), 2):
#     if s[i] in dict_:
#         dict_[s[i]] += int(s[i + 1])
#     else:
#         dict_[s[i]] = int(s[i + 1])
# print(dict_)
# ---------------------------------------------------------------------------


# text = 'exercises'
# print({i:text.count(i) for i in text})
# ---------------------------------------------------------------------------


# my_dict={
#     '1': '.,?!:',
#     '2': 'ABC',
#     '3': 'DEF',
#     '4': 'GHI',
#     '5': 'JKL',
#     '6': 'MNO',
#     '7': 'PQRS',
#     '8': 'TUV',
#     '9': 'WXYZ',
#     '0': ' '
# }
# text = input('Enter text: ').upper()
# for i in text:
#     for j in my_dict:
#         if i in my_dict[j]:
#             print(j * (my_dict[j].index(i) + 1), end='')
# ---------------------------------------------------------------------------


# list1=[[5, 18], [28, 38], [50,70], [95, 98]]
# list2=[[1, 9], [14, 25], [30, 48], [55, 75], [78, 83], [92, 97]]

# meeting=8

# i=0
# j=0

# while i<=len(list1)-1 or j<=len(list2)-1:
#     if list1[i][0]<list2[j][1] and list1[i][1]>=list2[j][1]:
#         if list2[j][1]-list1[i][0]>=meeting:
#             print(list1[i][0], list2[j][1])
#             break
#         else:
#             i+=1
#     elif list1[i][0]<list2[j][1] and list2[j][1]>list1[i][1]:
#         if list1[i][1]-list1[i][0]>=meeting:
#             print(list1[i][0], list1[i][1])
#             break
#     else:
#         i+=1
#     if list2[j][0]<list1[i][1] and list2[j][1]>=list1[i][1]:
#         if list1[i][1]-list2[j][0]>=meeting:
#             print(list2[j][0], list1[i][1])
#             break
#         else:
#             j+=1
#     elif list2[j][0]<list1[i][1] and list2[j][1]>=list1[i][1]:
#         if list2[j][1]-list2[j][0]>=meeting:
#             print(list2[j][0], list2[j][1])
#             break
#     else:
#         j+=1
# ---------------------------------------------------------------------------

# slotA = [[10, 50], [60, 120], [140, 210]]
# slotB = [[0, 15], [60, 70]]
# dur = 8
# i, j = 0, 0
# while i < len(slotA) and j < len(slotB):
#     start = max(slotA[i][0], slotB[j][0])
#     stop = min(slotA[i][1], slotB[j][1])
    
#     if stop - start >= dur:
#         print(start, start + dur)
#         break
    
#     if slotA[i][1] < slotB[j][1]:
#         i += 1
#     else:
#         j += 1
# else:
#     print(None)
# ---------------------------------------------------------------------------

# n = int(input('Enter number: '))
# print([1 if i % 2 == 0 else i % 5 for i in range(0, n)])
# ---------------------------------------------------------------------------

# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# print([i for i in nice_list for i in i for i in i])
# ---------------------------------------------------------------------------


# mylist = ['flower', 'flow', 'flight']
# mylist.sort(key=len)
# index = 1
# while index < len(mylist):
#     if mylist[0] == mylist[index][:len(mylist[0])]:
#         index += 1
#     else:
#         mylist[0] = mylist[0][:-1]
# print(mylist[0])
# ---------------------------------------------------------------------------

# mylist = [170, -1, 160, 150, -1, -1, 190, 180]
# [150, -1, 160, 170, -1, -1, 180, 190]
# ---------------------------------------------------------------------------



# mylist = [7, 4, 1, 5, 5, 5, 2, 6, 9, 7,9, 8, 7, 8, 7, 3, 6, 3, 3, 4, 1]

# mylist.sort()

# if mylist[0] != mylist[1]:
#     print(mylist[0])

# if mylist[-1] != mylist[-2]:
#     print(mylist[-1])

# for i in range(0,len(mylist)-1):

#     if mylist[i] != mylist[i+1] and mylist[i] != mylist[i-1]:
#         print(mylist[i])

