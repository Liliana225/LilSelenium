from re import search

import allure

import constants
from base_page.base_page import BasePage
from selenium.webdriver.common.by import By

from constants import CURRENT_URL
from pages.loginPage import LoginPageLocators


class ElementsPage(BasePage):
    @allure.step("Отметить элементы")
    def markElements(self):
        label_checkbox = self.find_elements(LoginPageLocators.LABELCHECKBOX, 5)
        for x in label_checkbox:
            if x.text == "Water" or x.text == "Wind":
                x.click()
        label_radio = self.find_elements(LoginPageLocators.LABELRADIO, 5)
        for x in label_radio:
            if x.text == "Selen":
                x.click()
        option = self.find_elements(LoginPageLocators.OPTIONS, 5)
        for x in option:
            if x.text == "Yellow":
                x.click()

    @allure.step("Проверить элементы")
    def check_elements(self):
        info_panel = self.find_element(LoginPageLocators.INFO_PANEL, 5)
        assert info_panel.is_displayed()
        assert info_panel.text.__contains__("Water")
        assert info_panel.text.__contains__("Wind")
        assert info_panel.text.__contains__("Selen")
        assert info_panel.text.__contains__("Yellow")

    @allure.step("Проверить нужный ли сайт открыт")
    def isOpenedNow(self):
        return self.driver.current_url == CURRENT_URL






