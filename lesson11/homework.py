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
        while self._one <= self._number:
            temp = self._one
            self._one, self._two = self._two, self._two + self._one
            return temp
        raise StopIteration


"""
2.
Напишите класс, объектом которого будет итератор производящий только
чётные числа до n включительно.
"""


"""
3.
Напишите итератор factorials(n), генерирующий последовательность
факториалов натуральных чисел.
"""


"""
4.*
Напишите итератор BinomialCoefficients(n), генерирующий последовательность
биномиальных коэффициентов C0n,C1n,…,Cnn
Запрещается использовать факториалы.
"""


if __name__ == '__main__':
    c = Fibonacci(10)
    for i in c:
        print(i)
