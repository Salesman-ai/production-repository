import unittest
from result import check_result
from elements import check_exists
from elements import check_disabled
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import unittest

options = Options()
options.add_argument("--headless=new")

browser = webdriver.Chrome(options=options)
browser.get('http://192.168.58.4')



class RunTest(unittest.TestCase):

    def test_elements_exists(self):
        result = check_exists(browser)
        self.assertEqual(result, 8)

    def test_check_disabled(self):
        result = check_disabled(browser)
        self.assertFalse(result.is_enabled());

    def test_result(self):
        result = check_result(browser)
        self.assertIsInstance(result, float)
    

if __name__ == '__main__':
    unittest.main()
