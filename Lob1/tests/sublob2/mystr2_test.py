import unittest
from Lob1.src.scripts.sublob2.mystr_02 import MyString2

class MyTestCase2(unittest.TestCase):
    def test_something(self):
        my_str = MyString2('malayalam')
        self.assertEqual(True, my_str.check_palindrome())  # add assertion here
