import unittest
from homework import Fibonacci, EvenNumber, Factorials, BinomialCoefficients


class HomeworkTest(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(list(Fibonacci(21)), [0, 1, 1, 2, 3, 5, 8, 13, 21])
        self.assertEqual(list(Fibonacci(10)), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(list(Fibonacci(1)), [0, 1, 1])
        a = Fibonacci(1)
        next(a)
        next(a)
        next(a)
        with self.assertRaises(StopIteration):
            next(a)

    def test_even_number(self):
        self.assertEqual(list(EvenNumber(11)), [2, 4, 6, 8, 10])
        self.assertEqual(list(EvenNumber(10)), [2, 4, 6, 8, 10])
        self.assertEqual(list(EvenNumber(2)), [2])
        n = EvenNumber(2)
        next(n)
        with self.assertRaises(StopIteration):
            next(n)

    def test_factorials(self):
        self.assertEqual(list(Factorials(5)), [1, 2, 6, 24, 120])
        self.assertEqual(list(Factorials(7)), [1, 2, 6, 24, 120, 720, 5040])
        self.assertEqual(list(Factorials(1)), [1])
        n = Factorials(1)
        next(n)
        with self.assertRaises(StopIteration):
            next(n)

    def test_binomial_coefficients(self):
        self.assertEqual(list(BinomialCoefficients(2)), [1, 2, 1])
        self.assertEqual(list(BinomialCoefficients(3)), [1, 3, 3, 1])
        self.assertEqual(list(BinomialCoefficients(5)), [1, 5, 10, 10, 5, 1])
        n = BinomialCoefficients(0)
        next(n)
        with self.assertRaises(StopIteration):
            next(n)


if __name__ == '__main__':
    unittest.main()
