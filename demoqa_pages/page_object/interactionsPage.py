import allure
from selenium.webdriver.common.by import By

from demoqa_pages.base_page import BasePage

class InteractionsPageLocators():
    SELECTABLE = (By.XPATH, "//p[text() = 'Выбор элементов кликом или выделением области']")
    ELEMENTS_5 = (By.XPATH, "//span[text() = 'Элемент 5']")
    LOG = (By.XPATH, "//p[@class = 'text-sm text-gray-500 mt-1']")
    ELEMENTS_7 = (By.XPATH, "//span[text() = 'Элемент 7']")
    SINGLE_SELECTION = (By.XPATH, "//button[text() = 'Одиночный выбор']")
    ELEMENTS_1 = (By.XPATH, "//span[text() = 'Элемент 1']")
    ELEMENTS_4 = (By.XPATH, "//span[text() = 'Элемент 4']")
    ELEMENTS_8 = (By.XPATH, "//span[text() = 'Элемент 8']")
    SELECT_ALL = (By.XPATH, "//button[text() = 'Выбрать все']")

class InteracrionsPage(BasePage):
    @allure.step("Выбрать элемент 5")
    def select_elements_5(self):
        self.find_element(InteractionsPageLocators.SELECTABLE, 5).click()
        self.find_element(InteractionsPageLocators.ELEMENTS_5, 5).click()

    @allure.step("Выбрать элемент 7")
    def select_elements_7(self):
        self.find_element(InteractionsPageLocators.ELEMENTS_7, 5).click()

    @allure.step("Выбрать элементы 1, 4, 8")
    def multiple_selection(self):
        self.find_element(InteractionsPageLocators.SINGLE_SELECTION, 5).click()
        self.find_element(InteractionsPageLocators.ELEMENTS_1, 5).click()
        self.find_element(InteractionsPageLocators.ELEMENTS_4, 5).click()
        self.find_element(InteractionsPageLocators.ELEMENTS_8, 8).click()

    @allure.step("Выбрать всё")
    def select_all(self):
        self.find_element(InteractionsPageLocators.SELECT_ALL, 5).click()

    @allure.step("Получить лог элементов")
    def get_log_elements(self):
        log = self.find_element(InteractionsPageLocators.LOG, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return log

    @allure.step("Получить лог множества элементов")
    def get_log_multiple(self):
        log_multiple = self.find_element(InteractionsPageLocators.LOG, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return log_multiple

    @allure.step("Получить лог всех элементов")
    def get_log_all(self):
        log_all = self.find_element(InteractionsPageLocators.LOG, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return log_all