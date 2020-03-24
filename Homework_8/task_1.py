# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9

import hashlib

s = input('Введите строку: ')


def substrings_counter(s):
    hash_list = []
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] != '' and s[i:j] != s:
                hash_list.append(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
                count += 1

    for i in range(len(hash_list) - 1):
        for j in range(i + 1, len(hash_list)):
            if hash_list[i] == hash_list[j]:
                count -= 1

    print(f'Сумма подстрок: {count}')


substrings_counter(s)
