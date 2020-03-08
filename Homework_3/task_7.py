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


# Вариант 1
min_first, min_second = (0, 1) if arr[0] < arr[1] else (1, 0)
for i in range(2, len(arr)):
    if arr[i] < arr[min_first]:
        spam = min_first
        min_first = i
        if arr[spam] < arr[min_second]:
            min_second = spam

    elif arr[i] < arr[min_second]:
        min_second = i

print(f'Число {arr[min_first]} в ячейке {min_first}')
print(f'Число {arr[min_second]} в ячейке {min_second}')


# Вариант 2
def min_el(arr):
    result = float('inf')
    for el in arr:
        if result > el:
            result = el
    return result


res1 = min_el(arr)
arr.remove(res1)
res2 = min_el(arr)
print(f'Два наименьших элемента {res1} и {res2}')
