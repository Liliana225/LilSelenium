import pytest
from playwright.sync_api import Browser, sync_playwright

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def browser_pw() -> Browser:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()