'''
Day 8 
Unit Test
'''

import unittest
from div import floordiv 

class TestDivMethods(unittest.TestCase):
    def test_div_asserts_proper_value(self):
        self.assertEqual(floordiv(4,2), 2)

    def test_div_asserts_zero(self):
        self.assertEqual(floordiv(2,4), 0)

    def test_div_asserts_integer_and_not_float(self):
        self.assertEqual(floordiv(10,3), 3)

    def test_div_asserts_one(self):
        self.assertEqual(floordiv(3,3), 1)    


if __name__ == '__main__':
    unittest.main()