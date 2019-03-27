#encoding=utf-8
import unittest
from selenium import webdriver
from BaiduSearch.Common.Basehandle import BaseHandle
from BaiduSearch.Common.get_search_data import get_search_data
import time
class Testmaillogin(unittest.TestCase):
    url="https://mail.163.com/"
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.mail=BaseHandle(self.driver)
        self.mail.open(self.url)
    def tearDown(self):
        time.sleep(2)
    # def test_163maillogin(self):
    #     self.mail.mail_login("limingqiande123","796532lxr")
    #     t=self.mail.is_login_success()
    #     self.assertEqual(t,"limingqiande123@163.com")
    def test_login_errorname(self):
        self.mail.mail_login("liming123de2","34563dfg")
        t=self.mail.login_error()
        self.assertEqual(t,u"帐号或密码错误")
    def test_kong_name(self):
        self.mail.mail_login("","23456fgh")
        t=self.mail.login_error()
        self.assertEqual(t,u"请输入帐号")

if __name__=="__main__":
    unittest.main()


