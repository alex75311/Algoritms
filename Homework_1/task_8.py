# https://drive.google.com/file/d/1JhQRvziVMSIath2DxW8N1sEVlsL4ByTg/view?usp=sharing
# Определить, является ли год, который ввел пользователь, високосным или не високосным.
# Примечания:
# 1. Во всех заданиях, где речь идёт о буквах алфавита, решения необходимы только для строчных букв латинского
# алфавита от a до z.
# 2. Попытайтесь решить задания без использования циклов и собственных функций (они будут рассматриваться на уроке 2),
# а также без массивов (они будут рассматриваться на уроке 3).
# Для простоты понимания зарезервированные слова for и while считаются циклом, def - функцией, любые квадратные скобки
# [ и ] - массивами. Их наличие в коде расценивается как неверное решение.

year = int(input('Введите год '))
if year % 4 != 0:
    print('Год не високосный')
elif year % 100 == 0:
    if year % 400 == 0:
        print('Год високосный')
    else:
        print('Год не високосный')
else:
    print('Год високосный')
