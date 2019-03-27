#coding=utf-8
import unittest
import time
class Test(unittest.TestCase):
    #装饰器，setUpClass所有用例执行前仅执行一次
    @classmethod
    def setUpClass(cls):
        print("start")
    @unittest.skip
    def test01(self):
        print("test01")
    def test02(self):
        print("test02")
    @unittest.skipIf(True,u"为True的时候跳过")
    def test03(self):
        print("test03")
    @unittest.skipUnless(False,u"为False的时候跳过")
    def test05(self):
        print("test05")
    def test04(self):
        a=2
        b=4
        self.assertEqual(a,b)
    #装饰器 tearDownClass所有用例执行后仅执行一次
    @classmethod
    def tearDownClass(cls):
        print("end")
if __name__=="__main__":
    unittest.main()