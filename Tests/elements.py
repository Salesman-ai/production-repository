from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def check_exists(browser):
    status = 0
    for i in range(1, 10):
        if i < 6:
            if browser.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[1]/form/div[{i}]/select") != 0:
                status += 1
        else:
            if browser.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[1]/form/div[{i}]/input") != 0:
                status += 1
    return status

def check_disabled(browser):
    return browser.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[1]/form/div[2]/select")

def check_is_disabled_enabled(browser):
    brand = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[1]/select")
    select_brand = Select(brand)
    select_brand.select_by_value('Lexus')
    time.sleep(1)

    return browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[2]/select")


def check_if_button_is_disabled(browser):
    return browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/button")