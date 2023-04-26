from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Driver():
    """Запускает драйвер для браузера Chrome."""

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.open_page()

    def open_page(self):
        """Открывает страницу переданную в объект драйвера."""
        self.driver.get(self.url)

    def get_element(self, locator):
        """Возвращает элемент по CSS селектору."""
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_elements(self, locator):
        """Возвращает список элементов по CSS селектору"""
        return self.driver.find_elements(By.CSS_SELECTOR, locator)

    def select_tab(self, tab_number):
        """Переходит на номер вкладки переданный в tab_number"""
        return self.driver.switch_to.window(self.driver.window_handles[tab_number])

    def hover_on_element(self, element_name):
        """Ховер по элементу"""
        return ActionChains(self.driver).move_to_element(element_name)