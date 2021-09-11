import unittest
from exam import TimeUI

time_ui = TimeUI()

class TestStringMethods(unittest.TestCase):

    def test_is_equal(self):
        self.assertEqual(time_ui.return_string(), 'abc')

    def test_is_digit(self):
        self.assertFalse(time_ui.return_string().isdigit())

if __name__ == '__main__':
    unittest.main()