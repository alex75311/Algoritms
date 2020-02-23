# https://drive.google.com/file/d/1aDoOlVjwWrMfFt_Xk38XNJsqyyiZR1MD/view?usp=sharing
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.


summ = 0
x = 1
n = int(input('Введите n '))
while n != 0:
    summ += x
    x /= -2
    n -= 1
print(summ)
