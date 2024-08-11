from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from conf import *
from time import sleep


def test_data_types_form(chrome_browser):
    chrome_browser.get(URL_1)
    from_data = {
         "first-name": first_name,
         "last-name": last_name,
         "address": address,
         "e-mail": email,
         "phone": phone,
         "zip-code": zip_code,
         "city": city,
         "country": country,
         "job-position": job_position,
         "company": company
    }
    
    for field_name, value in from_data.items():
        chrome_browser.find_element(By.NAME,field_name).send_keys(value)

    WebDriverWait(chrome_browser, 40, 0.1).until(
        EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    sleep(2)

    field_classes = {
        "zip-code": "danger",
        "first-name": "success",
        "last-name": "success",
        "address": "success",
        "e-mail": "success",
        "phone": "success",
        "city": "success",
        "country": "success",
        "job-position": "success",
        "company": "success"
    }

    for field_id, class_name in field_classes.items():
        assert class_name in chrome_browser.find_element(
            By.ID, field_id).get_attribute("class")
        
