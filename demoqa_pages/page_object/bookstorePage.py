import allure
from selenium.webdriver.common.by import By

from demoqa_pages.base_page import BasePage

class BookStorePageLocators():
    REGISTER = (By.XPATH, "//span[text() = 'Register']")
    USERNAME = (By.XPATH, "//input[@type = 'text']")
    PASSWORD = (By.XPATH, "//input[@type = 'password']")
    REGISTER_BUTTON = (By.XPATH, "//button[@type = 'submit']")
    BOOK_STORE_BUTTON = (By.XPATH, "//main/div/div/button")
    ADD_TO_COLLECTION = (By.XPATH, "//button[text() = 'Add to Collection']")
    PROFILE = (By.XPATH, "//span[text() = 'Profile']")
    MY_COLLECTION = (By.XPATH, "//div[@class = 'bg-white p-6 rounded-lg shadow-sm border border-gray-100']")
    MORE_ABOUT_THE_BOOK = (By.XPATH, "//a[text() = 'Подробнее о книге']")
    ADD_TO_BASKET = (By.XPATH, "//button[text() = 'Добавить в корзину']")
    BASKET = (By.XPATH, "//span[text() = '0']")

class BookStorePage(BasePage):

    @allure.step("Зарегистрироваться на сайте")
    def register_on_the_site(self, username1: str, password1: str):
        self.find_element(BookStorePageLocators.REGISTER, 5).click()

        username = self.find_element(BookStorePageLocators.USERNAME, 5)
        username.click()
        username.send_keys(username1)

        password = self.find_element(BookStorePageLocators.PASSWORD, 5)
        password.click()
        password.send_keys(password1)

        self.find_element(BookStorePageLocators.REGISTER_BUTTON, 5).click()

    @allure.step("Добавить книгу в коллекцию")
    def add_a_new_book(self):
        elems = self.find_elements(BookStorePageLocators.BOOK_STORE_BUTTON, 5)
        elems[0].click()
        self.find_element(BookStorePageLocators.ADD_TO_COLLECTION, 5).click()

    @allure.step("Получить лог моей коллекции")
    def get_log_a_book(self):
        self.find_element(BookStorePageLocators.PROFILE, 5).click()
        log_a_book = self.find_element(BookStorePageLocators.MY_COLLECTION, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return log_a_book

    @allure.step("Добавить книгу в корзину")
    def book_and_basket(self):
        self.find_element(BookStorePageLocators.BOOK_STORE_BUTTON, 5).click()
        self.find_element(BookStorePageLocators.MORE_ABOUT_THE_BOOK, 5).click()
        self.switch_to_new_window(0)
        self.find_element(BookStorePageLocators.ADD_TO_BASKET, 5).click()

    @allure.step("Получить лог корзины")
    def log_basket(self):
        log_basket = self.find_element(BookStorePageLocators.BASKET, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return log_basket





