#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import logging

class BasePage():
    def __init__(self,driver):
        self.driver=driver
    def open(self,url):
        self.driver.get(url)
    def find_element(self,locator):
        try:
            e=WebDriverWait(self.driver,15).until(EC.presence_of_element_located(locator))
        except BaseException:
            print("can't find the locator")
        else:
            return e
    def send_keys(self,locator,keyword):
        e=self.find_element(locator)
        e.clear()
        e.send_keys(keyword)
    def cick_button(self,locator):
        e=self.find_element(locator)
        e.click()
    def switch_to_frame(self,d):
        self.driver.switch_to_frame(d)
    def is_title_contains(self,title):
        result=WebDriverWait(self.driver,10).until(EC.title_contains(title))
        return result
    def is_alert_present(self):
        result=WebDriverWait(self.driver,10).until(EC.alert_is_present())
        return result

