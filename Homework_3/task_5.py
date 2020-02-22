# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
# Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе
# написанных самостоятельно.

from random import randint

SIZE = 20
MIN_ITEM = -100
MAX_ITEM = 100

arr = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Исходный массив')
print(arr)
res = {i: el for i, el in enumerate(arr) if el < 0}
result = MIN_ITEM
for i, el in res.items():
    if result < el:
        result = el
        result_i = i
print(f'Максимальный отрицательный элемент находится под индексом {result_i} равен {result}')
