# https://drive.google.com/file/d/1aDoOlVjwWrMfFt_Xk38XNJsqyyiZR1MD/view?usp=sharing
# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


x = 32
k = 0
while x < 127:
    while k < 10:
        print(f'{x}={chr(x)} ', end='')
        k += 1
        x += 1
        if x > 127:
            break
    k = 0
    print('\r')
