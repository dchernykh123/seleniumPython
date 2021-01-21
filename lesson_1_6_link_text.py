from selenium import webdriver
import time
import math

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/find_link_text")
    result = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = driver.find_element_by_link_text(result)
    link.click()
    input1 = driver.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name("city")
    input3.send_keys("Taganrog")
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")
    button = driver.find_element_by_xpath("/html/body/div/form/button")
    button.click()
finally:
    time.sleep(30)
    driver.quit()
