#coding=utf-8
import unittest
class Testin(unittest.TestCase):
    def setUp(self):
        pass
    def testini(self):
        self.a="hello"
        self.b="hello lxr"
        self.assertIn(self.a,self.b,msg="a is not in b")
    def testtrue(self):
        self.a=3
        self.assertTrue(self.a==1,msg="a is not 1")
    def tearDown(self):
        pass
if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(Testin("testini"))
    runner=unittest.TextTestRunner()
    runner.run(suite)