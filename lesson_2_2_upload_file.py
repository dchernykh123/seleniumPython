from selenium import webdriver
import time
import os

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/file_input.html")
    input1 = driver.find_element_by_css_selector("[name = 'firstname']")
    input1.send_keys("Dima")
    input2 = driver.find_element_by_css_selector("[name = 'lastname']")
    input2.send_keys("Test")
    input3 = driver.find_element_by_css_selector("[name = 'email']")
    input3.send_keys("qwe@qwe.qwe")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file1 = driver.find_element_by_id("file")
    file1.send_keys(file_path)
    button1 = driver.find_element_by_xpath("/html/body/div/form/button")
    button1.click()
finally:
    time.sleep(15)
    driver.quit()
