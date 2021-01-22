import unittest
from selenium import webdriver
import time

class test_registration_form(unittest.TestCase):
    def test_reg1(self):
            driver = webdriver.Chrome()
            driver.get("http://suninjuly.github.io/registration1.html")
            input1 = driver.find_element_by_css_selector("[placeholder='Input your first name']")
            input1.send_keys("QWE")
            input2 = driver.find_element_by_css_selector("[placeholder='Input your last name']")
            input2.send_keys("QWE")
            input3 = driver.find_element_by_css_selector("[placeholder='Input your email']")
            input3.send_keys("QWE")
            submit = driver.find_element_by_class_name("btn-default")
            submit.click()
            time.sleep(1)
            welcome_text_elt = driver.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registered" )
            driver.quit()
    def test_reg2(self):
            driver = webdriver.Chrome()
            driver.get("http://suninjuly.github.io/registration2.html")
            input1 = driver.find_element_by_css_selector("[placeholder='Input your first name']")
            input1.send_keys("QWE")
            input2 = driver.find_element_by_css_selector("[placeholder='Input your last name']")
            input2.send_keys("QWE")
            input3 = driver.find_element_by_css_selector("[placeholder='Input your email']")
            input3.send_keys("QWE")
            submit = driver.find_element_by_class_name("btn-default")
            submit.click()
            time.sleep(1)
            welcome_text_elt = driver.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Not registered" )
            driver.quit()

if __name__ == "__main__":
    unittest.main()
