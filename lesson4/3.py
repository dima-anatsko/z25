# Заполнить список вещественных чисел вводом с клавиатуры.
# Найте элементы списка, которые меньше среднего арифметического.

items = []
sum_items = 0
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
        sum_items += number
if items:
    means = []
    mean = sum_items / len(items)
    for item in items:
        if item < mean:
            means.append(item)
    if means:
        print('элементы списка, которые меньше ср. арифметического', means)
    else:
        print('список не содержит элементов, меньше ср. арифметического')
else:
    print('Список не содержит элементов!')
