#coding=utf-8
from count import Count
import unittest
class TestCount(unittest.TestCase):
    def setUp(self):
        self.j=Count(2,5)
    def test_add(self):
        self.add=self.j.add()
        self.assertEqual(self.add,8)
    def test_sub(self):
        self.sub=self.j.sub()
        self.assertEqual(self.sub,-2)
    def tearDown(self):
        pass

if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(TestCount("test_sub"))
    suite.addTest(TestCount("test_add"))
    runner=unittest.TextTestRunner()
    runner.run(suite)

