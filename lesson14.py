# text1 = 'liveev'
# text2 = 'ivlev'
# dict1 = {i:text1.count(i) for i in text1}
# dict2 = {i:text2.count(i) for i in text2}
# print(dict1 == dict2)

# s = 'a,2,b,3,c,4,e,11,a,4,b,5'
# # {'a':6, 'b':8, 'c':4, 'e':11}
# s = s.split(',')
# x = {}
# for i in range(0, len(s), 2):
#     let = s[i]
#     number = int(s[i + 1])
#     if let in x:
#         x[let] += number
#     else:
#         x[let] = number
# print(x)

# dict1 = {'a':2, 'b':2, 'c':1}
# x = {}
# for i in dict1:
#     if dict1[i] not in x:
#         x[dict1[i]] = i
#     else:
#         x[dict1[i]] = list(x[dict1[i]])
#         x[dict1[i]].append(i)
# print(x)

# users = {
#     'User1':6,
#     'User2':4,
#     'User3':10,
#     'User4':1,
#     'User5':7,
#     'User6':5
# }
# mean_score = sum(users.values()) / len(users)
# for i in users:
#     if users[i] > mean_score:
#         print(i)