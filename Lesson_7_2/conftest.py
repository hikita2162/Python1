import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignor-certificate-errors')

@pytest.fixture(scope="module")
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    