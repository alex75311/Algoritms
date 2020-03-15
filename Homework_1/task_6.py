# https://drive.google.com/file/d/1JhQRvziVMSIath2DxW8N1sEVlsL4ByTg/view?usp=sharing
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# Примечания:
# 1. Во всех заданиях, где речь идёт о буквах алфавита, решения необходимы только для строчных букв латинского
# алфавита от a до z.
# 2. Попытайтесь решить задания без использования циклов и собственных функций (они будут рассматриваться на уроке 2),
# а также без массивов (они будут рассматриваться на уроке 3).
# Для простоты понимания зарезервированные слова for и while считаются циклом, def - функцией, любые квадратные скобки
# [ и ] - массивами. Их наличие в коде расценивается как неверное решение.

ch = int(input('Введите номер буквы в алфавите '))
alpha = chr(ch + 96)
print('Это буква', alpha)