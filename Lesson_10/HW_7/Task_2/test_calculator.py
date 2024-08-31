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

from HW_7.Task_1.Page import Page
from HW_7.Task_2.calculator import Calculator


@pytest.fixture()
def chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
@allure.title("Сумма чисел")
@allure.description("Ввод чисел в форму")
@allure.feature("Fill form")
@allure.severity("blocker")
def test_calculator(chrome):

    chrome.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator = Calculator(chrome)
    calculator.set_delay(1)
    with allure.step("Проверить результат"):
        calculator.press_buttons("7")
        calculator.press_buttons("+")
        calculator.press_buttons("8")
        calculator.press_buttons("=")
        calculator.wait()
    with allure.step("Проверить результат"):
        assert calculator.check_result() == "15"