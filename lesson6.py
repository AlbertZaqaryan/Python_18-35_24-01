# text = "python"
# 785
# for i in range(785):
#     print(i)

# text = "python"
# for i in text:
#     if i == 'o':
#         continue
#     else:
#         print(i)

# 'py'
# 'yt'
# 'th'
# 'ho'
# 'on'
# -------------------------------------------------------------

# text = 'python'
# print(text[0], text[1])
# print(text[1], text[2])
# print(text[2], text[3])
# print(text[3], text[4])
# print(text[4], text[5])
# -------------------------------------------------------------

# text = 'python'
# for i in range(0, len(text) - 1):
#     print(text[i], text[i + 1])

# -------------------------------------------------------------

# text = 'python programming'
# for i in text:
#     print(i)
# -------------------------------------------------------------

# for i in range(0, len(text) - 2):
#     print(text[i], text[i + 1], text[i + 2])
# -------------------------------------------------------------
# text = input('Enter word: ')
# number_count = 0
# letter_count = 0
# char_count = 0
# for i in text:
#     if i.isdigit():
#         number_count += 1
#     elif i.isalpha():
#         letter_count += 1
#     else:
#         char_count += 1
# print(f'number count -> {number_count}\nletter count -> {letter_count}\nchar count -> {char_count}')
# -------------------------------------------------------------
# for i in range(6):
#     print(i)
# -------------------------------------------------------------

# i = 0
# while i < 6:
#     print(i)
#     i += 1
# -------------------------------------------------------------

# summ = 0
# count = 0
# while True:
#     number = int(input('Enter number: '))
#     if number == 0:
#         print(summ / count)
#         break
#     else:
#         summ += number
#         count += 1
# -------------------------------------------------------------


# for i in range(0, 101, 10):
#     print(f'{i}(C) = {i * 1.8 + 32}(F)')
# -------------------------------------------------------------

# text = input('Enter text: ')
# print(text == text[::-1])
# -------------------------------------------------------------

# binary_code = input('Enter bin code: ')
# binary_code = binary_code[::-1]
# number = 0
# for i in range(len(binary_code)):
#     number += 2 ** i * int(binary_code[i])
# print(number)
# -------------------------------------------------------------


# import random

# first_number = random.randint(1, 100)
# print(first_number)
# for i in range(99):
#     number = random.randint(1, 100)
#     if number > first_number:
#         print(number, 'update')
#         first_number = number
#     else:
#         print(number)
# -------------------------------------------------------------


# n = int(input('Enter n:  '))
# m = int(input('Enter m:  '))
# d = min(n, m)
# while n % d != 0 or m % d != 0:
#     d -= 1
# print(d)
# -------------------------------------------------------------


# text = 'hello'
# text = text.replace(' ', '')
# print(text)
# -------------------------------------------------------------

# text = 'flee to me remote elf'
# text = text.replace(' ', '')
# print(text == text[::-1])
# -------------------------------------------------------------
