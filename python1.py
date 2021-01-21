import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Класс теста унаследован от unittest.TestCase.
#Наследование класса TestCase является способом сообщения модулю unittest, что это тест:
class PythonOrgSearch(unittest.TestCase):
    #setUp — это часть инициализации, этот метод будет вызываться перед каждым методом теста,
    #который вы собираетесь написать внутри класса теста.
    def setUp(self):
        self.driver = webdriver.Chrome()
    #Далее описан метод нашего теста. Метод теста всегда должен начинаться с фразы test.
    #Первая строка метода создает локальную ссылку на объект драйвера, созданный методом setUp.
    def test_search_in_python_org(self):
        driver = self.driver
        #Метод driver.get перенаправляет к странице URL в параметре:
        driver.get("http://www.python.org")
        #Следующая строка — это утверждение, что заголовок содержит слово “Python”:
        self.assertIn("Python", driver.title)
        #Поиск эелемента по названию:
        elem = driver.find_element_by_name("q")
        #После этого мы посылаем нажатия клавиш (аналогично введению клавиш с клавиатуры):
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        #Чтобы удостовериться, что мы получили какой-либо результат, добавим утверждение:
        assert "No results found." not in driver.page_source
    #Метод tearDown будет вызван после каждого метода теста. Это метод для действий чистки.
    #В текущем методе реализовано закрытие окна браузера.
    #Вы можете также вызывать метод quit вместо close.
    def tearDown(self):
        self.driver.close()
#Завершающий код — это стандартная вставка кода для запуска набора тестов
#[Сравнение __name__ с "__main__" означает,
#что модуль (файл программы) запущен как отдельная программа:
if __name__ == "__main__":
    unittest.main()
