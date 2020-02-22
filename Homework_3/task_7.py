# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.
# Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе
# написанных самостоятельно.

from random import randint

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100

arr = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Исходный массив')
print(arr)


def min_el(arr):
    result = MAX_ITEM
    for el in arr:
        if result > el:
            result = el
    return result


res1 = min_el(arr)
arr.remove(res1)
res2 = min_el(arr)
print(f'Два наименьших элемента {res1} и {res2}')
