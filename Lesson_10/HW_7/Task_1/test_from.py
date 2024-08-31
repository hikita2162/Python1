import allure
from selenium import webdriver

from time import sleep


import pytest
from selenium import webdriver  # импорт драйвера для взаимодействия с браузером

from Page import Page


@pytest.fixture()
def chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Заполнить форму")
@allure.description("Заполнить форму, нажать подтвердить и проверить, что система указывает цветом, если обязательное поле не заполнено")
@allure.feature("Fill form")
@allure.severity("blocker")
def test_form(chrome):
    chrome.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    page = Page(chrome)
    with allure.step("Заполнить поля"):
        page.fill_fields("last-name", "Иван")
        page.fill_fields("first-name", "Петров")
        page.fill_fields("address", "Аграрная, 12-3")
        page.fill_fields("e-mail", "test@skypro.ru")
        page.fill_fields("phone", "+79850009911")
        page.fill_fields("city", "Москва")
        page.fill_fields("country", "Россия")
        page.fill_fields("job-position", "QA")
        page.fill_fields("company", "SkyPro")
        page.fill_fields("company", "SkyPro")
    with allure.step("Нажать submit"):
        page.click_submit()
    with allure.step("Проверить результат"):
        assert "danger" in page.check_class("zip-code")
        assert "success" in page.check_class("first-name")
        assert "success" in page.check_class("last-name")
        assert "success" in page.check_class("address")
        assert "success" in page.check_class("e-mail")
        assert "success" in page.check_class("phone")
        assert "success" in page.check_class("city")
        assert "success" in page.check_class("country")
        assert "success" in page.check_class("job-position")
        assert "success" in page.check_class("company")
    chrome.quit()