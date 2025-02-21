from selenium.webdriver.common.by import By

from demoqa_pages.base_page import BasePage


class MainPagesLocators():

    ELEMENTS =  (By.XPATH, "//div[@class = 'text-gray-600 text-sm']")
    WIDGETS = (By.XPATH, "//h3[text() = 'Widgets']")


class MainPage(BasePage):

    def go_to_elements(self):
        self.find_element(MainPagesLocators.ELEMENTS, 5).click()
        return

    def go_to_widgets(self):
        self.find_element(MainPagesLocators.WIDGETS, 5).click()
        return






