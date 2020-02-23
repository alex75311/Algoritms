# https://drive.google.com/file/d/1aDoOlVjwWrMfFt_Xk38XNJsqyyiZR1MD/view?usp=sharing
# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


def func(n):
    if n == 1:
        return 1
    else:
        result = n + func(n - 1)
    return result


n = int(input('Введите n '))
x = n * (n + 1) / 2
y = func(n)
if x == y:
    print('Формула 1+2+...+n = n(n+1)/2 подтвердилась')
else:
    print('Формула 1+2+...+n = n(n+1)/2 не подтвердилась')
