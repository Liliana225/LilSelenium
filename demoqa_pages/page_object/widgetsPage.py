import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from demoqa_pages.base_page import BasePage

class WidgetsPageLocators():
    AUTO_COMPLETE = (By.XPATH, "//h3[text() = 'Auto Complete']")
    SINGLE_SEARCH = (By.XPATH, "//input[@placeholder = 'Type a color...']")
    MILTIPLE_SEARCH = (By.XPATH, "//input[@placeholder = 'Type colors...']")
    MULTIPLE_SEARCH_FIELD =  (By.XPATH, "//input[@placeholder = '']")
    BLUE_BUTTON = (By.XPATH, "//span[text() = 'Blue']")
    BROWN_BUTTON = (By.XPATH, "//span[text() = 'Brown']")
    GRAY_BUTTON = (By.XPATH, "//span[text() = 'Gray']")
    LOG1 = (By.XPATH, "//input[@value = 'Blue']")

class WidgetsPage(BasePage):
    @allure.step("Найти один цвет")
    def search_a_single_color(self, color1: str):
        self.find_element(WidgetsPageLocators.AUTO_COMPLETE, 5).click()

        blue = self.find_element(WidgetsPageLocators.SINGLE_SEARCH, 5)
        blue.click()
        blue.send_keys(color1)

        self.find_element(WidgetsPageLocators.BLUE_BUTTON, 5).click()
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.step("Найти коричневый цвет")
    def search_a_brown_color(self, color2: str):
        brown = self.find_element(WidgetsPageLocators.MILTIPLE_SEARCH, 5)
        brown.click()
        brown.send_keys(color2)

        self.find_element(WidgetsPageLocators.BROWN_BUTTON, 5).click()
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.step("Найти серый цвет")
    def search_a_gray_color(self, color3: str):
        grey = self.find_element(WidgetsPageLocators.MULTIPLE_SEARCH_FIELD, 5)
        grey.click()
        grey.send_keys(color3)

        self.find_element(WidgetsPageLocators.GRAY_BUTTON, 5).click()
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.step("Локатор поиска одного цвета")
    def single_by_value(self):
        log1 = self.find_element(WidgetsPageLocators.LOG1, 5)
        colorLog = log1.get_attribute("value")
        return colorLog

    @allure.step("Получить лог коричневого цвета")
    def get_log_brown(self):
        try:
            return self.find_element(WidgetsPageLocators.BROWN_BUTTON, 5).text
        except TimeoutException:
            return ""

    @allure.step("Получить лог серого цвета")
    def get_log_gray(self):
        try:
            return self.find_element(WidgetsPageLocators.GRAY_BUTTON, 5).text
        except TimeoutException:
            return ""