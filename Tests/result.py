from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def check_result(browser):

    #Brand
    brand = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[1]/select")
    select_brand = Select(brand)
    select_brand.select_by_value('Lexus')
    time.sleep(1)

    #Model
    model = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[2]/select")
    select_model = Select(model)
    select_model.select_by_value('NX200')

    #Body Type
    body_type = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[3]/select")
    select_body_type = Select(body_type)
    select_body_type.select_by_value('sedan')

    #Fuel Type
    fuel_type = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[4]/select")
    select_fuel_type = Select(fuel_type)
    select_fuel_type.select_by_value('diesel')

    #Transmission
    transmission = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[5]/select")
    select_transmission = Select(transmission)
    select_transmission.select_by_value('AT')

    #Mileage
    milleage = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[6]/input")
    milleage.send_keys('10000')

    #Power
    power = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[7]/input")
    power.send_keys('200')

    #Year
    year = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[8]/input")
    year.send_keys('2000')

    #Engine
    engine = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/div[9]/input")
    engine.send_keys('1.5')
    time.sleep(2)

    #Check Price
    check_btn = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/form/button")
    check_btn.click()
    time.sleep(3)

    #Get Result
    result = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/p[2]").text

    return float(result)