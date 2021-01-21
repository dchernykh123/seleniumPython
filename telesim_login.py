import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TelesimLogin(unittest.TestCase):
    def setUp(self):
            self.driver = webdriver.Chrome()
    def test_login_in_telesim(self):
            driver = self.driver
            driver.get("https://telesim.dunice-testing.com/auth/login")
            self.assertIn("multitel-users", driver.title)
            time.sleep(1)
            elem = driver.find_element_by_id("input-14")
            elem.send_keys("operator1@mail.com")
            time.sleep(1)
            elem = driver.find_element_by_id("input-18")
            time.sleep(1)
            elem.send_keys("QWEqwe123")
            time.sleep(1)
            elem.send_keys(Keys.RETURN)
            time.sleep(3)
            assert "dashboard" in driver.current_url
    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
    unittest.main()
