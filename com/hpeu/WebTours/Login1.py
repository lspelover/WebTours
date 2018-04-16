#coding=utf-8
'''
Created on 2018��4��2��

@author: lushi
'''

from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_LoginTest(self):
        mydriver = self.driver
        mydriver.get('http://newtours.demoaut.com/mercurywelcome.php')
        mydriver.find_element_by_name('userName').send_keys('LuShiPeng')
        mydriver.find_element_by_name('password').send_keys('lushipeng')
        mydriver.find_element_by_name('login').click()
        time.sleep(5)
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()
    
'''
mydriver = webdriver.Firefox()
mydriver.get('http://newtours.demoaut.com/mercurywelcome.php') 

mydriver.find_element_by_name('userName').send_keys('LuShiPeng')
mydriver.find_element_by_name('password').send_keys('lushipeng')
mydriver.find_element_by_name('login').click()

time.sleep(5)

mydriver.close()
'''