import unittest
from Lob1.src.scripts.sublob1.mystr_01 import  MyString1

class MyTestCase1(unittest.TestCase):
    def test_something(self):
        my_str = MyString1('ravi')
        self.assertEqual(my_str.check_len(), 4)  # add assertion here

