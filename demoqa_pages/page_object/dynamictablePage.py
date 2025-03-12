import allure
from selenium.webdriver.common.by import By
from demoqa_pages.base_page import BasePage

class DynamicTablePageLocators():
    DYNAMIC_TABLE_BUTTON = (By.XPATH, "//h3[text() = 'Динамическая таблица']")
    START_TEST_BUTTON = (By.XPATH, "//button[text() = 'Начать тест']")
    ADD_A_STRING_IN_TABLE = (By.XPATH, "//button[text() = 'Добавить строку']")
    TABLE_LOCATOR = (By.XPATH, "//table[@class = 'w-full border-collapse']/tbody/tr")
    SAVE_NEW_USERS = (By.XPATH, "//button[@title = 'Сохранить']")
    EDIT_USERS_BUTTON = (By.XPATH, "//button[@title = 'Редактировать']")


class DynamicTablePage(BasePage):
    def len_table(self, name: str, age: int, email: str, city: str):
        self.find_element(DynamicTablePageLocators.DYNAMIC_TABLE_BUTTON, 5).click()
        self.find_element(DynamicTablePageLocators.START_TEST_BUTTON, 5).click()
        self.scroll_to_bottom(DynamicTablePageLocators.TABLE_LOCATOR)
        lentable = len(self.find_elements(DynamicTablePageLocators.TABLE_LOCATOR, 5))
        table = [[]]
        for x in range (0,lentable):
            y = str(x+1)
            tempLocator = (By.XPATH, DynamicTablePageLocators.TABLE_LOCATOR[1] + "["+y+"]/td")
            print(tempLocator[1])
            row = self.find_elements(tempLocator, 5)
            table.append(row)

        self.find_element(DynamicTablePageLocators.ADD_A_STRING_IN_TABLE, 5).click()

        for row in table:
            for elem in row:
                if elem.text == "Санкт-Петербург":
                    elem[]

        # table[3] = [4, name, age, email, city]
        # self.find_element(DynamicTablePageLocators.SAVE_NEW_USERS, 5).click()
        #
        # self.find_element(DynamicTablePageLocators.ADD_A_STRING_IN_TABLE, 5).click()
        # table[4] = [4, name, age, email, city]
        # self.find_element(DynamicTablePageLocators.SAVE_NEW_USERS, 5).click()
        #
        # edit = self.find_elements(DynamicTablePageLocators.EDIT_USERS_BUTTON,5)
        # edit[0].click()







