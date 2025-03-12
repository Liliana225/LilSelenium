import allure
from selenium.webdriver.common.by import By

from demoqa_pages.base_page import BasePage


class AlertsPageLocators():
    ALERTS = (By.XPATH, "//span[text() = 'Alerts']")
    SHOW_ALERT = (By.XPATH, "//button[@id = 'alertButton']")
    SHOW_CONFIRM = (By.XPATH, "//button[@id = 'confirmButton']")
    SHOW_PROMT = (By.XPATH, "//button[@id = 'promtButton']")
    SHOW_ALERT_AFTER_5_SECOND = (By.XPATH, "//button[@id = 'timerAlertButton']")
    LOG_CONFIRM = (By.XPATH, "//span[@id = 'confirmResult']")
    LOG_PROMT = (By.XPATH, "//span[@id = 'promptResult']")

class AlertsPage(BasePage):
    @allure.step("Нажать на алерт")
    def show_alert(self):
        self.find_element(AlertsPageLocators.ALERTS, 5).click()
        self.find_element(AlertsPageLocators.SHOW_ALERT, 5).click()
        alert = self.switch_to_alerts()
        alert.accept()

    @allure.step("Нажать на алерт")
    def show_confirm(self):
        self.find_element(AlertsPageLocators.SHOW_CONFIRM, 5).click()
        alert = self.switch_to_alerts()
        alert.dismiss()

    @allure.step("Показать алерт")
    def show_promt(self, promt: str):
        self.find_element(AlertsPageLocators.SHOW_PROMT, 5).click()
        alert = self.switch_to_alerts()
        alert.send_keys(promt)
        alert.accept()

    @allure.step("Нажать на алерт")
    def show_alert_after_5_seconds(self):
        self.find_element(AlertsPageLocators.SHOW_ALERT_AFTER_5_SECOND, 5).click()
        alert = self.alert_is_visible(10)
        alert = self.switch_to_alerts()
        alert.accept()

    @allure.step("Получить лог алерта")
    def get_log_confirm(self):
        log_confirm = self.find_element(AlertsPageLocators.LOG_CONFIRM, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return log_confirm

    @allure.step("Получить лог алерта")
    def get_log_promt(self):
        log_promt = self.find_element(AlertsPageLocators.LOG_PROMT, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return log_promt





