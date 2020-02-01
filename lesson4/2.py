# Заполнить список вещественных чисел вводом с клавиатуры.
# Сколько элементов списка больше по модулю максимального числа.

items = []
max_item = None
col = 0
while True:
    number = input('введите число: ')
    if not number:
        break
    try:
        number = float(number)
    except ValueError:
        print('Это не число, повторите ввод.')
    else:
        items.append(number)
        if max_item is None or number > max_item:
            max_item = number
if items:
    for item in items:
        col = col + 1 if abs(item) > max_item else col
    print('Кол-во чисел в списке больших по модулю чем максимальное =', col)
else:
    print('Список не содержит элементов!')
