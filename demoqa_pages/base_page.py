from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demoqa.ru/qa-auto"
        self.action_chains = ActionChains(driver)

    def find_element(self, locator, time):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def wait_for_to_be_clickable_on_element(self, locator, time):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    def wait_for_visible(self, locator, time):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def scroll_to_bottom(self, locator):
        elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        mapp = elem.location_once_scrolled_into_view
        return