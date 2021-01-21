from selenium import webdriver
import time
import math

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/execute_script.html")
    num1 = driver.find_element_by_id("input_value")
    x = num1.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    input1 = driver.find_element_by_id("answer")
    input1.send_keys(y)
    check1 = driver.find_element_by_css_selector("[for = 'robotCheckbox']")
    check1.click()
    radioRobots = driver.find_element_by_css_selector("[for = 'robotsRule']")
    driver.execute_script("return arguments[0].scrollIntoView(true);", radioRobots)
    radioRobots.click()
    button1 = driver.find_element_by_xpath("/html/body/div/form/button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()
finally:
    time.sleep(15)
    driver.quit()
