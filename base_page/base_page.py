from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://jdi-testing.github.io/jdi-light/index.html"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time). until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def switch_to_frame(self, frame: str):
        return self.driver.switch_to.frame(frame)

    def switch_to_default(self):
        return self.driver.switch_to.default_content()



