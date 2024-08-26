from Lesson_7_2.sweg_Labs.LoginPage import LoginPage
from Lesson_7_2.sweg_Labs.ProductsPage import ProductsPage
from Lesson_7_2.sweg_Labs.CheckoutPage import CheckoutPage

user_name = "standard_user"
password = "secret_sauce"

first_name = "Nikita"
last_name = "Dogadin"
postol_code = "601500"

sum = "$58.29"

def test_purchase(chrome_browser):
    Login_Page = LoginPage(chrome_browser)
    Login_Page.open()
    Login_Page.sign_in(user_name, password)

    Products_Page = ProductsPage(chrome_browser)
    Products_Page.add_to_cart()
    Products_Page.go_to_cart()
    Products_Page.checkout_click()

    Checkout_Page = CheckoutPage(chrome_browser)
    Checkout_Page.make_checkout(first_name, last_name, postol_code)

    txt = Checkout_Page.check_total()
    assert sum in txt