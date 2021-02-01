import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\n quit browser...")
    browser.quit()

@pytest.mark.parametrize('param', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_open_links(browser, param):
    link = f"https://stepik.org/lesson/{param}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    answer = str(math.log(int(time.time())))
    input1 = browser.find_element_by_tag_name("textarea")
    input1.send_keys(answer)
    button1 = browser.find_element_by_class_name("submit-submission")
    button1.click()
    correct = browser.find_element_by_class_name("smart-hints__hint")
    text_correct = correct.text
    assert text_correct == "Correct!", "Answer is not correct"
