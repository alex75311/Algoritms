# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии
# сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

from random import randint


def bubble_sort(array):
    stop = len(array) - 1
    while stop > 0:
        trigger = True
        for i in range(stop):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                trigger = False
        stop -= 1
        print(array, trigger)
        if trigger:
            break
    return array


arr = [randint(-100, 99) for _ in range(10)]
print(f'Исходный массив {arr} \nОтсортированный массив {bubble_sort(arr)}')
