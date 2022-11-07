from main import fibonacci_3 as fibonacci
import unittest


class TestFibonacci_3(unittest.TestCase):

    def test_fibonacci_1_is_1(self):
        self.assertEqual(1, fibonacci(1))

    def test_fibonacci_9_is_34(self):
        self.assertEqual(34, fibonacci(9))

    def test_fibonacci_(self):
        with self.assertRaises(ValueError):
            fibonacci(-10)


if __name__ == "__main__":
    unittest.main()
