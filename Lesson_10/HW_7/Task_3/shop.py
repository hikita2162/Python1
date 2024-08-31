from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Shop:

    def __init__(self, browser):
        self.browser = browser

    def fill_fields(self, field, value):
        self.browser.find_element(By.ID, field).send_keys(value)

    def click_button(self, button):
        self.browser.find_element(By.ID, f'{button}').click()

    def check_result(self):
        return self.browser.find_element(By.CLASS_NAME, "summary_total_label").text