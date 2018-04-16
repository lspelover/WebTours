import unittest
from com.hpeu.WebTours.Login import Login
from com.hpeu.WebTours.LoginTest import LoginTest
#Add All testcase as above format

if __name__ == '__main__':
    suite = unittest.TestSuite()
    
    suite.addTest(Login('test_WebTourLogin'))
    suite.addTest(LoginTest('test_LoginTest'))
    # Add more test case as above format
    
    Runner = unittest.TextTestRunner()
    
    Runner.run(suite)