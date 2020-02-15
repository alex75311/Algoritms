x = int(input('Введите трехзначное число '))
summ = 0
proizv = 1

y = x % 10
summ += y
proizv *= y
x = x // 10

y = x % 10
summ += y
proizv *= y
x = x // 10

summ += x
proizv *= x

print(f'Сумма цифр равна {summ}')
print(f'Произведение цифр равно {proizv}')