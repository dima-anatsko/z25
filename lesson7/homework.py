import time
import re

"""1. Написать кэширующий декоратор,
который принимает время (в секундах, сколько необюходимо хранить результат)

@cache(60)  # значит что результат функции foo будет хранится 60 секунд
def foo():
    pass
"""


def cache(_time):
    def inner(func):
        def decorator(*args, **kwargs):
            cache._cache = getattr(cache, '_cache', {})
            _key = (args, tuple(sorted(kwargs.items(), key=lambda i: i[0])))
            result, time_cache = cache._cache.get(_key, (None, None))
            if result is None or time.time() - time_cache > _time:
                result, time_cache = func(*args, **kwargs), time.time()
                cache._cache[_key] = result, time_cache
            return result

        return decorator

    return inner


@cache(10)
def func(seconds):
    time.sleep(seconds)
    print(seconds)
    return seconds


@cache(10)
def func_diff(seconds):
    time.sleep(seconds)
    print(seconds)
    return seconds - 1 if seconds > 3 else 2


"""
2.
Написать декоратор, который считает сколько раз была вызвана функция и выводит
эту информации на экран.
В качестве аргумента(необязательного) декоратор может принимать
текст(форматированный), который
будет выводиться вместе с количеством вызовов. Если данный аргумент не передан,
то выводить текст по умолучанию(любой)
@counter():
def foo():
    return 1
foo(123)
>>> 'Count - 1'
>>> 1
foo("asd")
>>> 'Count - 2'
>>> 1
@counter("Text {}"):
def foo1():
    return 1
>>> 'Text 1'
>>> 1
"""


def counter(text='Count - {}'):
    def inner(func):
        def decorator(*args, **kwargs):
            counter._count = getattr(counter, '_count', {})
            _name = func.__name__
            counter._count[_name] = counter._count.get(_name, 0) + 1
            result = func(*args, **kwargs)
            print(text.format(counter._count[_name]))
            return result

        return decorator

    return inner


@counter()
def foo():
    return 1


@counter("foo1 = {}")
def foo1():
    return 1


"""
3.
Написать функцию, которая извлекает даты из строки.'
Допускаем что во всех месяцах 31 день
get_datetimes('Lorem Ipsum is simply 12-01-2018 dummy text of
the printing 10-13-2018 and typesetting industry.
10-02-2018 Lorem Ipsum has been the industry a s x')
>>> ['12-01-2018', '10-02-2018']
"""


def get_datetimes(string):
    pattern = re.compile(
        r'((?:(?:0\d)|(?:1[0-2]))-(?:(?:[0-2]\d)|(?:3[0,1]))-\d{4})')
    return pattern.findall(string)


"""
4.
Написать функцию, которая извлекает все слова,
начинающиеся на гласную(согласную). Какие слова извлекать - аргумент функции
get_words('Lorem Ipsum is simply', sym=('consonants', 'vowels'))
>>> ['Lorem', 'Ipsum', 'is', 'simply']
get_words('Lorem Ipsum is simply', sym=('consonants',))
>>> ['Lorem', 'sumply']
get_words('Lorem Ipsum is simply', sym=('vowels',))
>>> ['Ipsum', 'is']
"""


def get_words(string, sym=('consonants', 'vowels')):
    if sym == ('consonants',):
        pattern = re.compile(r'\b[qwrtpsdfghklzxcvbnm]\w*', flags=re.I)
    elif sym == ('vowels',):
        pattern = re.compile(r'\b[aeyuio]\w*', flags=re.I)
    else:
        pattern = re.compile(r'\b[a-zA-Z]\w*')
    return pattern.findall(string)


"""
5. Написать функцию, которая группирует результат команды ping
((<icmp_seq>, <ttl>), ...)
s = "64 bytes from 216.58.215.110: icmp_seq=0 ttl=54 time=30.391 ms
64 bytes from 216.58.215.110: icmp_seq=1 ttl=54 time=30.667 ms
64 bytes from 216.58.215.110: icmp_seq=2 ttl=54 time=33.201 ms
64 bytes from 216.58.215.110: icmp_seq=3 ttl=54 time=30.140 ms
64 bytes from 216.58.215.110: icmp_seq=4 ttl=54 time=31.822 ms"
get_result(s)
>>> ((0, 30.391), (1, 30.667), (2, 33.201), (3, 30.140), (4, 31.822))
"""


def get_ping_info(*args, **kwargs):
    pass


if __name__ == "__main__":
    timer = time.time()
    print(func(func(func(func(5)))))
    assert time.time() - timer < 10
    timer = time.time()
    print(func_diff(func_diff(func_diff(func_diff(func_diff(3))))))
    assert time.time() - timer < 10
    print('cache - ok')
    foo()
    foo()
    foo1()
    foo()
    foo1()
    print('count - ok')
    str_one = '''Lorem Ipsum is simply 12-01-2018 dummy text of the printing
     10-13-2018 and typesetting industry. 10-02-2018 Lorem Ipsum has been
     the industry a s x'''
    str_two = '''
    With the support of the Communist Party, the country's name was changed
    to the Republic of Belarus on 08-25-1991.[85] Stanislav Shushkevich,
    the chairman of the Supreme Soviet of Belarus, met with Boris Yeltsin of
    Russia and Leonid Kravchuk of Ukraine on 12-08-1991 in Belavezhskaya
    Pushcha to formally declare the dissolution of the Soviet Union and the
    formation of the Commonwealth of Independent States.[85]
    '''
    assert get_datetimes(str_one) == ['12-01-2018', '10-13-2018', '10-02-2018']
    assert get_datetimes(str_two) == ['08-25-1991', '12-08-1991']
    print('get_datetimes - ok')
    text = 'Lorem Ipsum is simply'
    assert get_words(text, ('vowels',)) == ['Ipsum', 'is']
    assert get_words(text, sym=('consonants',)) == ['Lorem', 'simply']
    assert get_words(text) == ['Lorem', 'Ipsum', 'is', 'simply']
    print('get_words - ok')
