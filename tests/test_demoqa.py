import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from demoqa_pages.base_page import BasePage
from demoqa_pages.page_object.buttonsPage import ButtonsPage
from demoqa_pages.page_object.checkboxPage import CheckBoxPage
from demoqa_pages.page_object.radiobuttonPage import RadioButtonPage
from demoqa_pages.page_object.textboxPage import TextBoxPage
from demoqa_pages.page_object.main_page import MainPage
from demoqa_pages.page_object.webtablesPage import WebTablesPage
from demoqa_pages.page_object.widgetsPage import WidgetsPage

FullNameForTest = "lili"
MyEmail = "li@mail.ru"
CurAddress = "Spb"
PerAddress = "Msk"

@pytest.fixture(scope="session")
def driverFixture():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_write_to_textbox(driverFixture):
    textbox_page = TextBoxPage(driverFixture)
    main_page = MainPage(driverFixture)
    textbox_page.go_to_site()
    main_page.go_to_elements()
    textbox_page.write_to_textbox(FullNameForTest, MyEmail, CurAddress, PerAddress)
    logs = textbox_page.get_logs()
    assert logs.text.__contains__(FullNameForTest)
    assert logs.text.__contains__(MyEmail)
    assert logs.text.__contains__(CurAddress)
    assert logs.text.__contains__(PerAddress)

def test_select_in_the_checkbox(driverFixture):
    checkbox_page = CheckBoxPage(driverFixture)
    main_page = MainPage(driverFixture)
    checkbox_page.go_to_site()
    main_page.go_to_elements()
    checkbox_page.fill_checkboxes()
    filling = checkbox_page.get_filling()
    assert filling.text.__contains__("Commands")
    assert filling.text.__contains__("Workspace")
    assert filling.text.__contains__("Excel File.doc")

def test_selection_radiobutton(driverFixture):
    radiobutton_page = RadioButtonPage(driverFixture)
    main_page = MainPage(driverFixture)
    radiobutton_page.go_to_site()
    main_page.go_to_elements()
    radiobutton_page.click_on_radio_button()
    assert not radiobutton_page.click_on_enabled().is_enabled()
    radiobutton_page.click_on_impressive()
    logs = radiobutton_page.get_logs()
    assert logs.text.__contains__("Impressive")

def test_buttons(driverFixture):
    third_click_count = 3
    right_click_count = 2
    dynamic_click_count = 2

    buttons_page = ButtonsPage(driverFixture)
    main_page = MainPage(driverFixture)
    buttons_page.go_to_site()
    main_page.go_to_elements()
    text1 = buttons_page.click_on_n_time(third_click_count)
    assert text1.__contains__(str(third_click_count))
    assert text1.__contains__("You have clicked")
    text2 = buttons_page.click_on_right_click(right_click_count)
    assert text2.__contains__(str(right_click_count))
    assert text2.__contains__("You have right clicked")
    text3 = buttons_page.click_on_double_click()
    assert text3.__contains__("You have double clicked")
    text4 = buttons_page.click_on_dynamic_click(dynamic_click_count)
    assert text4.__contains__(str(dynamic_click_count))
    assert text4.__contains__("You have dynamically clicked")

def test_webtables(driverFixture):
    first_name = "li"
    full_name = "ah"
    age = 23
    email = "li@mail.ru"
    salary = 100
    depart = "IT"
    name = "li"
    webtables_page = WebTablesPage(driverFixture)
    main_page = MainPage(driverFixture)
    webtables_page.go_to_site()
    main_page.go_to_elements()
    webtables_page.add_new_employee(first_name,full_name, age,email,salary,depart)
    assert webtables_page.get_logs()[0].__contains__(first_name)
    assert webtables_page.get_logs()[0].__contains__(full_name)
    assert webtables_page.get_logs()[1].__contains__(str(age))
    assert webtables_page.get_logs()[2].__contains__(email)
    assert webtables_page.get_logs()[3].__contains__(str(salary))
    assert webtables_page.get_logs()[4].__contains__(depart)
    webtables_page.by_name(name)
    assert webtables_page.get_logs()[0].__contains__(name)
    webtables_page.delete_add()
    assert len(webtables_page.get_rows_in_table()) == 0

def test_widgets(driverFixture):
    color1 = ("bl","Blue")
    color2 = ("b", "Brown")
    color3 = ("g", "Gray")
    widgets_page = WidgetsPage(driverFixture)
    main_page = MainPage(driverFixture)
    widgets_page.go_to_site()
    main_page.go_to_widgets()
    widgets_page.search_a_single_color(color1[0])
    assert widgets_page.single_by_value() == color1[1]
    widgets_page.search_a_brown_color(color2[0])
    assert widgets_page.get_log_brown() == color2[1]
    widgets_page.search_a_gray_color(color3[0])
    assert widgets_page.get_log_gray() == color3[1]

