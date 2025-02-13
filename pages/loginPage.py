from re import search

import constants
from base_page.base_page import BasePage
from selenium.webdriver.common.by import By

from constants import CURRENT_URL


class LoginPageLocators:

 NAME = (By.XPATH, "//input[@id='name']")
 PASSWORD = (By.XPATH, "//input[@id='password']")
 LOGIN_BUTTON = (By.XPATH, "//button[@class = 'uui-button dark-blue btn-login']")
 LOGOUT = (By.XPATH, "//div[@class = 'logout']")
 USERNAME = (By.ID, "user-name")
 LABELCHECKBOX = (By.XPATH, "//label[@class = 'label-checkbox']")
 LABELRADIO = (By.XPATH, "//label[@class = 'label-radio']")
 OPTIONS = (By.XPATH, "//option")
 INFO_PANEL = (By.XPATH, "//div[@class = 'info-panel-body info-panel-body-log']")
 NAVIGATION_BAR = (By.CSS_SELECTOR, "[name='navigation-sidebar']")
 ACTIVE = (By.XPATH, "//div[@class = 'uui-header dark-gray']")
 BENEFIT_TXT = (By.CSS_SELECTOR, ".benefit-txt")
 FRAME_BUTTON = (By.CSS_SELECTOR, "#frame-button")
 SERVICE = (By.XPATH, "//a[@class = 'dropdown-toggle']")
 DIFFERENT_ELEMENTS = (By.XPATH, "//a[@href='different-elements.html']")
 PROFILE_PHOTO = (By.XPATH, "//div[@class = 'profile-photo']")

class LoginPage(BasePage):

    def login(self, login:str, password:str):
        self.find_element(LoginPageLocators.PROFILE_PHOTO).click()
        login_field = self.find_element(LoginPageLocators.NAME, 5)
        login_field.click()
        login_field.send_keys(login)

        password_field = self.find_element(LoginPageLocators.PASSWORD, 5)
        password_field.click()
        password_field.send_keys(password)

        self.find_element(LoginPageLocators.LOGIN_BUTTON, 5).click()

        return

    def check_login(self):
        return (self.find_element(LoginPageLocators.LOGOUT).is_displayed() and
                self.find_element(LoginPageLocators.USERNAME).text == constants.HAME)

    def checkStartElements(self):
        find_element = self.find_element(LoginPageLocators.NAVIGATION_BAR, 5)
        find_element1 = self.find_element(LoginPageLocators.ACTIVE, 5)
        find_elements = self.find_elements(LoginPageLocators.BENEFIT_TXT, 5)
        everyElementIsDisplayed = True
        for x in find_elements:
            if not x.is_displayed():
                everyElementIsDisplayed = False
        return find_element.is_displayed() and find_element1.is_displayed() and everyElementIsDisplayed

    def checkFrame(self):
        #self.switch_to_frame("frame")
        checkFrame = self.find_element(LoginPageLocators.FRAME_BUTTON, 5)
        #self.switch_to_default()
        return checkFrame.is_displayed()

    def goToElementsPage(self):
        self.find_element(LoginPageLocators.SERVICE, 5).click()
        self.find_element(LoginPageLocators.DIFFERENT_ELEMENTS, 5).click()
        return










