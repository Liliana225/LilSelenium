import time
from time import sleep

import selenium.webdriver.common.by
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import constants

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

driver.get(constants.ADRESS)

elem = driver.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR,  "[name='navigation-sidebar']")

elem1 = driver.find_element(selenium.webdriver.common.by.By.XPATH, "//div[@class = 'uui-header dark-gray']")

assert elem1.is_displayed()

elem2 = driver.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR, ".benefit-txt")

driver.switch_to.frame("frame")

elem3 = driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR, "#frame-button")

assert elem3.is_displayed()

driver.switch_to.default_content()

assert len(elem2) == 4