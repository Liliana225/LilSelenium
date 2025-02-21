from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from demoqa_pages.base_page import BasePage

class WebTablesPageLocators():
    WEB_TABLES = (By.XPATH, "//h3[text() = 'Web Tables']")
    ADD_NEW_EMPLOYEE = (By.XPATH, "//button[text() = 'Add New Employee']")
    FIRST_NAME = (By.XPATH, "//input[@name = 'firstName']")
    LAST_NAME = (By.XPATH, "//input[@name = 'lastName']")
    AGE = (By.XPATH, "//input[@name = 'age']")
    EMAIL = (By.XPATH, "//input[@name = 'email']")
    SALARY = (By.XPATH, "//input[@name = 'salary']")
    DEPARTMENT = (By.XPATH, "//input[@name = 'department']")
    ADD = (By.XPATH, "//button[text() = 'Add']")
    LOGS = (By.XPATH, "//td[text() = 'li@mail.ru']/../td")
    SEARCH = (By.XPATH, "//input[@placeholder = 'Search...']")
    DELETE = (By.XPATH, "//td[text() = 'li@mail.ru']/../td[6]/div/button[@class = 'p-1 text-red-600 hover:text-red-800']")
    ROWS_IN_TABLE = (By.XPATH, "//tbody[@class = 'bg-white divide-y divide-gray-200']/*")

class WebTablesPage(BasePage):

    def add_new_employeer(self, first_name:str, last_name:str, age: int, email:str, salary:int, department:str):

        self.find_element(WebTablesPageLocators.WEB_TABLES, 5).click()
        self.find_element(WebTablesPageLocators.ADD_NEW_EMPLOYEE, 5).click()

        firstName = self.find_element(WebTablesPageLocators.FIRST_NAME, 5)
        firstName.send_keys(first_name)

        lastName = self.find_element(WebTablesPageLocators.LAST_NAME, 5)
        lastName.send_keys(last_name)

        myage = self.find_element(WebTablesPageLocators.AGE, 5)
        myage.send_keys(age)

        myemail = self.find_element(WebTablesPageLocators.EMAIL, 5)
        myemail.send_keys(email)

        mysalary = self.find_element(WebTablesPageLocators.SALARY, 5)
        mysalary.send_keys(salary)

        mydepartment = self.find_element(WebTablesPageLocators.DEPARTMENT, 5)
        mydepartment.send_keys(department)

        self.find_element(WebTablesPageLocators.ADD, 5).click()

    def get_logs(self):

        logs = self.find_elements(WebTablesPageLocators.LOGS, 5)
        logs_text = []
        for x in logs:
            logs_text.append(x.text)
        return logs_text

    def search_lil(self, name: str):

        search = self.find_element(WebTablesPageLocators.SEARCH,5)
        search.click()
        search.send_keys(name)
        return search.text

    def delete_add(self):
        self.find_element(WebTablesPageLocators.DELETE, 5).click()

    def get_rows_in_table(self) ->[] :
        try:
            return self.find_elements(WebTablesPageLocators.ROWS_IN_TABLE, 5)
        except TimeoutException:
            return []



