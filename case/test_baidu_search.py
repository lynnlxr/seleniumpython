#coding=utf-8
import unittest
from selenium import webdriver
from BaiduSearch.Common.Basehandle import BaseHandle
from BaiduSearch.Common.get_search_data import get_search_data
from BaiduSearch.Common.StartEnd import StartEnd
import logging
import time
data1=get_search_data()
print(data1)
import HTMLTestRunner
from ddt import ddt,data
@ddt
class Test_Baidu_Search(StartEnd):
    # url = "https://www.baidu.com"
    # def setUp(self):
    #     logging.info("======begin=====")
    #     self.driver=webdriver.Chrome()
    #     self.baidu=BaseHandle(self.driver)
    #     self.baidu.open(self.url)
    # def tearDown(self):
    #     time.sleep(3)
    #     logging.info("==========test finished============")
    #     self.driver.quit()
    @data(*data1)
    def test_baidu_search(self,data1):
        logging.info("=====test1=====")
        self.baidu.baidu_search(data1)
        e=self.baidu.is_title_contains(u"百度搜索")
        self.assertTrue(e)
if __name__=="__main__":
    unittest.main()







