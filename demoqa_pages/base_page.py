import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demoqa.ru/qa-auto"
        self.base_url1 = "https://demoqa.com/"
        self.action_chains = ActionChains(driver)

    def find_element(self, locator, time):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    @allure.step("Открыть сайт")
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step("Открыть сайт")
    def go_to_site_com(self):
        return self.driver.get(self.base_url1)

    def wait_for_to_be_clickable_on_element(self, locator, time):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    def wait_for_visible(self, locator, time):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def scroll_to_bottom(self, locator):
        elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        mapp = elem.location_once_scrolled_into_view
        return

    def switch_to_alerts(self):
        return self.driver.switch_to.alert

    def alert_is_visible(self, time):
        return WebDriverWait(self.driver, time).until(EC.alert_is_present())

    def switch_to_new_window(self, index: int):
        main_window = self.driver.current_window_handle
        new_window = [window for window in self.driver.window_handles if window != main_window][index]
        self.driver.switch_to.window(new_window)