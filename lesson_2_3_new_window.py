from selenium import webdriver
import time
import math

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/redirect_accept.html")
    button1 = driver.find_element_by_class_name("btn-primary")
    button1.click()
    #current_window = driver.current_window_handle #текущее окно
    first_window = driver.window_handles[0]
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    num1 = driver.find_element_by_id("input_value")
    x = num1.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    input1 = driver.find_element_by_id("answer")
    input1.send_keys(y)
    button1 = driver.find_element_by_class_name("btn-primary")
    button1.click()
finally:
    time.sleep(15)
    driver.quit()
