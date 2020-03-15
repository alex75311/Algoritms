# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается
# в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных
# функций для перевода из одной системы счисления в другую в данной задаче под запретом.

import collections

hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

num1 = input('Введите первое число ').upper()
num2 = input('Введите второе число ').upper()


def check_hex_num(spam):
    mem = spam // 16
    spam %= 16
    return spam, mem


def hex_sum(num1, num2):
    mem = 0
    num1 = collections.deque(num1)
    num2 = collections.deque(num2)
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    num1.reverse()
    num2.reverse()
    res = collections.deque()
    for i in range(len(num1)):
        if i < len(num2):
            spam = hex_list.index(num1[i]) + hex_list.index(num2[i]) + mem
        else:
            spam = hex_list.index(num1[i]) + mem
        spam, mem = check_hex_num(spam)
        res.appendleft(hex_list[spam])
    if mem == 1:
        res.appendleft('1')
    return ''.join(list(res))


def hex_multiplication(num1, num2):
    num1 = collections.deque(num1)
    num2 = collections.deque(num2)
    res = collections.deque()
    multiplier = 0
    if len(num1) > len(num2):
        num1, num2 = num2, num1
    num1.reverse()
    for i in range(len(num1)):
        multiplier += hex_list.index(num1[i]) * 16 ** i
    num1.reverse()
    for _ in range(multiplier):
        res = hex_sum(res, num2)
    if not res:
        return 0
    return res


print(f'Сумма равна {hex_sum(num1, num2)}')
print(f'Произведение равно {hex_multiplication(num1, num2)}')
