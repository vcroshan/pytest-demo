class MyString2:
    def __init__(self, s):
        self.s = s

    def check_palindrome(self):
        print('check_palindrome')
        return self.s == self.s[::-1]

