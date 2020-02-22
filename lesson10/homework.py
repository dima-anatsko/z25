import time

"""
0. (*) Написать функцию, которая из списка чисел составляет
максимальное число
[98, 9, 34] -> 99834
"""


def max_number(_list):
    res = None
    if _list:
        max_bit = len(str(max(_list)))
        _list = list(map(str, _list))
        _dict = {i: i + i[-1] * (max_bit - len(i)) for i in _list}
        res = int(''.join(sorted(_list, key=lambda x: _dict[x], reverse=True)))
    return res


"""
1.
Напишите менеджер контекста MultiFileOpen, который позволяет работать с
несколькими файлами:
MultiFileOpen(('file1.txt', 'r'), ('file2.txt', 'w'), ..., ('fileN.txt', 'rb'))
"""


class MultiFileOpen:
    def __init__(self, *args):
        self._args = args
        self._open = {}

    def __enter__(self):
        self._open = {item: open(*item) for item in self._args}
        return self._open

    def __exit__(self, exc_type, exc_val, exc_tb):
        for key in self._open:
            self._open[key].close()
        if exc_val:
            raise


"""
2.
Напишите менеджер контекста Timer, который позволяет получать текущее время
выполнения кода (отсчет начинается с конструкции with):
with Timer("Time: {}") as timer:
    do_some_logic()
    print(timer.now())  # Time: 3.4123 sec
    do_some_other_logic()
    print(timer.now())  # Time: 5.71 sec
"""


class Timer:
    def __init__(self, string):
        self._string = f'{string} sec'
        self._start = None

    def __enter__(self):
        self._start = time.time()
        return self

    def now(self):
        return self._string.format(time.time() - self._start)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    assert max_number([234, 123, 98]) == 98234123
    assert max_number([1, 2, 3, 4]) == 4321
    assert max_number([]) is None
    assert max_number([98, 9, 34]) == 99834
    print('max_number - OK')
    with MultiFileOpen(('file1.txt', 'r'), ('file2.txt', 'w')) as file:
        file[('file2.txt', 'w')].write(file[('file1.txt', 'r')].read())
    with Timer("Time: {}") as timer:
        time.sleep(2)
        print(timer.now())
        time.sleep(1)
        print(timer.now())
