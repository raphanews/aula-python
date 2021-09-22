#testando classe
import unittest

class MyFun1:
    def fun(self, n):
        return n + 1

class MyFunTest(unittest.TestCase):
    def testFun(self):
        obj = MyFun1()
        self.assertEqual(obj.fun(3), 4)

if __name__ == '__main__':
    unittest.main()