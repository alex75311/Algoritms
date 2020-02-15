# https://drive.google.com/file/d/1JhQRvziVMSIath2DxW8N1sEVlsL4ByTg/view?usp=sharing
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# Примечания:
# 1. Во всех заданиях, где речь идёт о буквах алфавита, решения необходимы только для строчных букв латинского
# алфавита от a до z.
# 2. Попытайтесь решить задания без использования циклов и собственных функций (они будут рассматриваться на уроке 2),
# а также без массивов (они будут рассматриваться на уроке 3).
# Для простоты понимания зарезервированные слова for и while считаются циклом, def - функцией, любые квадратные скобки
# [ и ] - массивами. Их наличие в коде расценивается как неверное решение.


print('Введите 3 разных числа через пробел ')
a, b, c = map(int, input().split(' '))
if a > b and a < c: print(f'Среднее число {a}')
elif a > c and a < b: print(f'Среднее число {a}')
elif b > a and b < c: print(f'Среднее число {b}')
elif b > c and b < a: print(f'Среднее число {b}')
else: print(f'Среднее число {c}')
