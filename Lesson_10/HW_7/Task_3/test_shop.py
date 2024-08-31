import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

from time import sleep


import pytest
from selenium import webdriver  # импорт драйвера для взаимодействия с браузером

from HW_7.Task_3.shop import Shop


@pytest.fixture()
def chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("выполнение входа на сайт")
@allure.description("Выбор, формирование товара")
@allure.feature("Fill form")
@allure.severity("blocker")
def test_shop(chrome):
    chrome.get("https://www.saucedemo.com/")
    shop = Shop(chrome)
    with allure.step("авторизация"):
        shop.fill_fields("user-name", "standard_user")
        shop.fill_fields("password", "secret_sauce")
        shop.click_button("login-button")
    with allure.step("Добавление товаров"):
        shop.click_button("add-to-cart-sauce-labs-backpack")
        shop.click_button("add-to-cart-sauce-labs-bolt-t-shirt")
        shop.click_button("add-to-cart-sauce-labs-onesie")
    with allure.step("вход в корзину"):
        shop.click_button("shopping_cart_container")
    with allure.step("Заполнение данных"):
        shop.click_button("checkout")
        shop.fill_fields("first-name", "Владимир")
        shop.fill_fields("last-name", "Васильев")
        shop.fill_fields("postal-code", "111222")
    with allure.step("Нажатие кнопки результат"):
        shop.click_button("continue")
    with allure.step("Проверить результат"):
        assert shop.check_result()== "Total: $58.29"