# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
# вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

from timeit import timeit
import cProfile

n = 100


def sieve(k):
    global n
    a = [i for i in range(n + 1)]
    a[1] = 0
    lst = []
    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
        if len(lst) == k:
            return lst[-1]
    n *= 5
    return sieve(k)


def prime(k):
    lst = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
        if len(lst) == k:
            return lst[-1]


cProfile.run('sieve(100)')
cProfile.run('prime(100)')
# print(sieve(100))
# print(prime(100))
print(timeit('sieve(100)', number=100, globals=globals()))  # 0.040964150
print(timeit('sieve(200)', number=100, globals=globals()))  # 0.055681603
print(timeit('sieve(400)', number=100, globals=globals()))  # 0.223352655
print(timeit('sieve(800)', number=100, globals=globals()))  # 0.30342736

print(timeit('prime(100)', number=100, globals=globals()))  # 0.122445056
print(timeit('prime(200)', number=100, globals=globals()))  # 0.584289209
print(timeit('prime(400)', number=100, globals=globals()))  # 2.815240362
print(timeit('prime(800)', number=100, globals=globals()))  # 13.17652349

'''
Вывод:
сложность решета O(n log(log n))
сложность обычного алгоритма O(n**2)
Решето Эратосфена отрабатывает значительно быстрее
'''
