# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
# Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе
# написанных самостоятельно.

from random import randint

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100

summ = 0
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
print('Полученный массив')
if min_i > max_i:
    min_i, max_i = max_i, min_i
print(arr[min_i+1:max_i])
for i in range(min_i+1, max_i):
    summ += arr[i]
print(f'Сумма элементов {summ}')
