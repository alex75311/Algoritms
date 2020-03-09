# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

from timeit import timeit


# Вариант 1
def var1(n):
    summ = 0
    x = 1
    while n != 0:
        summ += x
        x /= -2
        n -= 1
    return summ


# Вариант 2
def var2(n, x=1):
    if n == 1:
        return x
    else:
        result = x + var2(n - 1, x / -2)
        return result


# Вариант 3
def var3(n):
    item = 1
    sum_ = 0
    for _ in range(n):
        sum_ += item
        item /= -2
    return sum_


print(timeit('var1(100)', number=10000, globals=globals()))  # 0.08788623699999999
print(timeit('var1(200)', number=10000, globals=globals()))  # 0.16495976599999998
print(timeit('var1(400)', number=10000, globals=globals()))  # 0.342664448
print()
print(timeit('var2(100)', number=10000, globals=globals()))  # 0.15363887499999995
print(timeit('var2(200)', number=10000, globals=globals()))  # 0.3251030400000001
print(timeit('var2(400)', number=10000, globals=globals()))  # 0.7196057149999999
print()
print(timeit('var3(100)', number=10000, globals=globals()))  # 0.0574443189999998
print(timeit('var3(200)', number=10000, globals=globals()))  # 0.10755256000000002
print(timeit('var3(400)', number=10000, globals=globals()))  # 0.23634859500000016

'''
Вывод: оптимальным решением является Вариант 3
Сложность всех алгоритмов O(n)
'''
