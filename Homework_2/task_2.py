# https://drive.google.com/file/d/1aDoOlVjwWrMfFt_Xk38XNJsqyyiZR1MD/view?usp=sharing
# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


cht = ncht = 0
num = int(input('Введите натуральное число '))
while num % 10 != 0 or num // 10 != 0:
    x = num % 10
    num = num // 10
    if x % 2 == 0:
        cht += 1
    else:
        ncht += 1
print(f'Количество четных {cht}, количество нечетных {ncht}')
