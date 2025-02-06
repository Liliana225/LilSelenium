import time
from time import sleep

import selenium.webdriver.common.by
from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from webdriver_manager.chrome import ChromeDriverManager

import constants

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

driver.get(constants.ADRESS)

elem = driver.find_element(selenium.webdriver.common.by.By.CLASS_NAME, "profile-photo")

elem.click()


elem1 = driver.find_element(selenium.webdriver.common.by.By.ID, "name")

elem1.send_keys(constants.LOGIN)


elem2 = driver.find_element(selenium.webdriver.common.by.By.ID, "password")

elem2.send_keys(constants.PASSWORD)


elem3 = driver.find_element(selenium.webdriver.common.by.By.ID, "login-button")

elem3.click()


elem4 = driver.find_element(selenium.webdriver.common.by.By.CLASS_NAME, "logout")
elem5 = driver.find_element(selenium.webdriver.common.by.By.ID, "user-name")
assert elem4.is_displayed()
assert elem5.text == constants.HAME