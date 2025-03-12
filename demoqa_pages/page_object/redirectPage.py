import allure
from selenium.webdriver.common.by import By
from demoqa_pages.base_page import BasePage
import math

class RedirectPageLocators():
    MATH_BUTTON = (By.XPATH, "//a[@class = 'trollface btn btn-primary']")
    ANSWER_BUTTON = (By.XPATH, "//input[@type = 'text']")
    SUBMIT = (By.XPATH, "//button[@type = 'submit']")
    REDIRECT_BUTTON = (By.XPATH, "//p[text() = 'Тест с математическим редиректом и ограничением по времени']")
    X_ELEMENT = (By.XPATH, "//label[@class = 'block text-gray-700']")

class RedirectPage(BasePage):
    @allure.step("Выполнить решение математического уравнения")
    def math_redirect_test(self):
        self.find_element(RedirectPageLocators.REDIRECT_BUTTON, 5).click()
        self.find_element(RedirectPageLocators.MATH_BUTTON, 5).click()

        x_elements = self.find_element(RedirectPageLocators.X_ELEMENT, 5)
        x = int(x_elements.text[38:-1])

        result = math.log(abs(12 * math.sin(x)))
        answer = self.find_element(RedirectPageLocators.ANSWER_BUTTON, 5)
        answer.click()
        answer.send_keys(result)
        self.find_element(RedirectPageLocators.SUBMIT,5).click()

    @allure.step("Получить лог алерта")
    def get_log_alert(self) -> str:
        alert = self.switch_to_alerts()
        alert_text = alert.text
        alert.accept()
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return alert_text
