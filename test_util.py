import unittest

from utils import bracket


class Utils(unittest.TestCase):
    def test_max_bracket(self):
        speed = 12
        speed = bracket(speed, -10, 10)
        self.assertEqual(10, speed)

    def test_other_max_bracket(self):
        speed = 12
        speed = bracket(speed, -11, 11)
        self.assertEqual(11, speed)

    def test_min_bracket(self):
        speed = -12
        speed = bracket(-12, -10, 10)
        self.assertEqual(-10, speed)

    def test_within_brackets(self):
        speed = 8
        speed = bracket(speed, -10, 10)
        self.assertEqual(8, speed)


if __name__ == '__main__':
    unittest.main()
