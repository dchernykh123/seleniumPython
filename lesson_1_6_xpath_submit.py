from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/find_xpath_form")
    elem1 = driver.find_element_by_name("first_name")
    elem1.send_keys("Dima")
    elem2 = driver.find_element_by_name("last_name")
    elem2.send_keys("Testerov")
    elem3 = driver.find_element_by_name("firstname")
    elem3.send_keys("Taganrog")
    elem4 = driver.find_element_by_id("country")
    elem4.send_keys("Russia")
    submit = driver.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
    submit.click()
finally:
    time.sleep(20)
    driver.quit()
