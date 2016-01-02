__author__ = 'Hernan Y.Ke'
import unittest
from itertools import combinations
from functools import wraps

def convert(alpha):
    return ",".join([str(ord(i)-96) for i in alpha])
class TestOne(unittest.TestCase):
    def test_system(self):
        cases = [("aa","1,1"),("xy","24,25")]
        for case in cases:
            with self.subTest(case=case):
                self.assertEqual(convert(case[0]),case[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)