#coding=utf-8
import unittest
from selenium import webdriver
from BaiduSearch.Common.Basehandle import BaseHandle
from BaiduSearch.Common.get_search_data import get_search_data
from BaiduSearch.Common.StartEnd import StartEnd
import logging
class Test_setting(StartEnd):
    def test_alert_setting(self):
        self.baidu.seeting_save()
        e=self.baidu.is_alert_present()
        self.assertTrue(e)
if __name__=="__main__":
    unittest.main()