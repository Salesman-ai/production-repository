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
import os
from dotenv import load_dotenv
from pathlib import Path


try:
    config_path = Path('./config.file')
    load_dotenv(dotenv_path=config_path)
except Exception as error:
    exit()

options = Options()
options.add_argument("--headless=new")

browser = webdriver.Chrome(options=options)
browser.get('http://' + os.environ.get("WEBSITE_URL"))

browser_error = webdriver.Chrome(options=options)
browser_error.get('http://' + os.environ.get("WEBSITE_URL"))

browser_disabled = webdriver.Chrome(options=options)
browser_disabled.get('http://' + os.environ.get("WEBSITE_URL"))


class RunTest(unittest.TestCase):

    def test_elements_exists(self):
        result = check_exists(browser)
        self.assertEqual(result, 9)

    def test_check_disabled(self):
        result = check_disabled(browser)
        self.assertTrue(result)
    
    def test_check_disabled_is_enabled(self):
        result = check_is_disabled_enabled(browser_disabled)
        self.assertTrue(result)

    #-----------------------

    def test_result(self):
        result = check_good_result(browser)
        self.assertTrue(result>0.0)
        self.assertIsInstance(result, float)
    
    def test_error_result(self):
        result = check_error_result(browser_error)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()