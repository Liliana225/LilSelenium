import time
from time import sleep

import selenium.webdriver.common.by
from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from webdriver_manager.chrome import ChromeDriverManager

import constants

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

driver.get(constants.ADRESS)

elem = driver.find_element(selenium.webdriver.common.by.By.CLASS_NAME, "profile-photo")
elem.click()

elem1 = driver.find_element(selenium.webdriver.common.by.By.ID, "name")
elem1.send_keys(constants.LOGIN)

elem2 = driver.find_element(selenium.webdriver.common.by.By.ID, "password")
elem2.send_keys(constants.PASSWORD)

elem3 = driver.find_element(selenium.webdriver.common.by.By.ID, "login-button")
elem3.click()

elem4 = driver.find_element(selenium.webdriver.common.by.By.CLASS_NAME, "dropdown-toggle")
elem4.click()

elem5 = driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "DIFFERENT ELEMENTS")
elem5.click()

elem6 = driver.find_elements(selenium.webdriver.common.by.By.CLASS_NAME, "label-checkbox")
for x in elem6:
    if x.text == "Water" or x.text == "Wind":
        x.click()

elem7 = driver.find_elements(selenium.webdriver.common.by.By.CLASS_NAME, "label-radio")
for x in elem7:
    if x.text == "Selen":
        x.click()

elem8 = driver.find_elements(selenium.webdriver.common.by.By.TAG_NAME, "option")
for x in elem8:
    if x.text == "Yellow":
        x.click()

elem9 = driver.find_element(selenium.webdriver.common.by.By.CLASS_NAME, "info-panel-section")

print(elem9.text)

assert elem9.is_displayed()
assert elem9.text.__contains__("Water")
assert elem9.text.__contains__("Wind")
assert elem9.text.__contains__("Yellow")
assert elem9.text.__contains__("Selen")



