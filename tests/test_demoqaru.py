import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from demoqa_pages.page_object.asyncvalidationformPage import AsyncValidationFormPage
from demoqa_pages.page_object.bookhousePage import BookHousePage
from demoqa_pages.page_object.bookstorePage import BookStorePage
from demoqa_pages.page_object.buttonsPage import ButtonsPage
from demoqa_pages.page_object.checkboxPage import CheckBoxPage
from demoqa_pages.page_object.datepickerPage import DatePickerPage
from demoqa_pages.page_object.dynamictablePage import DynamicTablePage
from demoqa_pages.page_object.explicitwaitPage import ExplicitWaitPage
from demoqa_pages.page_object.formsPage import StudentRegisrtationForm, FormsPage, Hobbies
from demoqa_pages.page_object.interactionsPage import InteracrionsPage
from demoqa_pages.page_object.radiobuttonPage import RadioButtonPage
from demoqa_pages.page_object.redirectPage import RedirectPage
from demoqa_pages.page_object.selectsumPage import SelectSumPage
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

@pytest.fixture(scope="session")
def student_registration_form():
    form = StudentRegisrtationForm()
    form = (form.set_firstname("Liliana").
            set_lastname("Akhatova").
            set_email("lili@mail.ru")
            .set_isFemale(True)
            .set_mobile(89966059445)
            .set_date("07.07.2001")
            .set_curaddress("Saint-P")
            .set_state("LO")
            .set_city("Spb")
            .set_hobbies([Hobbies.MUSIC, Hobbies.READING])
            .set_upload_pictures("Screenshot_36.jpg"))
    return form

@allure.severity(allure.severity_level.NORMAL)
@allure.epic("Тесты demoqa.ru")
@allure.story("Тесты elements")
@allure.feature("Тесты textbox")
@allure.description("Тест проверяет корректность работы раздела textbox")
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

@allure.severity(allure.severity_level.CRITICAL)
@allure.epic("Тесты demoqa.ru")
@allure.story("Тесты elements")
@allure.feature("Тесты checkbox")
@allure.description("Тест проверяет корректность работы раздела checkbox")
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

@allure.severity(allure.severity_level.NORMAL)
@allure.epic("Тесты demoqa.ru")
@allure.story("Тесты elements")
@allure.feature("Тесты radiobutton")
@allure.description("Тест проверяет корректность работы раздела radiobutton")
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

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты demoqa.ru")
@allure.story("Тесты elements")
@allure.feature("Тесты buttons")
@allure.description("Тест проверяет корректность работы раздела buttons")
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

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты demoqa.ru")
@allure.story("Тесты elements")
@allure.feature("Тесты webtables")
@allure.description("Тест проверяет корректность работы раздела webtables")
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


@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты demoqa.ru")
@allure.story("Тесты widgets")
@allure.feature("Тесты widgets")
@allure.description("Тест проверяет корректность работы раздела widgets")
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

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты demoqa.ru")
@allure.story("Тесты interactions")
@allure.feature("Тесты selectable")
@allure.description("Тест проверяет корректность работы раздела interactions")
def test_interactions(driverFixture):
    element_5 = 5
    element_7 = 7
    elements = "1, 4, 8"
    elements_all = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12"
    interactions_page = InteracrionsPage(driverFixture)
    main_page = MainPage(driverFixture)
    interactions_page.go_to_site()
    main_page.go_to_interactions()
    interactions_page.select_elements_5()
    log = interactions_page.get_log_elements()
    assert log.text.__contains__(str(element_5))
    interactions_page.select_elements_7()
    assert log.text.__contains__(str(element_7))
    interactions_page.multiple_selection()
    log_multiple = interactions_page.get_log_multiple()
    assert log_multiple.text.__contains__(elements)
    interactions_page.select_all()
    log_all = interactions_page.get_log_all()
    assert log_all.text.__contains__(elements_all)

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты demoqa.ru")
@allure.story("Тесты bookstore")
@allure.feature("Тесты add_a_book")
@allure.description("Тест проверяет корректность работы раздела bookstore")
def test_add_a_book(driverFixture):
    username = "Liliana"
    password = "lilo225522"
    log_a_book1 = "By Richard E. Silverman"
    log_basket1 = 0
    bookstore_page = BookStorePage(driverFixture)
    main_page = MainPage(driverFixture)
    bookstore_page.go_to_site()
    main_page.go_to_bookstore()
    bookstore_page.register_on_the_site(username, password)
    bookstore_page.add_a_new_book()
    log_a_book = bookstore_page.get_log_a_book()
    assert log_a_book.text.__contains__(log_a_book1)
    bookstore_page.book_and_basket()
    log_basket = bookstore_page.log_basket()
    assert log_basket.text.__contains__(str(log_basket1))

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты demoqa.ru")
@allure.story("Тесты forms")
@allure.feature("Тесты student registration form")
@allure.description("Тест проверяет корректность работы раздела forms")
def test_forms(driverFixture, student_registration_form):
    main_page = MainPage(driverFixture)
    forms_page = FormsPage(driverFixture)
    forms_page.go_to_site()
    main_page.go_to_forms()
    forms_page.register_form(student_registration_form)

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты demoqa.ru")
@allure.story("Тесты date picker")
@allure.feature("Тесты выбора даты")
@allure.description("Тест проверяет корректность работы раздела date picker")
def test_select_a_date(driverFixture):
    log_select = "July 7, 2025"
    log_range = "July 7, 2025 - July 7, 2026"
    main_page = MainPage(driverFixture)
    date_picker = DatePickerPage(driverFixture)
    date_picker.go_to_site()
    main_page.go_to_widgets()
    date_picker.select_a_single_date()
    log_select_a_date = date_picker.log_select_a_date()
    assert log_select_a_date.get_attribute("value").__contains__(log_select)
    date_picker.select_a_range_date()
    log_select_a_range_date = date_picker.log_select_a_range_date()
    assert log_select_a_range_date.get_attribute("value").__contains__(log_range)


@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты demoqa.ru")
@allure.story("Тесты redirect page")
@allure.feature("Тесты решения математического уравнения")
@allure.description("Тест проверяет корректность работы раздела redirect page")
def test_redirect_page(driverFixture):
    right = "Правильно"
    main_page = MainPage(driverFixture)
    redirect_page = RedirectPage(driverFixture)
    redirect_page.go_to_site()
    main_page.go_to_tests()
    redirect_page.math_redirect_test()
    get_log_alert = redirect_page.get_log_alert()
    assert get_log_alert.__contains__(right)


@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты demoqa.ru")
@allure.story("Тесты book house")
@allure.feature("Тесты покупки дома за определенную стоимость")
@allure.description("Тест проверяет корректность работы раздела book house")
def test_book_house(driverFixture):
    right = "Congratulations!"
    main_page = MainPage(driverFixture)
    bookhouse_page = BookHousePage(driverFixture)
    bookhouse_page.go_to_site()
    main_page.go_to_tests()
    bookhouse_page.book_house()
    get_log_alert = bookhouse_page.get_log_alert()
    assert get_log_alert.__contains__(right)


@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты demoqa.ru")
@allure.story("Тесты select sum")
@allure.feature("Тесты выбора из выпадающего списка результата суммы")
@allure.description("Тест проверяет корректность работы раздела select sum")
def test_select_sum(driverFixture):
    right = "Правильно"
    main_page = MainPage(driverFixture)
    selectsum_page = SelectSumPage(driverFixture)
    selectsum_page.go_to_site()
    main_page.go_to_tests()
    selectsum_page.select_sum()
    get_select_sum = selectsum_page.get_select_sum()
    assert get_select_sum.__contains__(right)

@allure.severity(allure.severity_level.MINOR)
@allure.epic("Тесты demoqa.ru")
@allure.story("Тесты explicit wait")
@allure.feature("Тесты заполнения формы и введения кода")
@allure.description("Тест проверяет корректность работы explicit wait")
def test_explicit_wait(driverFixture):
    firstname = "Lil"
    lastname = "Akhatova"
    email = "lili7achatova@gmail.com"
    congratulations = "Поздравляем! Тест успешно пройден!"
    main_page = MainPage(driverFixture)
    explicitwait_page = ExplicitWaitPage(driverFixture)
    explicitwait_page.go_to_site()
    main_page.go_to_tests()
    explicitwait_page.fill_out_the_form(firstname, lastname, email)
    explicitwait_page.check_code()
    log = explicitwait_page.log_after_checking_code()
    assert log.__contains__(congratulations)

def test_validation_form(driverFixture):
    name = "Lili"
    email = "lili7achatova@gmail.com"
    right = "Форма успешно отправлена!"
    main_page = MainPage(driverFixture)
    asyncvalidationform_page = AsyncValidationFormPage(driverFixture)
    asyncvalidationform_page.go_to_site()
    main_page.go_to_tests()
    asyncvalidationform_page.submit_the_form(name, email)
    asyncvalidationform_page.click_on_submit_the_form()
    log = asyncvalidationform_page.get_log_alert()
    assert log.__contains__(right)

def test_invalidation_form(driverFixture):
    name = "Nikita"
    email = "N"
    log1 = "Неверный формат email"
    main_page = MainPage(driverFixture)
    asyncvalidationform_page = AsyncValidationFormPage(driverFixture)
    asyncvalidationform_page.go_to_site()
    main_page.go_to_tests()
    asyncvalidationform_page.submit_the_form(name, email)
    log = asyncvalidationform_page.get_log()
    assert log.__contains__(log1)

def test_dynamictable(driverFixture):
    name1 = "Lili"
    age1 = 20
    email1 = "lili@mail.ru"
    city1 = "Spb"
    main_page = MainPage(driverFixture)
    dynamictable_page = DynamicTablePage(driverFixture)
    dynamictable_page.go_to_site()
    main_page.go_to_tests()
    dynamictable_page.len_table(name1, age1, email1, city1)














