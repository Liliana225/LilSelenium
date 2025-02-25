import allure
from selenium.webdriver.common.by import By

from demoqa_pages.base_page import BasePage


class CheckboxLocators():
    CHECK_BOX = (By.XPATH, "//p[text() = 'Работа с чекбоксами и их состояниями']")
    EXPAND_ALL1 = (By.XPATH, "//div[@class = 'mb-8']/div/div/button[@class = 'p-1 hover:bg-gray-100 rounded']")
    EXPAND_ALL2 = (By.XPATH, "//div[@class = 'ml-2']/div[1]/div/button[@class = 'p-1 hover:bg-gray-100 rounded']")
    EXPAND_ALL3 = (By.XPATH, "//div[@class = 'ml-2']/div[2]/div/button[@class = 'p-1 hover:bg-gray-100 rounded']")
    EXPAND_ALL4 = (By.XPATH, "//div[@class = 'ml-2']/div[3]/div/button[@class = 'p-1 hover:bg-gray-100 rounded']")
    COMMANDS = (By.XPATH, "//span[text() = 'Commands']")
    WORK_SPACE = (By.XPATH, "//span[text() = 'Workspace']")
    EXEL_FILE_DOC = (By.XPATH, "//span[text() = 'Excel File.doc']")
    RESULT = (By.XPATH, "//div[@class = 'mt-6 p-4 bg-gray-50 rounded-lg']")

class CheckBoxPage(BasePage):
    @allure.step("Заполнить checkbox")
    def fill_checkboxes(self):
        self.find_element(CheckboxLocators.CHECK_BOX, 5).click()
        self.find_element(CheckboxLocators.EXPAND_ALL1, 5).click()
        self.find_element(CheckboxLocators.EXPAND_ALL2, 5).click()
        self.find_element(CheckboxLocators.EXPAND_ALL3, 5).click()
        self.find_element(CheckboxLocators.EXPAND_ALL4, 5).click()
        self.find_element(CheckboxLocators.COMMANDS, 5).click()
        self.find_element(CheckboxLocators.WORK_SPACE, 5).click()
        self.scroll_to_bottom(CheckboxLocators.EXEL_FILE_DOC)
        self.find_element(CheckboxLocators.EXEL_FILE_DOC, 5).click()
        return

    @allure.step("Получить заполнения")
    def get_filling(self):
        filling = self.find_element(CheckboxLocators.RESULT, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return filling