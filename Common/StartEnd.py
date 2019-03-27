#coding=utf-8
from selenium import webdriver
from BaiduSearch.Common.Basehandle import BaseHandle
import unittest
import time
class StartEnd(unittest.TestCase):
    url="https://www.baidu.com"
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.baidu=BaseHandle(self.driver)
        self.baidu.open(self.url)
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

