# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

from random import randint


def median(arr):
    for i in range(len(arr)):
        left = right = center = 0
        for j in range(len(arr)):
            if i != j:
                if arr[i] > arr[j]:
                    left += 1
                elif arr[i] < arr[j]:
                    right += 1
                else:
                    center += 1
        if left == right or left + center == right or left == right + center or center - (
                abs(m - left) + abs(m - right)) == 0:
            return arr[i]


m = int(input('Введите m '))
array = [randint(0, 10) for _ in range(2 * m + 1)]
print(f'Исходный массив {array}')
print(f'Отсортированный массив {sorted(array)}')
print(f'Медиана {median(array)}')
