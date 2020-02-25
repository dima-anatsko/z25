"""
1.
Напишите итератор Fibonacci(n), который генерирует числа Фибоначчи до
n включительно.
"""


class Fibonacci:
    def __init__(self, number):
        self._one, self._two = 0, 1
        self._number = number

    def __iter__(self):
        return self

    def __next__(self):
        if self._one <= self._number:
            temp = self._one
            self._one, self._two = self._two, self._two + self._one
            return temp
        raise StopIteration


"""
2.
Напишите класс, объектом которого будет итератор производящий только
чётные числа до n включительно.
"""


class EvenNumber:
    def __init__(self, number):
        self._number = number
        self._start = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._start += 2
        if self._start <= self._number:
            return self._start
        raise StopIteration


"""
3.
Напишите итератор factorials(n), генерирующий последовательность
факториалов натуральных чисел.
"""


class Factorials:
    def __init__(self, number):
        self._number = number
        self._start = 1
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._number:
            self._start *= self._next
            self._next += 1
            self._number -= 1
            return self._start
        raise StopIteration


"""
4.*
Напишите итератор BinomialCoefficients(n), генерирующий последовательность
биномиальных коэффициентов C0n,C1n,…,Cnn
Запрещается использовать факториалы.
"""


class BinomialCoefficients:
    def __init__(self, n):
        self._n = n
        self._k = 0
        self._res = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._k == 0:
            self._k += 1
            return self._res
        elif self._k <= self._n:
            self._res = int(((self._n - self._k + 1) / self._k) * self._res)
            self._k += 1
            return self._res
        raise StopIteration
