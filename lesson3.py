import time
from time import sleep

import selenium.webdriver.common.by
from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from webdriver_manager.chrome import ChromeDriverManager

import constants

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

driver.get(constants.ADRESS)

elem = driver.find_element(selenium.webdriver.common.by.By.XPATH, "//div[@class='profile-photo']")
elem.click()

elem1 = driver.find_element(selenium.webdriver.common.by.By.XPATH, "//input[@id='name']")
elem1.send_keys(constants.LOGIN)

elem2 = driver.find_element(selenium.webdriver.common.by.By.XPATH, "//input[@id='password']")
elem2.send_keys(constants.PASSWORD)

elem3 = driver.find_element(selenium.webdriver.common.by.By.XPATH, "//button[@id='login-button']")
elem3.click()

elem4 = driver.find_element(selenium.webdriver.common.by.By.XPATH, "//a[@class='dropdown-toggle']")
elem4.click()

elem5 = driver.find_element(selenium.webdriver.common.by.By.XPATH, "//a[@href='different-elements.html']")
elem5.click()

elem6 = driver.find_elements(selenium.webdriver.common.by.By.XPATH, "//label[@class = 'label-checkbox']")
for x in elem6:
    if x.text == "Water" or x.text == "Wind":
        x.click()

elem7 = driver.find_elements(selenium.webdriver.common.by.By.XPATH, "//label[@class = 'label-radio']")
for x in elem7:
    if x.text == "Selen":
        x.click()

elem8 = driver.find_elements(selenium.webdriver.common.by.By.XPATH, "//option")
for x in elem8:
    if x.text == "Yellow":
        x.click()

elem9 = driver.find_element(selenium.webdriver.common.by.By.XPATH, "//div[@class = 'info-panel-section']")

print(elem9.text)

assert elem9.is_displayed()
assert elem9.text.__contains__("Water")
assert elem9.text.__contains__("Wind")
assert elem9.text.__contains__("Yellow")
assert elem9.text.__contains__("Selen")



