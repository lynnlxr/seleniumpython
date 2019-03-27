#encoding=utf-8
import unittest
import HTMLTestRunner
import time,sys
import logging
path1="E:\\Seleniumlynn\\"
sys.path.append(path1)
test_dir="E:\\Seleniumlynn\\BaiduSearch\\case"
report_dir="E:\\Seleniumlynn\\BaiduSearch\\reports\\"
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + '/' + now + ' test_report.html'
f=open(report_name,"wb")
runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="test report",description="all test")
logging.info("====start run case=====")
runner.run(discover)


