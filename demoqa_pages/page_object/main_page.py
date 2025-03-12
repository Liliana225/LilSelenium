import allure
from selenium.webdriver.common.by import By

from demoqa_pages.base_page import BasePage


class MainPagesLocators():
    ELEMENTS =  (By.XPATH, "//div[@class = 'text-gray-600 text-sm']")
    WIDGETS = (By.XPATH, "//h3[text() = 'Widgets']")
    INTERACTIONS = (By.XPATH, "//h3[text() = 'Interactions']")
    ALERTS = (By.XPATH, "//h3[text() = 'Alerts & Modals']")
    ALERTS_COM = (By.XPATH, "//h5[text() = 'Alerts, Frame & Windows']")
    BOOK_STORE = (By.XPATH, "//h3[text() = 'Book Store']")
    FORMS = (By.XPATH, "//h3[text() = 'Forms']")
    TESTS = (By.XPATH, "//h3[text() = 'Tests']")

class MainPage(BasePage):
    @allure.step("Открыть страницу элементов")
    def go_to_elements(self):
        self.find_element(MainPagesLocators.ELEMENTS, 5).click()
        return

    @allure.step("Открыть страницу виджетов")
    def go_to_widgets(self):
        self.find_element(MainPagesLocators.WIDGETS, 5).click()
        return

    @allure.step("Открыть страницу interactions")
    def go_to_interactions(self):
        self.find_element(MainPagesLocators.INTERACTIONS, 5).click()
        return

    @allure.step("Открыть страницу алертов")
    def go_to_alerts(self):
        self.find_element(MainPagesLocators.ALERTS, 5).click()
        return

    @allure.step("Открыть сайт")
    def go_to_alerts_com(self):
        self.scroll_to_bottom(MainPagesLocators.ALERTS_COM)
        self.find_element(MainPagesLocators.ALERTS_COM, 5).click()
        return

    @allure.step("Открыть раздел BookStore")
    def go_to_bookstore(self):
        self.find_element(MainPagesLocators.BOOK_STORE, 5).click()
        return

    @allure.step("Открыть раздел Forms")
    def go_to_forms(self):
        self.find_element(MainPagesLocators.FORMS, 5).click()
        return

    @allure.step("Открыть раздел tests")
    def go_to_tests(self):
        self.find_element(MainPagesLocators.TESTS, 5).click()
        return


