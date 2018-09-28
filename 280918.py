import unittest

def sum(a,b):
    return a+b

def g(a,b):
    return a/b

class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sum(1,3),4)

unittest.main()

# python3 doctest
# для тестирования сайтов selenium
# coverage
