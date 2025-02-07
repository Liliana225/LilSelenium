import time
from time import sleep

import selenium.webdriver.common.by
from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from webdriver_manager.chrome import ChromeDriverManager

import constants

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

driver.get(constants.ADRESS)

elem = driver.find_elements(selenium.webdriver.common.by.By.NAME, "navigation-sidebar")



elem1 = driver.find_element(selenium.webdriver.common.by.By.CLASS_NAME, "active")

print(len(elem))

#assert len(elem) ==5
#assert elem1.text == "HOME"

elem2 = driver.find_elements(selenium.webdriver.common.by.By.CLASS_NAME, "benefit-txt")
print(len(elem2))


driver.switch_to.frame("frame")

elem3 = driver.find_element(selenium.webdriver.common.by.By.ID, "frame-button")

assert elem3.is_displayed()

driver.switch_to.default_content()

assert len(elem2) == 4