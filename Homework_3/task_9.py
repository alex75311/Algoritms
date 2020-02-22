# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе
# написанных самостоятельно.

from random import randint

SIZE_X = 5
SIZE_Y = 20
MIN_ITEM = 0
MAX_ITEM = 100

arr = [[randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_X)] for _ in range(SIZE_Y)]
print('Исходный массив')
for i in range(SIZE_Y):
    print(arr[i], end='')
    print()

max_ = MIN_ITEM
res_arr = []
for y in range(SIZE_X):
    min_ = MAX_ITEM
    for x in range(SIZE_Y):
        if min_ > arr[x][y]:
            min_ = arr[x][y]
    res_arr.append(min_)

for el in res_arr:
    if max_ < el:
        max_ = el

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы равен {max_}')
