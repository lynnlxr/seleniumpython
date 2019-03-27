#coding=utf-8
from Prac.prac import Count
import unittest
import HTMLTestRunner
class TestAdd(unittest.TestCase):
    def setUp(self):
        print("begin")
    def test_add1(self):
        self.j=Count(3,4,8)
        h=self.j.add()
        self.assertEqual(h,8,"wrong answer")
    def test_add2(self):
        self.j=Count("hello"," lynn",7)
        l=self.j.add()
        self.assertEqual(l,"hello lynn","wrong answer")
    def tearDown(self):
        print("over")
if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(TestAdd("test_add1"))
    suite.addTest(TestAdd("test_add2"))
    runner=unittest.TextTestRunner()
    runner.run(suite)
