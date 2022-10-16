'''
Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''


# from itertools import accumulate
# import operator

# N = int(input('Введите число: '))


# def get_prods(N):
#     return list(accumulate([x for x in range(1, N + 1)], operator.mul))

# print(get_prods(N))

'''
Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
'''

# print("x | y | z | ¬(X ∧ Y) ∨ Z")
# for x in range (0, 2):
#     for y in range (0, 2):
#         for z in range (0, 2):
#             print(f"{x} | {y} | {z} | {int(not(x and y) or z)}")

'''
Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
«one» «onetwonine» - o – 2, n – 3, e – 2
'''

# print("Введите првую строку")
# string_1 = input()
# print("Введите вторую строку")
# string_2 = input()
# for i in range (len(string_1)):
#     count = 0
#     for j in range (len(string_2)):
#         if (string_1[i] == string_2[j]):
#             count +=1
#     print(f"{string_1[i]} - {count}")

'''
Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
3 -> [2, 3, -3, -2, -1, 0, 1]
'''

# print("Введите число N больше 0")
# n = int(input())
# print(f"{n-1}, {n}, ", end = "")
# for i in range(n*2-2):
#     print(f"{-n+i}, ", end = "")
# print(n-2)
    