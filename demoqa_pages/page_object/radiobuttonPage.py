import allure
from selenium.webdriver.common.by import By

from demoqa_pages.base_page import BasePage

class RadioButtonLocators():
    RADIO_BUTTON = (By.XPATH, "//h3[text() = 'Radio Button']")
    NO_BUTTON = (By.XPATH, "//input[@value = 'no']")
    IMPRESSIVE = (By.XPATH, "//input[@value = 'impressive']")
    RESULT = (By.XPATH, "//span[@class = 'text-[#1565c0] font-medium capitalize']")

class RadioButtonPage(BasePage):
    @allure.step("Кликнуть по кнопке radiobutton")
    def click_on_radio_button(self):
        self.find_element(RadioButtonLocators.RADIO_BUTTON, 5).click()
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return

    @allure.step("Кликнуть по кнопке no")
    def click_on_enabled(self):
        no_button = self.find_element(RadioButtonLocators.NO_BUTTON, 5)
        return no_button

    @allure.step("Кликнуть по кнопке impressive")
    def click_on_impressive(self):
        self.find_element(RadioButtonLocators.IMPRESSIVE, 5).click()
        return

    @allure.step("Получить логи")
    def get_logs(self):
        logs = self.find_element(RadioButtonLocators.RESULT, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return logs