# coding=utf-8


import os
import configparser
from test.test_optparse import TestConflict

class ReadFile():
    def getTestConf(self,section, option):
        root_dir=os.path.dirname(os.path.abspath('.'))
        
        #result is WebTours\com\hpeu
        
        #print("!!!!")
        config = configparser.ConfigParser()
        file_path = root_dir + '\\..\\..\\resources\\Configuration.properties'
        
       
        config.read(file_path)
        
        #print(config.sections())
        #print(config.options(config.sections))
        
        TestConf = config.get(section, option)
        
        return TestConf
    
    def getElement(self,section,option):
        root_dir=os.path.dirname(os.path.abspath('.'))
        file_path = root_dir + '\\..\\..\\resources\\PageElement.properties'
        #result is WebTours\com\hpeu
        
        #print("!!!!")
        config = configparser.ConfigParser()

        config.read(file_path)
        
        #print(config.sections())
        #print(config.options(config.sections))
        
        Element = config.get(section, option)
        return Element
        
        