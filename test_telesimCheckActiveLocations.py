from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://telesim.dunice-testing.com/auth/login"

class TestClickOnStrign():
    def test_login(self, browser):
        browser.get(link)
        browser.implicitly_wait(5)
        input1 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[1]/div/div[1]/div/input")
        input2 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[2]/div/div[1]/div/input")
        input1.send_keys("operator1@mail.com")
        input2.send_keys("QWEqwe123")
        button1 = browser.find_element_by_css_selector("[type = 'button']")
        button1.click()
        #expectedString = WebDriverWait(browser, 5).until(EC.presence_of_element_located(By.XPATH, "/html/body/div[1]/div/div/div/nav/div[1]/div[1]/span"))
        #expectedStringText = expectedString.text
        #if "Telesim Inc." in expectedStringText:
            #assert "dashboard" in browser.current_url, "Login error"
        time.sleep(3)
        assert "dashboard" in browser.current_url, "Login error"
    def test_check_active_status_in_locations(self, browser):
        browser.get("https://telesim.dunice-testing.com/staff/locations")
        status2 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[3]/span")
        status2_text = status2.text
        country1_edit = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/main/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[1]")
        country1_edit.click()
        edit_button1 = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div/div/button")
        edit_button1.click()
        # status1 = browser.find_element_by_xpath(
        #     "/html/body/div[1]/div/div[1]/div/main/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[3]/span")
        # status1_text = status1.text
        country2_edit = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/main/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]")
        country2_edit.click()
        checkbox1 = browser.find_element_by_css_selector("[for='custom-checkbox-60']")
        checkbox1.click()
        edit_button2 = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div[4]/div/div/div[2]/div[2]/div/div[1]/div/button")
        edit_button2.click()
        time.sleep(2)
        status3 = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/main/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[3]/span")
        status3_text = status3.text
        assert status1_text not in status3_text, "Checkbox is not worked"
        # country1_edit = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[1]")
        # country1_edit.click()
        # edit_button1 = browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div/div/button")
        # edit_button1.click()
        # status1 = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[3]/span")
        # status1_text = status1.text
        # status2 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[3]/span")
        # status2_text = status2.text
        # if status2_text == "Active":
        #     country2_edit = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]")
        #     country2_edit.click()
        #     checkbox1 = browser.find_element_by_css_selector("[for='custom-checkbox-60']")
        #     checkbox1.click()
        #     edit_button2 = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[2]/div/div[1]/div/button")
        #     edit_button2.click()
        #     time.sleep(1)
        #     status3 = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[3]/span")
        #     status3_text = status3.text
        #     assert status1_text not in status3_text, "Checkbox is not worked"
        # elif status2_text == "Inactive":
        #     country2_edit = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]")
        #     country2_edit.click()
        #     checkbox1 = browser.find_element_by_css_selector("[for='custom-checkbox-60']")
        #     checkbox1.click()
        #     edit_button2 = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[2]/div/div[1]/div/button")
        #     edit_button2.click()
        #     time.sleep(1)
        #     status3 = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[3]/span")
        #     status3_text = status3.text
        #     assert status1_text in status3_text, "Checkbox is not worked"


