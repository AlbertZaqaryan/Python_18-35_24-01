# while True:
#     password = input('Enter password: ')
#     number_count = 0
#     char_count = 0
#     if len(password) < 8:
#         print('Your password is not strong!!!')
#     else:
#         if password[0].isupper():
#             for i in password:
#                 if i.isdigit():
#                     number_count += 1
#                 elif i.isalpha():
#                     continue
#                 else:
#                     char_count += 1
#             if char_count >= 2 and number_count >= 2:
#                 print(password, 'IS VERY STRONG')
#                 break
#             else:
#                 print('Your password is not strong!!!')
#         else:
#             print('Your password is not strong!!!')


# link = "https://www.youtube.com/watch?v=RRW2aUSw5vU"
# print(link[link.index('=') + 1:])
# link = link.split('=')
# print(link[1])


# text = input('Enter word:  ')
# print(text == text[::-1])

# text = 'python'
# print(list(text))

# number = input('Enter 5 numbers: ').split(' ')
# print([int(i) for i in number if int(i) % 2 == 0])

# mylist = [7, 7, 4, 1, 5, 6, 9, 8, 7, 4, 10, 6, 8, 4, 2, 6, 5, 7, 8]
# for i in mylist.copy():
#     if i % 2 == 0:
#         mylist.remove(i)
# print(mylist)

# mylist = [7, 7, 4, 1, 5, 6, 9, 8, 7, 4, 10, 6, 8, 4, 2, 6, 5, 7, 8]
# for i in range(len(mylist) - 1, -1, -1):
#     if mylist[i] % 2 == 0:
#         mylist.pop(i)
# print(mylist)


# mylist = [7, 7, 4, 1, 5, 5, 5, 5, 5, 5, 6, 9, 8, 7, 4, 10, 6, 8, 4, 2, 6, 5, 7, 8]
# for i in range(len(mylist) - 1, -1, -1):
#     if mylist.count(mylist[i]) > 1:
#         mylist.pop(i)
# print(mylist)


# text = 'ssbbsbsbsbbssssssssssbsbsssssbsbsbsbsbs'
# text_s = 's' * len(text)
# while text_s not in text:
#     text_s = text_s[:-1]
# print(text_s, len(text_s))


# mylist = [4, 10, 15, 27, 30, 36, 40, 52, 64, 78, 125, 223, 358, 445]
# n = 223
# start = 0
# stop = len(mylist)
# while True:
#     mid = (start + stop) // 2
#     if n == mylist[mid]:
#         print(mid)
#         break
#     elif n > mylist[mid]:
#         start = mid + 1
#     else:
#         stop = mid - 1


# list1=[[5,18],[28.38],[50,70],[95,98]]
# list2=[[1,9],[14,25],[30,48],[55,75],[78,83],[92,97]]
# for i in list1:
#     for j in list2:
#         if min(i[-1],j[-1])>=max(i[0],j[0]):
#             print([max(i[0],j[0]),min(i[-1],j[-1])])



# user = {
#     "username":"_Gugo_777", 
#     "password":"ILovePython123$"
# }
# print(user)

# dict_ = {
#     'a':1,
#     'b':[1, 2, 3],
#     'a':10,
#     'c':[1, 2, 3],
#     1:[1, 2, 3]
# }
# print(dict_)


# dict_ = {
#     'a':10,
#     'b':4,
#     'c':-8
# }
# print(dict_['a'])
# print(dict_['Ճ'])
# print(dict_.get('a', 'ՉԿԱ!'))
# dict_['a'] = 77
# dict_['Ճ']  = 55
# dict_.setdefault('Չ', 30)
# print(dict_)
# print(dict_.keys())
# print(dict_.values())
# print(dict_.items())

# test_list = [(1,'a'), (2, 'c'), (3, 'p')]
# print(dict(test_list))

# dict_ = {
#     'a':10,
#     'b':4,
#     'c':-8
# }
# new_dict = {
#     'Ա':10,
#     'Բ':11
# }
# del dict_['a']
# print(dict_)
# dict_.popitem()
# print(dict_)

# dict_.pop('a')
# print(dict_)
# print(len(dict_))

# dict_.clear()
# print(dict_)
# dict_.update(new_dict)
# print(dict_)



# dict_ = {
#     'a':10,
#     'b':4,
#     'c':-8
# }
# x = sorted(dict_, reverse=True)
# x = sorted(dict_.values(), reverse=True)
# print(x)
# x = sorted(dict_, key=dict_.get)
# print(x)

# dict_ = {
#     'a':{
#         'b':10
#     }
# }
# print(dict_['a']['b'])



# MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
#                     'C':'-.-.', 'D':'-..', 'E':'.',
#                     'F':'..-.', 'G':'--.', 'H':'....',
#                     'I':'..', 'J':'.---', 'K':'-.-',
#                     'L':'.-..', 'M':'--', 'N':'-.',
#                     'O':'---', 'P':'.--.', 'Q':'--.-',
#                     'R':'.-.', 'S':'...', 'T':'-',
#                     'U':'..-', 'V':'...-', 'W':'.--',
#                     'X':'-..-', 'Y':'-.--', 'Z':'--..',
#                     '1':'.----', '2':'..---', '3':'...--',
#                     '4':'....-', '5':'.....', '6':'-....',
#                     '7':'--...', '8':'---..', '9':'----.',
#                     '0':'-----', ', ':'--..--', '.':'.-.-.-',
#                     '?':'..--..', '/':'-..-.', '-':'-....-',
#                     '(':'-.--.', ')':'-.--.-', ' ':' '}
# text = input('Enter text: ').upper()
# for i in text:
#     print(MORSE_CODE_DICT.get(i), end='')



dict_ = {
    1 :'AEILNORSTU',
    2 :'DG',
    3 :'BCMP',
    4 :'FHVWY',
    5 :'K',
    8 :'JX',
    10:' QZ'
}
text = input('Enter name: ').upper() # 'ALBERT'
summ = 0
for i in text:
    for j in dict_:
        if i in dict_.get(j):
            summ += j
print(summ)