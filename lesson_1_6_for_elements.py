from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/huge_form.html")
    elements = driver.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("qwe")
    button = driver.find_element_by_xpath("/html/body/div/form/button")
    button.click()
finally:
    time.sleep(30)
    driver.quit()
