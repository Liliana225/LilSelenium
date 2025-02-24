import time

import allure
from selenium.webdriver.common.by import By
from demoqa_pages.base_page import BasePage
from demoqa_pages.page_object.main_page import MainPage
from selenium.webdriver.common.keys import Keys

class TextBoxPageLocators():
    TEXT_BOX = (By.XPATH, "//div[@class = 'flex items-center gap-3']")
    FULL_NAME = (By.XPATH, "//input[@id = 'fullName']")
    EMAIL = (By.XPATH, "//input[@id = 'email']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id = 'currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id = 'permanentAddress']")
    SUBMIT = (By.XPATH, "//form[@class = 'space-y-6']/div[5]/button")
    LOGS = (By.XPATH, "//div[@class = 'mt-8 p-4 bg-gray-50 rounded-lg']")


class TextBoxPage(BasePage):
    @allure.step("Заполнить textbox")
    def write_to_textbox(self, fullname: str, myemail: str, curaddress: str, peraddress: str):
        self.find_element(TextBoxPageLocators.TEXT_BOX, 5).click()

        full_name = self.find_element(TextBoxPageLocators.FULL_NAME, 5)
        full_name.send_keys(fullname)

        email = self.find_element(TextBoxPageLocators.EMAIL, 5)
        email.send_keys(myemail)

        current_address = self.find_element(TextBoxPageLocators.CURRENT_ADDRESS, 5)
        current_address.send_keys(curaddress)

        permanent_address = self.find_element(TextBoxPageLocators.PERMANENT_ADDRESS, 5)
        permanent_address.send_keys(peraddress)

        permanent_address.send_keys(Keys.PAGE_DOWN)

        self.scroll_to_bottom(TextBoxPageLocators.SUBMIT)
        submit = self.wait_for_to_be_clickable_on_element(TextBoxPageLocators.SUBMIT, 5)
        submit.click()
        return

    def get_logs(self):
        logs = self.find_element(TextBoxPageLocators.LOGS, 5)
        return logs
