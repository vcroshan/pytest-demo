import unittest
from Lob1.src.scripts.sublob3.mystr_03 import MyString3


class MyTestCase3(unittest.TestCase):
    def test_something(self):
        my_str = MyString3('ravi')
        self.assertEqual(my_str.case_change(), "RAVI")  # add assertion here
