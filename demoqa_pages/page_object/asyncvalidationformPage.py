import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from demoqa_pages.base_page import BasePage

class AsyncValidationFormLocators():
    ASYNCVALIDATION_BUTTON = (By.XPATH, "//h3[text() = 'Асинхронная валидация формы']")
    NAME = (By.XPATH, "//input[@placeholder = 'Введите имя пользователя']")
    EMAIL = (By.XPATH, "//input[@placeholder = 'Введите email']")
    SUBMIT_THE_FORM = (By.XPATH, "//button[text() = 'Отправить форму']")
    LOG = (By.XPATH, "//p[text() = 'Неверный формат email']")

class AsyncValidationFormPage(BasePage):
    def submit_the_form(self, myname: str, myemail:str):
        self.find_element(AsyncValidationFormLocators.ASYNCVALIDATION_BUTTON, 5).click()

        name = self.find_element(AsyncValidationFormLocators.NAME, 5)
        name.click()
        name.send_keys(myname)

        email = self.find_element(AsyncValidationFormLocators.EMAIL, 5)
        email.click()
        email.send_keys(myemail)

    def click_on_submit_the_form(self):
        self.wait_for_to_be_clickable_on_element(AsyncValidationFormLocators.SUBMIT_THE_FORM, 5).click()

    def get_log_alert(self):
        alert = self.switch_to_alerts()
        alert_text = alert.text
        alert.accept()
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return alert_text

    def get_log(self):
        log = self.find_element(AsyncValidationFormLocators.LOG, 5)
        return log.text