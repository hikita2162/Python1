from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:


    def __init__(self,browser):
        self.browser = browser

    def set_delay(self, delay):
        self.browser.find_element(By.ID, "delay").clear()
        self.browser.find_element(By.ID, "delay").send_keys(delay)

    def press_buttons(self, digit):
        self.browser.find_element(By.XPATH, f"//span[text() = '{digit}']").click()

    def wait(self):
        WebDriverWait(self.browser, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

    def check_result(self):
        return self.browser.find_element(By.CLASS_NAME, "screen").text