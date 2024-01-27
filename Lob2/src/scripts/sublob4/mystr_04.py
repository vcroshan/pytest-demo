class MyString4:
    def __init__(self, s):
        self.s = s

    def case_change(self):
        print('case_change')
        return self.s.upper()

