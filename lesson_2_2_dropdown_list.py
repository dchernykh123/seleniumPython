from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/selects1.html")
    num1 = driver.find_element_by_id("num1")
    y = num1.text
    num2 = driver.find_element_by_id("num2")
    z = num2.text
    def calc(y, z):
        return str(int(y) + int(z))
    y = calc(y, z)
    select1 = Select(driver.find_element_by_id("dropdown"))
    select1.select_by_value(y)
    button1 = driver.find_element_by_class_name("btn-default")
    button1.click()
finally:
    time.sleep(15)
    driver.quit()
