from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self,browser):
        self.browser = browser

    def make_checkout(slef, first_name, last_name, postol_code):
        slef.browser.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        slef.browser.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        slef.browser.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postol_code)
        slef.browser.find_element(By.CSS_SELECTOR, '#continue').click()
    
    def check_total(self):
        return self.browser.find_element(By.CSS_SELECTOR, '.summary_total_label').text