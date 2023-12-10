import unittest


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


class FibonacciTestCase(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_valid_input(self):
        result = self.fibonacci(5)
        self.assertEqual(result, 5)

    def test_large_input(self):
        result = self.fibonacci(10)
        self.assertEqual(result, 55)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci(-1)

    def test_string_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci("abc")

    def test_float_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci(3.14)

    def test_zero_input(self):
        result = self.fibonacci(0)
        self.assertEqual(result, 0)

    def test_cached_results(self):
        self.fibonacci(5)
        self.fibonacci(7)

        self.assertEqual(self.fibonacci(5), 5)
        self.assertEqual(self.fibonacci(7), 13)


if __name__ == '__main__':
    unittest.main()

