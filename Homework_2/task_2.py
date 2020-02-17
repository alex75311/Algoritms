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
