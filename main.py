# Работа в классе
# Задача 17
# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# num = 0
# count = 0
# for i in list_1:
#     if i != num:
#         count+=1
#         num = i
# print(count)

# 2 способ
# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(list_1))) 

# Задача 19
# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

# list_2 = [1, 2, 3, 4, 5]
# k = int(input("Введите k: "))
# print(f"{list_2[len(list_2)-k:len(list_2)]} {list_2[:len(list_2)-k]}")

# lst = [1, 2, 3, 4, 5]
# k = int(input('Введите k: '))
# for i in range(k):
#     lst.insert(0, lst.pop(-1))
# print(lst)

# Задача 21
# Напишите программу для печати всех уникальных 
# значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# dictionary_uniq = []
# for i in dictionary:
#      for val in list(i.values()):
#         # val = ["S001"; "S00f1"]
#         if val not in dictionary_uniq:
#             dictionary_uniq.append(val)
# print(dictionary_uniq)

# Задача 23
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# list_4 = [0, -1, 5, 2, 3]
# n = len(list_4)
# count = 0

# for i in range(n - 1):
#     if list_4[i+1] > list_4[i]:
#         count += 1

# print(f'{count}')


# ДОМАШНЕЕ ЗАДАНИЕ

# Задача 16
# import random
# list_1 = []
# k = int(input("Введите размер массива: "))
# for i in range(k):
#     n = random.randint(1, 6)
#     list_1.append(n)
# print(list_1)
# num = int(input("Введите элемент "))
# count = 0
# for j in list_1:
#     if num == j:
#         count+=1
# print(count)

# Задача 18
# import random
# list_1 = []
# k = int(input("Введите размер массива: "))
# for i in range(k):
#     n = random.randint(1, 5)
#     list_1.append(n)
# print(list_1)
# num = int(input("Введите число "))
# difference = 9999
# for i in list_1:
#     x = abs(num - i)
#     if x <= difference:
#         difference = x
# print(difference)

# Задача 20
n = input("Введите строку: ")
letters = {1 : set("авеинорст"),
           2 : set("дклмпу"),
           3 : set("бгёья"),
           4 : set("йы"),
           5 : set("жзхцч"),
           6 : set("шэю"),
           7 : set("фщъ")
           }
count = 0
for i in n:
    for k in letters:
        if i in letters[k]:
            count+=k
print(count)