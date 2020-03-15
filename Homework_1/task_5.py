# https://drive.google.com/file/d/1JhQRvziVMSIath2DxW8N1sEVlsL4ByTg/view?usp=sharing
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
# Примечания:
# 1. Во всех заданиях, где речь идёт о буквах алфавита, решения необходимы только для строчных букв латинского
# алфавита от a до z.
# 2. Попытайтесь решить задания без использования циклов и собственных функций (они будут рассматриваться на уроке 2),
# а также без массивов (они будут рассматриваться на уроке 3).
# Для простоты понимания зарезервированные слова for и while считаются циклом, def - функцией, любые квадратные скобки
# [ и ] - массивами. Их наличие в коде расценивается как неверное решение.

FIRST_KOD = 96
print('Введите две разные строчные английские буквы')
first = input('Первая буква ')
second = input('Вторая буква ')
ch1 = ord(first) - FIRST_KOD
ch2 = ord(second) - FIRST_KOD
print(f'Первая буква находится на {ch1} месте')
print(f'Вторая буква находится на {ch2} месте')
if ch1 > ch2:
    col = ch1 - ch2 - 1
else:
    col = ch2 - ch1 - 1
print(f'Количество букв между ними {col}')