from selenium.common.exceptions import NoSuchElementException

def check_exists_by_xpath(xpath):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

self.assertTrue(check_exists_by_xpath(xpath))


# or
def check_exists_by_xpath(xpath):
    return len(webdriver.find_elements_by_xpath(xpath)) > 0