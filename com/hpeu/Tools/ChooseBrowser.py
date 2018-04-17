# coding = utf-8

from selenium import webdriver

class ChooseBrowser():
    def ChooseBrowser(self,TestBrowser):
        driver = webdriver
        if TestBrowser == 'IE':
            driver = webdriver.Ie()
        elif TestBrowser == 'Chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        
        return driver