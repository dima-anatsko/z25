"""
Ex1
Это простое упражнение на использование упаковок.
Определите функцию print_given, которая для каждого переданного аргумента
будет распечатывать на отдельной строке через пробел имя аргумента
(если таковое имеется),
значение аргумента, тип аргумента.

Аргументы без имени должны быть распечатаны раньше именованных.
Порядок печати аргументов без имени важен: он должен совпадать с порядком,
в котором аргументы передаются. Порядок печати аргументов с именем неважен.

Пример:
print_given(1, 2, 3, [1, 2, 3], "one", "two", "three", two = 2, one = 1)
>>> 1 <class "int">
2 <class "int">
3 <class "int">
[1, 2, 3] <class "list">
one <class "str">
two <class "str">
three <class "str">
one 1 <class "int">
two 2 <class "int">

print_given()
"""


def print_given(*args, **kwargs):
    string = ''
    for item in args:
        string += f'{item} {type(item)}\n'
    for key in kwargs:
        string += f'{key} {kwargs[key]} {type(kwargs[key])}\n'
    print(string)
    return string


"""
Ex2
Написать функцию sort_by_abc,
на вход которой подаётся некоторое количество (не больше сотни)
разделённых пробелом целых чисел (каждое не меньше 0 и не больше 19).

Функция должна вернуть список в порядке лексикографического возрастания
названий этих чисел в английском языке.

Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2,
поскольку слово two в словаре встречается позже слова three,
а слово three -- позже слова one (иначе говоря, поскольку
выражение "one" < "three" < "two" является истинным)

Пример:
Sample Input:
[0, 1, 1, 2, 3, 5, 8, 13]
Sample Output:
[8, 5, 1, 1, 13, 3, 2, 0]

Использовать
number_names = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve",
        13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen",  18: "eighteen", 19: "nineteen"}
"""


def sort_by_abc(string):
    number_names = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve",
        13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen", 18: "eighteen", 19: "nineteen"}
    return sorted(map(int, string.split()), key=lambda x: number_names[x])


"""
Ex3
Напишите функцию composition(f, g), которая принимает на вход две
функции: f и g, -- и возвращает их композицию.

Не вдаваясь в лишние сейчас детали,  назовём композицией 𝑓∘𝑔 двух
заданных функций 𝑓, 𝑔 функцию ℎ, для которой

  ℎ(𝑥)=𝑓(𝑔(𝑥))

Определите функцию композиции, предполагая, что аргументы
у функции g могут быть какие угодно,
и любое возвращаемое функцией g значение будет
корректным аргументом для функции f.

Примеры:
h = composition(lambda x: x**2, lambda x: x + 1)
print(h(5))

>>> 36


h = composition(lambda x: x, composition(lambda x: x**2, lambda x: x + 1))
print(h(5))

>>> 36


h = composition(sum, lambda x, y, z: (x**2, y**3, z**4))
print(h(2, 3, 9))

>>> 6592
"""


def composition(func_1, func_2):
    def decorator(*args, **kwargs):
        return func_1(func_2(*args, **kwargs))
    return decorator


def my_add(number):
    return number + 1


def my_square(number):
    return number ** 2


def my_degree(*args):
    return map(lambda x: x[1] ** x[0], enumerate(args, 2))


"""
Ex4
Напишите декоратор flip, который делает так, что задекорированная функция
принимает все свои неименованные аргументы в порядке, обратном тому,
в котором их передали (для аргументов с именем не вполне правильно
учитывать порядок, в котором они были переданы)

Пример:
@flip
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res


div(2, 4, show=True)
>>> 2.0
"""


def flip(func):
    def decorator(*args, **kwargs):
        args = args[::-1]
        return func(*args, **kwargs)
    return decorator


@flip
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res


@flip
def diff(x, y, show=False):
    if show:
        print(x - y)
    return x - y


@flip
def my_print(*args):
    return ''.join(args)


"""
Ex5
Напишите декоратор introduce_on_debug, который
делает так, что задекорированная функция печатает своё имя
при вызове, но только если переменная debug имеет значение True.

Пример:
@introduce_on_debug(debug=False)
def identity(x):
    return x

identity(239)
>>> 239

@introduce_on_debug(debug=True)
def identity(x):
    return x

identity(57)
>>> identity
57
"""


def introduce_on_debug(debug=False):
    def inner(func):
        def decorator(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'{func.__name__}\n{result}' if debug else f'{result}'
        return decorator
    return inner


@introduce_on_debug(debug=True)
def identity_1(x):
    return x


@introduce_on_debug(debug=False)
def identity_2(x):
    return x


"""
Ex6
Напишите декоратор timer, который выводит время выполнения функции в секундах
"""


def timer(func):
    from datetime import datetime

    def decorator(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        time = datetime.timestamp(end) - datetime.timestamp(start)
        return result, time
    return decorator


@timer
def max_number_count_dict(number):
    _list = list(range(number))
    counter = {}
    for item in _list:
        counter[item] = counter.get(item, 0) + 1
    return max(counter.items(), key=lambda x: x[1])


@timer
def max_number_count_list(number):
    _list = list(range(number))
    return max({i: _list.count(i) for i in _list}.items(), key=lambda x: x[1])


if __name__ == "__main__":
    assert print_given(1, 2, '10') == "1 <class \'int\'>\n" + \
        "2 <class \'int\'>\n" + \
        "10 <class \'str\'>\n"
    assert print_given(a=1, b=(2, 4), vas=[28]) == "a 1 <class \'int\'>\n" + \
        "b (2, 4) <class \'tuple\'>\n" + \
        "vas [28] <class \'list\'>\n"
    assert print_given(1, 2, 3, [1, 2, 3], "one", "two", "three", two=2,
                       one=1) == "1 <class \'int\'>\n2 <class \'int\'>\n" + \
        "3 <class \'int\'>\n[1, 2, 3] <class \'list\'>\n" + \
        "one <class \'str\'>\ntwo <class \'str\'>\nthree <class \'str\'>\n" + \
        "two 2 <class \'int\'>\none 1 <class \'int\'>\n"
    print('print_given - OK')
    assert sort_by_abc('0 1 1 2 3 5 8 13') == [8, 5, 1, 1, 13, 3, 2, 0]
    assert sort_by_abc('18 8 12 2 13 6 4 1') == [8, 18, 4, 1, 6, 13, 12, 2]
    assert sort_by_abc('18 8 13 3 16 6 19 9') == [8, 18, 9, 19, 6, 16, 13, 3]
    print('sort_by_abc - OK')
    assert composition(sum, my_degree)(2, 3, 9) == 6592
    assert composition(lambda x: x**2, lambda x: x + 1)(5) == 36
    assert composition(my_square, my_add)(6) == 49
    assert composition(lambda x: x, composition(my_square, my_add))(5) == 36
    print('composition - OK')
    assert div(2, 4, show=False) == 2.0
    assert diff(2, 4, show=False) == 2
    assert my_print('world!', 'Hello, ', 'Vasja! ') == 'Vasja! Hello, world!'
    print('flip - OK')
    assert identity_1(45) == "identity_1\n45"
    assert identity_2(33) == "33"
    print('introduce_on_debug - OK')
    print(max_number_count_dict(100000))  # 0.02s
    print(max_number_count_list(100000))  # 96.47s
