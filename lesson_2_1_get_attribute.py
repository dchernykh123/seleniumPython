from selenium import webdriver
import time
import math

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/get_attribute.html")
    icon = driver.find_element_by_id("treasure")
    x = icon.get_attribute("valuex")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    input1 = driver.find_element_by_id("answer")
    input1.send_keys(y)
    checkRobot = driver.find_element_by_id("robotCheckbox")
    checkRobot.click()
    radioRobots = driver.find_element_by_id("robotsRule")
    radioRobots.click()
    button = driver.find_element_by_class_name("btn-default")
    button.click()
finally:
    time.sleep(10)
    driver.quit()
