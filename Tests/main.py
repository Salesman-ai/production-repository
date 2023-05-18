import unittest
from result import check_good_result, check_error_result
from elements import check_exists, check_is_disabled_enabled, check_disabled
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

browser_error = webdriver.Chrome(options=options)
browser_error.get('http://192.168.58.4')

browser_disabled = webdriver.Chrome(options=options)
browser_disabled.get('http://192.168.58.4')


class RunTest(unittest.TestCase):

    def test_elements_exists(self):
        result = check_exists(browser)
        self.assertEqual(result, 9)

    def test_check_disabled(self):
        result = check_disabled(browser)
        self.assertFalse(result.is_enabled());
    
    def test_check_disabled_is_enabled(self):
        result = check_is_disabled_enabled(browser_disabled)
        self.assertTrue(result.is_enabled());

    def test_result(self):
        result = check_good_result(browser)
        self.assertIsInstance(result, float)
    
    def test_error_result(self):
        result = check_error_result(browser_error)
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()