import os
import time

import allure
from selenium.webdriver.common.by import By
from enum import Enum

from demoqa_pages.base_page import BasePage


class FormsPageLocators():
    FIRST_NAME = (By.XPATH, "//input[@name = 'firstName']")
    LAST_NAME = (By.XPATH, "//input[@name = 'lastName']")
    EMAIL = (By.XPATH, "//input[@name = 'email']")
    FEMALE = (By.XPATH, "//span[text() = 'female']")
    MALE = (By.XPATH, "//span[text() = 'male']")
    MOBILE = (By.XPATH, "//input[@name = 'mobile']")
    DATE = (By.XPATH, "//input[@type = 'date']")
    HOBBIES = (By.XPATH, "//span[text() = 'reading']")
    UPLOAD_PICTURE = (By.XPATH, "//input[@type = 'file']")
    UPLOAD_PICTURE_BUTTON = (By.XPATH, "//button[@type = 'button']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@name = 'currentAddress']")
    STATE = (By.XPATH, "//input[@name = 'state']")
    CITY = (By.XPATH, "//input[@name = 'city']")
    SUBMIT_FORM = (By.XPATH, "//button[text() = 'Submit Form']")
    HOBBIES_FORMS = (By.XPATH, "//label[@class = 'flex items-center space-x-3 cursor-pointer']")


class Hobbies(Enum):
    SPORTS = 0
    READING = 1
    MUSIC = 2


class StudentRegisrtationForm:

    def set_firstname(self, firstname: str):
        self.firstname = firstname
        return self

    def set_lastname(self, lastname: str):
        self.lastname = lastname
        return self

    def set_email(self, email: str):
        self.email = email
        return self

    def set_isFemale(self, isFemale: bool):
        self.isFemale = isFemale
        return self

    def set_mobile(self, mobile: int):
        self.mobile = mobile
        return self

    def set_date(self, date: str):
        self.date = date
        return self

    def set_curaddress(self, curaddress: str):
        self.curaddress = curaddress
        return self

    def set_state(self, state: str):
        self.state = state
        return self

    def set_city(self, city: str):
        self.city = city
        return self

    def set_hobbies(self, hobbies: list[Hobbies]):
        self.hobbies = hobbies
        return self

    def set_upload_pictures(self, path: str):
        self.path = path
        return self

class FormsPage(BasePage):
    @allure.step("Заполнить форму")
    def register_form(self, form: StudentRegisrtationForm):
        first_name = self.find_element(FormsPageLocators.FIRST_NAME, 5)
        first_name.click()
        first_name.send_keys(form.firstname)

        last_name = self.find_element(FormsPageLocators.LAST_NAME, 5)
        last_name.click()
        last_name.send_keys(form.lastname)

        email = self.find_element(FormsPageLocators.EMAIL, 5)
        email.click()
        email.send_keys(form.email)

        if form.isFemale is True:
            self.find_element(FormsPageLocators.FEMALE, 5).click()
        else:
            self.find_element(FormsPageLocators.MALE, 5).click()

        self.scroll_to_bottom(FormsPageLocators.MOBILE)

        mobile = self.find_element(FormsPageLocators.MOBILE, 5)
        mobile.click()
        mobile.send_keys(form.mobile)

        date = self.find_element(FormsPageLocators.DATE, 5)
        date.click()
        date.send_keys(form.date)

        hobbies = self.find_elements(FormsPageLocators.HOBBIES_FORMS, 5)
        for hobby in form.hobbies:
            hobbies[hobby.value].click()

        file_path = os.path.abspath(form.path)
        upload_pictures = self.find_element(FormsPageLocators.UPLOAD_PICTURE, 5)
        upload_pictures.send_keys(file_path)


        curaddress = self.find_element(FormsPageLocators.CURRENT_ADDRESS, 5)
        curaddress.click()
        curaddress.send_keys(form.curaddress)

        state = self.find_element(FormsPageLocators.STATE, 5)
        state.click()
        state.send_keys(form.state)

        city = self.find_element(FormsPageLocators.CITY, 5)
        city.click()
        city.send_keys(form.city)

        self.scroll_to_bottom(FormsPageLocators.SUBMIT_FORM)
        self.find_element(FormsPageLocators.SUBMIT_FORM, 5).click()
