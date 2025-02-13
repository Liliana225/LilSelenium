from pages.elementsPage import ElementsPage
from pages.loginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
loginpage = LoginPage(driver)

loginpage.go_to_site()
assert loginpage.checkStartElements()
loginpage.switch_to_frame("frame")
assert loginpage.checkFrame()
loginpage.switch_to_default()
driver.quit()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
elementspage = ElementsPage(driver)
loginpage = LoginPage(driver)

loginpage.go_to_site()
loginpage.login("Roman", "Jdi1234")
loginpage.goToElementsPage()
assert elementspage.isOpenedNow()
elementspage.markElements()
elementspage.check_elements()
driver.quit()








