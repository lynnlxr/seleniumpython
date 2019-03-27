#coding=utf-8
from Prac.prac import Count
import unittest
import os
import time
import HTMLTestRunner
class TestSub(unittest.TestCase):
    def setUp(self):
        print("begin")
    def test_sub1(self):
        u'''测试两数相减'''
        self.j=Count(3,4,7)
        h=self.j.add()
        self.assertEqual(h,7,"wrong answer")
    def test_sub2(self):
        self.j=Count(6.8,2.5,7)
        l=self.j.add()
        self.assertEqual(l,2,"wrong answer")
    def tearDown(self):
        print("over")
if __name__=="__main__":
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    suite=unittest.TestSuite()
    suite.addTest(TestSub("test_sub1"))
    suite.addTest(TestSub("test_sub2"))
    # runner=unittest.TextTestRunner()
    # runner.run(suite)
    dd=os.getcwd()
    print(dd)
    file_path=os.path.join(os.getcwd()+"\\report\\"+now+"testadd.html")
    print(file_path)
    f=open(file_path,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=1,title="My first report",description="test sub")
    # runner=unittest.TextTestRunner()
    runner.run(suite)
