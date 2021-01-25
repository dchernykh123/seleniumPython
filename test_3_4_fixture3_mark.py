from selenium import webdriver
import pytest

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

#автозапуск при каждом тесте
@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")

class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
# запуск pytest -s -v -m smoke test_3_4_fixture3_mark.py
# pytest -s -v -m "not smoke" test_fixture8.py
# pytest -s -v -m "smoke or/and regression" test_fixture8.py