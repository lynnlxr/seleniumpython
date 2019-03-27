#coding=utf-8
from selenium import webdriver
from BaiduSearch.Common.Basepage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import logging
import time

class BaseHandle(BasePage):
    #百度搜索
    input_box = ("id", "kw")
    submit_button = ("id", "su")
    setting_button=("link text",u"设置")
    search_setting=("link text",u"搜索设置")
    #百度搜索设置
    meiyexianshi10=("id","nr")
    meiyexianshi50=("xpath","//option[@value='50']")
    saveseting=("xpath","//*[@id='gxszButton']/a")
    #163邮箱登录
    login_user=("xpath","//*[@id='account-box']/div[2]/input")
    login_pwd=("xpath","//input[@name='password' and @type='password']")
    switch_iframe=("xpath","//iframe[starts-with(@id,'x-URS-iframe')]")
    login_button=("id","dologin")
    login_success_button=("id","spnUid")
    error_text=("xpath","//*[@id='nerror']/div[2]")

    def input_send_keys(self,keywords):
        self.send_keys(self.input_box,keywords)
    def click_submit_button(self):
        self.cick_button(self.submit_button)
    #163邮箱登录
    def inpu_user(self,username):
        self.send_keys(self.login_user,username)
    def input_pwd(self,pwd):
        self.send_keys(self.login_pwd,pwd)
    def baidu_search(self,keywords):
        logging.info("输入关键字")
        self.input_send_keys(keywords)
        logging.info("点击搜索按钮")
        self.click_submit_button()
    def switch_frame(self):
        e=self.find_element(self.switch_iframe)
        self.switch_to_frame(e)
    def seeting_save(self):
        e=self.find_element(self.setting_button)
        ActionChains(self.driver).move_to_element(e).perform()
        self.cick_button(self.search_setting)
        self.cick_button(self.meiyexianshi10)
        self.cick_button(self.meiyexianshi50)
        self.cick_button(self.saveseting)
        time.sleep(3)
    def mail_login(self,username,pwd):
        self.switch_frame()
        self.inpu_user(username)
        self.input_pwd(pwd)
        self.cick_button(self.login_button)
    def is_login_success(self):
        text1=self.find_element(self.login_success_button).text
        return text1
    def login_error(self):
        text1=self.find_element(self.error_text).text
        return text1








