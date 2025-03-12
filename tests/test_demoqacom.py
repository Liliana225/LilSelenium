import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from demoqa_pages.page_object.alertsPage import AlertsPage
from demoqa_pages.page_object.main_page import MainPage


@pytest.fixture(scope="session")
def driverFixtureCom():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты demoqa.com")
@allure.story("Тесты alerts")
@allure.feature("Тесты alerts")
@allure.description("Тест проверяет корректность работы раздела alerts")
def test_alert_com(driverFixtureCom):
    log_confirm1 = "You selected Cancel"
    promt1 = "Lili"
    alerts_page = AlertsPage(driverFixtureCom)
    main_page = MainPage(driverFixtureCom)
    alerts_page.go_to_site_com()
    main_page.go_to_alerts_com()
    alerts_page.show_alert()
    #тут нет ассерта, нет лога на сайте
    alerts_page.show_confirm()
    log_confirm = alerts_page.get_log_confirm()
    assert log_confirm.text.__contains__(log_confirm1)
    alerts_page.show_promt(promt1)
    log_promt = alerts_page.get_log_promt()
    assert log_promt.text.__contains__(promt1)
    alerts_page.show_alert_after_5_seconds()


