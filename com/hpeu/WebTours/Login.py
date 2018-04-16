# coding=utf-8

import time
import unittest
from com.hpeu.Tools.ChooseBrowser import ChooseBrowser
from com.hpeu.Tools.ReadFile import ReadFile
from com.hpeu.Tools.GetScreenshot import GetScreenshot

class Login(unittest.TestCase):
    def setUp(self):
        #定义浏览器类型
       
        #driver = webdriver.Ie()
        self.GetVule = ReadFile()
        
        myBrowser = ChooseBrowser()        
        self.driver = myBrowser.ChooseBrowser(self.GetVule.getTestConf('BrowserType', 'TestBrowser'))
        self.getScreenTest = GetScreenshot(self.driver)
    
    def test_WebTourLogin(self):
        mydriver = self.driver
        
        SystemURL =self.GetVule.getTestConf('WebToursSystem', 'SystemURL')
        Username = self.GetVule.getElement('NAME', 'UsernameInputBox')
        Password = self.GetVule.getElement('NAME', 'PasswordInputBox')
        Loginbtn = self.GetVule.getElement('NAME', 'LoginBtn')
               
        # Open the Login page
        mydriver.get(SystemURL)
        time.sleep(5)
        #print(mydriver.find_element_by_xpath('//td[@colspan="2"]/font').text)
        
        assert ' to join Mercury Tours!' in mydriver.page_source
        self.getScreenTest.screenshot('LoginPage')
        
        #Input Username
        mydriver.find_element_by_name(Username).send_keys('LuShiPeng')
        #Input Password
        mydriver.find_element_by_name(Password).send_keys('lushipeng')
        #Click login button
        mydriver.find_element_by_name(Loginbtn).click()
        time.sleep(5)
        
        #OPen the home page
        self.assertEqual(mydriver.find_element_by_xpath("//tbody/tr/td[1]/a").text,'SIGN-OFF')
        
        self.assertEqual(mydriver.find_element_by_xpath("//form[@method='post']//tr[1]/td/font/font/b/font").text, 'Flight Details')
        
        #mydriver.get_screenshot_as_file("C:\\Users\\lushi\\eclipse-workspace\\WebTours\\screenshots\\login.png")
        self.getScreenTest.screenshot('HomePage')
        
        time.sleep(5)
        
    def tearDown(self):
        self.driver.close()
'''     
if __name__ == '__main__':
    unittest.main()
'''        