import allure
from selenium.webdriver.common.by import By
from demoqa_pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class SelectSumPageLocators():
    SELECT_SUM = (By.XPATH, "//p[text() = 'Тест на сложение чисел с выбором из выпадающего списка']")
    FIND_THE_SUM = (By.XPATH, "//h2[@class = 'text-xl font-semibold text-gray-700 flex items-center gap-2']/span")
    SELECT_ANSWER = (By.XPATH, "//select[@id = 'dropdown']")
    SUBMIT = (By.XPATH, "//button[@type = 'submit']")

class SelectSumPage(BasePage):
    @allure.step("Выбрать из выпадающего списка результат суммы двух чисел")
    def select_sum(self):
        self.find_element(SelectSumPageLocators.SELECT_SUM, 5).click()

        find_the_sum = self.find_elements(SelectSumPageLocators.FIND_THE_SUM, 5)

        result = int(find_the_sum[1].text) + int(find_the_sum[3].text)

        dropdown = self.find_element(SelectSumPageLocators.SELECT_ANSWER, 5)
        select = Select(dropdown)
        select.select_by_visible_text(str(result))

        self.find_element(SelectSumPageLocators.SUBMIT, 5).click()

    @allure.step("Получить лог алерта")
    def get_select_sum(self) -> str:
        alert = self.switch_to_alerts()
        alert_text = alert.text
        alert.accept()
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return alert_text




