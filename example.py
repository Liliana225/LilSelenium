import time
from time import sleep

import selenium.webdriver.common.by
from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.implicitly_wait(10)

driver.get("http://www.google.com")

elem0 = driver.find_element(selenium.webdriver.common.by.By.XPATH, "/html/body/div[1]/div[6]/div/div[2]/div[1]/a[2]")

print(elem0.text)

elem = driver.find_element(selenium.webdriver.common.by.By.ID, "APjFqb")

elem.send_keys("Лилиана")

elem.submit()


# elem2 = driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "Конфиденциальность")
#
# elem2.click()
#
# time.sleep(4)

# /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea - xPATH


