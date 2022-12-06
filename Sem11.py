# Задача 1. Постройте график функции: 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

import matplotlib.pyplot as plt

def task1():

    dot = list(5*i*i+10*i-30 for i in range(-20, 20))

    plt.plot(dot)
    plt.title("Задача 1")
    plotZero = list(0 for i in range(-50, 50))
    plt.plot(plotZero)

    plt.show()


# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

def task2():
    from random import randint
    dom = []
    a = {}
    print("Стоимость квадратного метра меньше 50000 рублей у домов номер:")
    for i in range(16):
            a[i] = int(randint(3000000, 20000000))/int(randint(100, 300))
            if (a[i] < 50000): print(i)
            dom.append(a[i])
    plt.plot(dom)
    plt.title("Задача 2")
    plotCondition = list(50000 for i in range(16))
    plt.plot(plotCondition)
    plt.show()


# ----------
K = int(input('Какую задачу проверим? '))
if K == 1:
    task1()
elif K == 2:
    task2()

else:
    print('Введено неверное значение.')