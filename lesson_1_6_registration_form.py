from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/registration1.html")
    input1 = driver.find_element_by_class_name("first")
    input1.send_keys("QWE")
    input2 = driver.find_element_by_class_name("second")
    input2.send_keys("QWE")
    input3 = driver.find_element_by_class_name("third")
    input3.send_keys("QWE")
    submit = driver.find_element_by_class_name("btn-default")
    submit.click()
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text, "Not registered"
finally:
    time.sleep(3)
    driver.quit()
