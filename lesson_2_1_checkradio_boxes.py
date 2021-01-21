from selenium import webdriver
import time
import math

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/math.html")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = driver.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = driver.find_element_by_id("answer")
    input1.send_keys(y)
    box1 = driver.find_element_by_css_selector("[for = 'robotCheckbox']")
    box1.click()
    # Проверка на наличие атрибута checked
    radioPeople = driver.find_element_by_id("peopleRule")
    people_checked = radioPeople.get_attribute("checked")
    assert people_checked is not None, "People radio is NOT selected by default"
    radioRobots = driver.find_element_by_id("robotsRule")
    people_checked = radioRobots.get_attribute("checked")
    assert people_checked is None, "People radio is selected by default"
    #
    radio1 = driver.find_element_by_css_selector("[for = 'robotsRule']")
    radio1.click()
    button1 = driver.find_element_by_class_name("btn-default")
    button1.click()
finally:
    time.sleep(15)
    driver.quit()
