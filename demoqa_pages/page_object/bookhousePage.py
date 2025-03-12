import allure
from selenium.webdriver.common.by import By
from demoqa_pages.base_page import BasePage
import math

class BookHousePageLocators():
    BOOK_HOUSE = (By.XPATH, "//p[text() = 'Форма бронирования дома']")
    BOOK_BUTTON = (By.XPATH, "//button[text() = 'Book']")
    ANSWER_BUTTON = (By.XPATH, "//input[@type = 'text']")
    SUBMIT = (By.XPATH, "//button[@type = 'submit']")
    PRICE_ELEMENT = (By.XPATH, "//div[@class = 'flex justify-between items-center mb-2']")
    X_ELEMENT = (By.XPATH, "//label[@class = 'block text-gray-700']")

class BookHousePage(BasePage):
    @allure.step("Купить дом за определенную сумму и решить уравнение")
    def book_house(self):
        self.find_element(BookHousePageLocators.BOOK_HOUSE, 5).click()
        while True:
            price = self.find_element(BookHousePageLocators.PRICE_ELEMENT, 5).text
            if "100" in price:
                self.find_element(BookHousePageLocators.BOOK_BUTTON, 5).click()
                break

        x_elements = self.find_element(BookHousePageLocators.X_ELEMENT, 5)
        x = int(x_elements.text[38:-1])

        result = math.log(abs(12 * math.sin(x)))
        answer = self.find_element(BookHousePageLocators.ANSWER_BUTTON, 5)
        answer.click()
        answer.send_keys(result)
        self.find_element(BookHousePageLocators.SUBMIT, 5).click()

    @allure.step("Получить лог алерта")
    def get_log_alert(self) -> str:
        alert = self.switch_to_alerts()
        alert_text = alert.text
        alert.accept()
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return alert_text


