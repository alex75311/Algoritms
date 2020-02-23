# https://drive.google.com/file/d/1aDoOlVjwWrMfFt_Xk38XNJsqyyiZR1MD/view?usp=sharing
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.


def summ(n, x=1):
    if n == 1:
        return x
    else:
        result = x + summ(n - 1, x / -2)
        return result


n = int(input('Введите n '))
result = summ(n)
print(result)
