from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    expectedPrice = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button1 = driver.find_element_by_id("book")
    button1.click()
    num1 = driver.find_element_by_id("input_value")
    x = num1.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    input1 = driver.find_element_by_id("answer")
    input1.send_keys(y)
    button2 = driver.find_element_by_id("solve")
    button2.click()
finally:
    time.sleep(15)
    driver.quit()
