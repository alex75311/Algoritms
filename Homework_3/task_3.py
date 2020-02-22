# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе
# написанных самостоятельно.

from random import randint

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100

arr = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Исходный массив')
print(arr)
min_el = max_el = arr[0]
min_i = max_i = 0
for i, el in enumerate(arr):
    if min_el > el:
        min_el = el
        min_i = i
    if max_el < el:
        max_el = el
        max_i = i
arr[min_i], arr[max_i] = arr[max_i], arr[min_i]
print('Полученный массив')
print(arr)
