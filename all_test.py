#coding=utf-8
import unittest
from Prac.testadd import TestAdd
from Prac.testsub import TestSub
import os
def createsuite():
    dir=os.getcwd()
    print(dir)
    discover=unittest.defaultTestLoader.discover(dir,pattern="test*.py",top_level_dir=None)
    print(discover)
    return discover
if __name__=="__main__":
    runner=unittest.TextTestRunner()
    runner.run(createsuite())