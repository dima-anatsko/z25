# Вводятся два целых числа.
# Проверить делится ли первое на второе.
# Вывести на экран сообщение об этом, а также остаток (если он есть)
# и частное (в любом случае).

dividend, divisor = None, None
while dividend is None or divisor is None:
    try:
        if dividend is None:
            dividend = int(input('введите целое делимое число: '))
        if divisor is None:
            divisor = int(input('введите целое число делитель: '))
    except ValueError as exc:
        print(f'Ошибка: \033[31m{exc}\033[0m, повторите ввод')
if divisor:
    print('Первое число делится на второе')
    remains = dividend % divisor
    if remains:
        print('Остаток от деления =', remains)
    print(dividend, '/', divisor, '=', dividend / divisor)
else:
    print('Деление на ноль')
