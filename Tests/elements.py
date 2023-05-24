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

    select = browser.find_element(By.XPATH, f"/html/body/div/div/div[2]/div[1]/form/div[2]/select")
    button = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/button")

    if select.is_enabled() == False and button.is_enabled() == False:
        return True
    else:
        return False

def check_is_disabled_enabled(browser):
    brand = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[1]/select")
    select_brand = Select(brand)
    select_brand.select_by_value('Lexus')
    time.sleep(2)

    select_enabled = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[2]/select")

    model = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[2]/select")
    select_model = Select(model)
    select_model.select_by_value('NX200')

    body_type = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[3]/select")
    select_body_type = Select(body_type)
    select_body_type.select_by_value('sedan')

    fuel_type = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[4]/select")
    select_fuel_type = Select(fuel_type)
    select_fuel_type.select_by_value('diesel')

    transmission = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[5]/select")
    select_transmission = Select(transmission)
    select_transmission.select_by_value('AT')

    milleage = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[6]/input")
    milleage.send_keys('10000')

    power = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[7]/input")
    power.send_keys('200')

    year = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[8]/input")
    year.send_keys('2000')

    engine = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[9]/input")
    engine.send_keys('1.5')
    time.sleep(2)

    button_enabled = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/button")

    if button_enabled.is_enabled() == True and select_enabled.is_enabled() == True:
        return True
    else:
        return False