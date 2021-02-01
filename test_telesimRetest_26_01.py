from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
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
    def test_click_on_string_for_editing(self, browser):
        packages = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/nav/div[1]/div[2]/div[1]/div[1]")
        packages.click()
        eSIM = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/nav/div[1]/div[2]/div[1]/div[2]/div[3]/div")
        eSIM.click()
        directory = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/nav/div[1]/div[2]/div[1]/div[2]/div[3]/div[2]/div[5]/a")
        directory.click()
        string = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/table/tbody/tr[1]")
        string.click()
        editString = browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/span")
        textEditString = editString.text
        assert textEditString in "Edit Package Period", "Edit window is not open"
    def test_pagination_link_between_user_tables(self, browser):
        browser.get("https://telesim.dunice-testing.com/staff/users/list/user")
        button1 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/main/div/div[2]/div/div/div[2]/div[2]/div[2]/nav/ul/li[3]/button")
        button1.click()
        time.sleep(1)
        operators = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/nav/div[1]/div[2]/a[5]/div[2]")
        operators.click()
        if len(browser.find_elements_by_xpath("/html/body/div[1]/div/div/div/main/div/div[2]/div/div/div[2]/div[1]/table/tbody/tr[1]")) > 0:
            print("OK")
        else:
            raise Exception("Test error! Tables are linked")
        admins = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/nav/div[1]/div[2]/a[6]/div[2]")
        admins.click()
        if len(browser.find_elements_by_xpath("/html/body/div[1]/div/div/div/main/div/div[2]/div/div/div[2]/div[1]/table/tbody/tr[1]")) > 0:
            print("OK")
        else:
            raise Exception("Test error! Tables are linked")
    def test_link_pagination_strings_numbers_between_user_tables(self, browser):
        browser.get("https://telesim.dunice-testing.com/staff/users/list/user")
        numbers_acc = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div/div[2]/div/div/div[2]/div[2]/div[3]/div/div/div/div/div[1]/div[1]/div")
        browser.execute_script("return arguments[0].scrollIntoView(true);", numbers_acc)
        numbers_acc.click()
        numbers_acc_20 = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div")
        numbers_acc_20.click()
        time.sleep(1)
        numbers_acc_20_click = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div/div[2]/div/div/div[2]/div[2]/div[3]/div/div/div/div/div[1]/div[1]/div")
        numbers_acc_20_click_text = numbers_acc_20_click.text
        operators = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/nav/div[1]/div[2]/a[5]/div[2]")
        operators.click()
        strings_numbers_operators = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/main/div/div[2]/div/div/div[2]/div[2]/div[3]/div/div/div/div/div[1]/div[1]/div")
        browser.execute_script("return arguments[0].scrollIntoView(true);", strings_numbers_operators)
        strings_numbers_operators_text = strings_numbers_operators.text
        assert numbers_acc_20_click_text != strings_numbers_operators_text, "Page numbers is equal after changing"

