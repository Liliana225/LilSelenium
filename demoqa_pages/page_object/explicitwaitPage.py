import allure
from selenium.webdriver.common.by import By
from demoqa_pages.base_page import BasePage

class ExplicitWaitPageLocators():
    EXPLICIT_WAIT_BUTTON = (By.XPATH, "//p[text() = 'Тест на работу с явными ожиданиями и заполнением формы']")
    SHOW_FORM_BUTTON = (By.XPATH, "//button[text() = 'Показать форму']")
    FIRST_NAME = (By.XPATH, "//input[@id = 'firstName']")
    LAST_NAME = (By.XPATH, "//input[@id = 'lastName']")
    EMAIL = (By.XPATH, "//input[@id = 'email']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text() = 'Submit']")
    LOG_AFTER_FILLING_FORM = (By.XPATH, "//div[@class = 'bg-green-50 p-4 rounded-lg']")
    VERIFICATION_CODE = (By.XPATH, "//input[@id = 'verificationCode']")
    CHECK_CODE = (By.XPATH, "//button[@type = 'submit']")
    LOG_AFTER_CHECKING_CODE = (By.XPATH, "//p[text() = 'Поздравляем! Тест успешно пройден!']")

class ExplicitWaitPage(BasePage):
    @allure.step("Заполнить форму после появления кликабельности у кнопки")
    def fill_out_the_form(self, first_name: str, last_name: str, email1:str):
        self.find_element(ExplicitWaitPageLocators.EXPLICIT_WAIT_BUTTON, 5).click()
        show_form_button = self.wait_for_to_be_clickable_on_element(ExplicitWaitPageLocators.SHOW_FORM_BUTTON, 10)
        show_form_button.click()

        firstname = self.find_element(ExplicitWaitPageLocators.FIRST_NAME, 5)
        firstname.click()
        firstname.send_keys(first_name)

        lastname = self.find_element(ExplicitWaitPageLocators.LAST_NAME, 5)
        lastname.click()
        lastname.send_keys(last_name)

        email = self.find_element(ExplicitWaitPageLocators.EMAIL, 5)
        email.click()
        email.send_keys(email1)

        self.find_element(ExplicitWaitPageLocators.SUBMIT_BUTTON, 5).click()

    @allure.step("Ввести верный проверочный код")
    def check_code(self):
        code_after_filling = self.find_element(ExplicitWaitPageLocators.LOG_AFTER_FILLING_FORM, 5)
        code = str(code_after_filling.text[47:])

        verification_code = self.find_element(ExplicitWaitPageLocators.VERIFICATION_CODE, 5)
        verification_code.click()
        verification_code.send_keys(code)

        self.find_element(ExplicitWaitPageLocators.CHECK_CODE, 5).click()

    @allure.step("Получить лог кода")
    def log_after_checking_code(self):
        log = self.find_element(ExplicitWaitPageLocators.LOG_AFTER_CHECKING_CODE, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return log.text

