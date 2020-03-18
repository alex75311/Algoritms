# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# ● написать 3 варианта кода (один у вас уже есть);
# ● проанализировать 3 варианта и выбрать оптимальный;
# ● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Задача поиска простого числа по его номеру без использования решета Эратосфена и с использованием

import sys
import math


def show(obj):
    sum_key = 0
    sum_value = 0
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                sum_key = sum_key + sys.getsizeof(key)
                print(f'type = {type(key)}, size = {sys.getsizeof(key)}, obj = {key}')
                sum_value = sum_value + sys.getsizeof(value)
                print(f'type = {type(value)}, size = {sys.getsizeof(value)}, obj = {value}')
            print(f'Память, занятая ссылками на переменные = {sum_key}')
            print(f'Память, занятая значениями переменных = {sum_value}')
        elif not isinstance(obj, str):
            for item in obj:
                show(item)
    print(f'Память, занятая функцией = {sys.getsizeof(obj)}')
    print(f'Всего занято памяти: {sys.getsizeof(obj) + sum_key + sum_value}')


def prime_1(num):
    count = 1
    current_prime = 2
    while count < num:
        current_prime += 1
        for i in range(2, int(current_prime ** 0.5) + 1):
            if current_prime % i == 0:
                break
        else:
            count += 1
    print(current_prime)
    return vars()


def prime_2(num):
    MULTIPLIER = 1.3
    size = int(num * math.log(num) * MULTIPLIER) if num > 10 else 30
    array = [True for _ in range(size)]
    array[:2] = [False, False]
    count = 0
    for i in range(2, size):
        if array[i]:
            count += 1
            if count == num:
                print(i)
                return vars()
            for j in range(i ** 2, size, i):
                array[j] = False


def prime_3(num):
    assert num <= 5761455, 'Слишком большой аргумент'
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1229: 10 ** 4,
               9592: 10 ** 5,
               78498: 10 ** 6,
               664579: 10 ** 7,
               5761455: 10 ** 8,
               }
    for key in pi_func:
        if num <= key:
            size = pi_func[key]
            break
    array = [i for i in range(size)]
    array[1] = 0
    for i in range(2, size):
        if array[i] != 0:
            j = i ** 2
            while j < size:
                array[j] = 0
                j += i
    res = [i for i in array if i != 0]
    print(res[num - 1])
    return vars()


num = 5000
show(prime_1(num))
print()
# Память, занятая ссылками на переменные = 122
# Память, занятая значениями переменных = 58
# Память, занятая функцией = 136
# Всего занято памяти: 316

show(prime_2(num))
print()
# Память, занятая ссылками на переменные = 204
# Память, занятая значениями переменных = 228772
# Память, занятая функцией = 204
# Всего занято памяти: 229180

show(prime_3(num))
# Память, занятая ссылками на переменные = 227
# Память, занятая значениями переменных = 451446
# Память, занятая функцией = 204
# Всего занято памяти: 451877

# Вывод: первый способ без использования Решета Эратосфена самый медленный, но и самый экономичный по памяти,
# последний самый быстрый, но и самый прожорливый.

# Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
# Win7 64bit
