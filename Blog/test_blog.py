#coding=utf-8
import unittest
from selenium import webdriver
import time
import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as EC
class BlogHome(unittest.TestCase):
#https://passport.cnblogs.com/user/signin
    u'''博客首页'''

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        url="http://www.cnblogs.com/yoyoketang"
        cls.driver.get(url)
        cls.driver.implicitly_wait(30)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_01(self):
        u'''验证元素存在：博客园'''
        locator=("id","blog_nav_sitehome")
        text=u"博客园"
        result=EC.text_to_be_present_in_element(locator,text)(self.driver)
        self.assertTrue(result)
    def test_02(self):
        u'''验证元素存在：首页'''
        locator=("id","blog_nav_myhome")
        text=u"首页23"
        # EC.title_is()
        result=EC.text_to_be_present_in_element(locator,text)(self.driver)
        self.assertTrue(result)
if __name__=="__main__":
    now = time.strftime('%Y-%m-%d_%H%M%S')
    test_report="E:\\Seleniumlynn\\Report\\"
    filename=test_report+now+'report.html'
    suite=unittest.TestSuite()
    suite.addTest(BlogHome("test_01"))
    suite.addTest(BlogHome("test_02"))
    fp=open(filename,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=1,title="report",description=u"用例执行情况")
    runner.run(suite)
    fp.close()


