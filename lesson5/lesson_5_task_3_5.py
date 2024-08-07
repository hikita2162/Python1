from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:

    driver.get("http://the-internet.herokuapp.com/inputs")
    imput_field = driver.find_element(By.TAG_NAME, "input")
    imput_field.send_keys("1000")
    sleep(2)
    imput_field.clear()
    sleep(1)
    imput_field.send_keys("999")
    sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.quit()
