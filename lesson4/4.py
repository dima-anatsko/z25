# Перевести число, введенное пользователем,
# в байты или килобайты в зависимости от его выбора.

number, _byte = None, None
while number is None or _byte is None:
    try:
        if number is None:
            number = int(input('введите целое число в битах: '))
    except ValueError as exc:
        print(f'Ошибка: \033[31m{exc}\033[0m, повторите ввод')
    if _byte is None:
        _byte = input(
            'введите "b", для перевода в байты, или "k", в килобайты: ')
        if _byte != 'b' and _byte != 'k':
            print('Ошибка, введите "b" или "k"')
            _byte = None
result = number // 8 + 1 if number % 8 else number // 8
if _byte == 'b':
    print(f'{number} бит = {result} байт')
else:
    result = result // 1024 + 1 if result % 1024 else result // 1024
    print(f'{number} бит = {result} Кбайт')
