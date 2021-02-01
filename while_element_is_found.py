#1
from selenium.common.exceptions import NoSuchElementException

found = False
while not found:
    try:
        link = driver.find_element_by_xpath(linkAddress)
        found = True
    except NoSuchElementException:
        time.sleep(2)
#2
elementlist = []
found = False
while not found:
    try:
        element_ = browser.find_element_by_xpath("//*[@class='class' and (contains(text(),'Optional-text-contain'))]")
        if element_.is_displayed():
            value = element_.find_element_by_css_selector("*")
            elementlist.append(value.text)
            print("Element: " + value.text)
            found = True
    except NoSuchElementException:
        elementlist.append("N/A")
        print("Element: N/A")
        found = True