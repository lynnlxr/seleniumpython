#coding=utf-8
import unittest
from selenium import webdriver
class Count():
    def __init__(self,a,b,s):
        self.a=a
        self.b=b
        self.s=s
    def add(self):
        return self.a+self.b
    def minus(self):
        return self.a-self.b
    def is_prime(self):
        if self.s<=1:
            return False
        for i in range(2,self.s):
            if self.s%2==0:
                return False
        return True





