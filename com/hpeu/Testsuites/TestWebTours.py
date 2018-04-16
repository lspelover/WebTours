import unittest
import os
import sys
sys.path.append(os.path.split(os.path.split(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])[0])[0])

from com.hpeu.WebTours.Login import Login
from com.hpeu.WebTours.Login1 import LoginTest

#Add All testcase as above format




if __name__ == '__main__':
    
    suite = unittest.TestSuite()
    
    suite.addTest(Login('test_WebTourLogin'))
    suite.addTest(LoginTest('test_LoginTest'))
    # Add more test case as above format
    
    Runner = unittest.TextTestRunner()
    
    Runner.run(suite)