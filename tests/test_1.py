import pytest

from pages.elementsPage import ElementsPage
from pages.loginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driverFixture():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_login(driverFixture):
    loginpage = LoginPage(driverFixture)
    loginpage.go_to_site()
    assert loginpage.checkStartElements()
    loginpage.switch_to_frame("frame")
    assert loginpage.checkFrame()
    loginpage.switch_to_default()


def test_elementsPage(driverFixture):
    elementspage = ElementsPage(driverFixture)
    loginpage = LoginPage(driverFixture)
    loginpage.go_to_site()
    loginpage.login("Roman", "Jdi1234")
    loginpage.goToElementsPage()
    assert elementspage.isOpenedNow()
    elementspage.markElements()
    elementspage.check_elements()









