from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Page:
    def __init__(self,browser):
        self.browser = browser

    def fill_fields(self, field, value):
        self.browser.find_element(By.NAME, field).send_keys(value)
    def click_submit(self):
        WebDriverWait(self.browser, 40, 0.1).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    def check_class(self, field):

        return self.browser.find_element(By.ID, field).get_attribute("class")