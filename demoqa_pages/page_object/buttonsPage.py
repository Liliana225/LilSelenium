import allure
from selenium.webdriver.common.by import By

from demoqa_pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class ButtonsPageLocators():
    BUTTONS = (By.XPATH, "//h3[text() = 'Buttons']")
    CLICK_ME = (By.XPATH, "//button[text() = 'Click Me']")
    RIGHT_CLICK_ME = (By.XPATH, "//button[text() = 'Right Click Me']")
    DOUBLE_CLICK_ME = (By.XPATH, "//button[text() = 'Double Click Me']")
    DYNAMIC_CLICK_ME = (By.XPATH, "//button[text() = 'Dynamic Click Me']")
    LOG_1 = (By.XPATH, "//p[text() = 'You have clicked ']")
    LOG_2 = (By.XPATH, "//p[text() = 'You have right clicked ']")
    LOG_3 = (By.XPATH, "//p[text() = 'You have double clicked ']")
    LOG_4 = (By.XPATH, "//p[text() = 'You have dynamically clicked ']")

class ButtonsPage(BasePage):
    @allure.step("Клинуть по кнопке n-раз")
    def click_on_n_time(self, n:int):
        self.find_element(ButtonsPageLocators.BUTTONS, 5).click()
        for _ in range(n):
            self.find_element(ButtonsPageLocators.CLICK_ME, 5).click()
        log1 = self.find_element(ButtonsPageLocators.LOG_1, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return log1.text

    @allure.step("Клинуть правой кнопкой мыши n-раз")
    def click_on_right_click(self, n:int):
        for _ in range(n):
            right_click_me = self.find_element(ButtonsPageLocators.RIGHT_CLICK_ME, 5)
            ActionChains(self.driver).context_click(right_click_me).perform()
        log2 = self.find_element(ButtonsPageLocators.LOG_2, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return log2.text

    @allure.step("Клинуть по кнопке дважды n-раз")
    def click_on_double_click(self):
        double_click = self.find_element(ButtonsPageLocators.DOUBLE_CLICK_ME, 5)
        ActionChains(self.driver).double_click(double_click).perform()
        log3 = self.find_element(ButtonsPageLocators.LOG_3, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return log3.text

    @allure.step("Клинуть по динамической кнопке n-раз")
    def click_on_dynamic_click(self, n: int):
        for _ in range(n):
            self.wait_for_to_be_clickable_on_element(ButtonsPageLocators.DYNAMIC_CLICK_ME, 5).click()
        log4 = self.find_element(ButtonsPageLocators.LOG_4, 5)
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        return log4.text