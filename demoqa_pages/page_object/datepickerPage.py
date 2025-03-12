import time

import allure
from selenium.webdriver.common.by import By
from enum import Enum

from selenium.webdriver.support.select import Select

from demoqa_pages.base_page import BasePage

class DatePickerPageLocators():
    DATE_PICKER = (By.XPATH, "//p[text() = 'Выбор даты и времени']")
    SELECT_A_SINGLE_DATE = (By.XPATH, "//input[@placeholder = 'Select a date...']")
    SELECT_A_RANGE_DATE = (By.XPATH, "//input[@placeholder = 'Select date range...']")
    BUTTON_7 = (By.XPATH, "//button[text() = '7']")
    BUTTON_MARCH_2025_1 = (By.XPATH, "//div[@class = 'flex items-center justify-between mb-4']/h3")
    NEXT_BUTTON = (By.XPATH, "//div[@class = 'flex items-center justify-between mb-4']/button[2]")
    BUTTON_MARCH_2025_2 = (By.XPATH, "//div[@class = 'flex items-center justify-between mb-4']/h3")

class DatePickerPage(BasePage):
    @allure.step("Выбрать одну дату")
    def select_a_single_date(self):
        self.find_element(DatePickerPageLocators.DATE_PICKER, 5).click()
        self.find_element(DatePickerPageLocators.SELECT_A_SINGLE_DATE, 5).click()

        while True:
            current_month_year = self.find_element(DatePickerPageLocators.BUTTON_MARCH_2025_1, 5).text
            if current_month_year == "July 2025":
                break
            next_button = self.find_element(DatePickerPageLocators.NEXT_BUTTON, 5)
            next_button.click()

        day_element = self.find_element(DatePickerPageLocators.BUTTON_7, 5)
        day_element.click()

    @allure.step("Выбрать диапозон (две даты)")
    def select_a_range_date(self):
        self.find_element(DatePickerPageLocators.SELECT_A_RANGE_DATE, 5).click()

        while True:
            current_month_year = self.find_element(DatePickerPageLocators.BUTTON_MARCH_2025_2, 5).text
            if current_month_year == "July 2025":
                break
            next_button = self.find_element(DatePickerPageLocators.NEXT_BUTTON, 5)
            next_button.click()

        day_element = self.find_element(DatePickerPageLocators.BUTTON_7, 5)
        day_element.click()

        while True:
            current_month_year = self.find_element(DatePickerPageLocators.BUTTON_MARCH_2025_2, 5).text
            if current_month_year == "July 2026":
                break
            next_button = self.find_element(DatePickerPageLocators.NEXT_BUTTON, 5)
            next_button.click()

        day_element = self.find_element(DatePickerPageLocators.BUTTON_7, 5)
        day_element.click()
        return

    def log_select_a_date(self):
        log_select_a_date = self.find_element(DatePickerPageLocators.SELECT_A_SINGLE_DATE, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return log_select_a_date

    def log_select_a_range_date(self):
        log_select_a_range_date = self.find_element(DatePickerPageLocators.SELECT_A_RANGE_DATE, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return log_select_a_range_date


