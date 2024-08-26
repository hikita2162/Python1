import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL для магазина
SHOP_URL = "https://www.saucedemo.com/"

# Данные для авторизации и оформления заказа
user_name = "standard_user"
password = "secret_sauce"
first_name = "Nikita"
last_name = "dogadin"
postal_code = "601500"
expected_sum = "58.29"

class BasePage:
    """
    Базовый класс для всех страниц.
    Содержит общие методы для работы с элементами на странице, такие как клик и ввод текста.
    """

    def __init__(self, driver):
        """
        Инициализация базовой страницы.
        :param driver: объект веб-драйвера Selenium.
        """
        self.driver = driver

    def find_and_click(self, by_locator):
        """
        Поиск элемента и выполнение клика.
        :param by_locator: локатор элемента (тип и значение).
        """
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_locator)).click()

    def find_and_type(self, by_locator, text):
        """
        Поиск элемента и ввод текста.
        :param by_locator: локатор элемента (тип и значение).
        :param text: текст, который необходимо ввести.
        """
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        """
        Поиск элемента и получение текста.
        :param by_locator: локатор элемента (тип и значение).
        :return: текст элемента.
        """
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).text.strip()


class LoginPage(BasePage):
    """
    Класс для страницы логина.
    Содержит методы для открытия страницы и авторизации пользователя.
    """

    def open(self):
        """
        Открывает страницу логина.
        """
        self.driver.get(SHOP_URL)

    def sign_in(self, username=user_name, password=password):
        """
        Выполняет авторизацию пользователя.
        :param username: имя пользователя (по умолчанию 'standard_user').
        :param password: пароль (по умолчанию 'secret_sauce').
        """
        self.find_and_type((By.CSS_SELECTOR, '#user-name'), username)
        self.find_and_type((By.CSS_SELECTOR, '#password'), password)
        self.find_and_click((By.CSS_SELECTOR, '#login-button'))


class ProductsPage(BasePage):
    """
    Класс для страницы с товарами.
    Содержит методы для добавления товаров в корзину и перехода в корзину.
    """

    def add_to_cart(self):
        """
        Добавляет указанные товары в корзину.
        """
        self.find_and_click((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'))
        self.find_and_click((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt'))
        self.find_and_click((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie'))

    def go_to_cart(self):
        """
        Переходит на страницу корзины.
        """
        self.find_and_click((By.CSS_SELECTOR, '.shopping_cart_link'))


class CheckoutPage(BasePage):
    """
    Класс для страницы оформления заказа.
    Содержит метод для начала оформления заказа.
    """

    def checkout_click(self):
        """
        Начинает процесс оформления заказа.
        """
        self.find_and_click((By.CSS_SELECTOR, '#checkout'))


class PersonalInfoPage(BasePage):
    """
    Класс для страницы ввода персональных данных.
    Содержит метод для заполнения формы с личной информацией.
    """

    def make_checkout(self, first_name, last_name, postal_code):
        """
        Заполняет форму с личной информацией и завершает оформление заказа.
        :param first_name: имя.
        :param last_name: фамилия.
        :param postal_code: почтовый индекс.
        """
        self.find_and_type((By.CSS_SELECTOR, '#first-name'), first_name)
        self.find_and_type((By.CSS_SELECTOR, '#last-name'), last_name)
        self.find_and_type((By.CSS_SELECTOR, '#postal-code'), postal_code)
        self.find_and_click((By.CSS_SELECTOR, '#continue'))
        # Удален клик по кнопке "Finish", чтобы не переходить на другую страницу


class OverviewPage(BasePage):
    """
    Класс для страницы обзора заказа.
    Содержит методы для получения итоговой суммы.
    """

    def get_total_amount(self):
        """
        Возвращает итоговую сумму заказа.
        :return: итоговая сумма в виде строки.
        """
        total_text = self.get_text((By.CSS_SELECTOR, '.summary_total_label'))
        print(f"Total amount found: {total_text}")  # Отладочная информация
        return total_text.replace("Total: $", "").strip()


@pytest.fixture
def browser():
    """
    Фикстура для создания и закрытия экземпляра веб-драйвера.
    :return: объект веб-драйвера Selenium.
    """
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_complete_purchase(browser):
    """
    Тестирует процесс покупки товаров на сайте.
    """
    login_page = LoginPage(browser)
    products_page = ProductsPage(browser)
    checkout_page = CheckoutPage(browser)
    personal_info_page = PersonalInfoPage(browser)
    overview_page = OverviewPage(browser)

    login_page.open()
    login_page.sign_in()

    products_page.add_to_cart()
    products_page.go_to_cart()

    checkout_page.checkout_click()

    personal_info_page.make_checkout(first_name, last_name, postal_code)

    total_amount = overview_page.get_total_amount()
    assert total_amount == expected_sum, f"Expected '{expected_sum}', but got '{total_amount}'"

    # Клик по кнопке "Finish" убран, чтобы не изменять страницу перед проверкой итоговой суммы
