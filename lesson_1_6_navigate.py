from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    input1 = driver.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name("city")
    input3.send_keys("Taganrog")
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")
    time.sleep(0.5)
    button = driver.find_element_by_id("submit_button")
    button.click()
finally:
    time.sleep(20)
    driver.quit()
