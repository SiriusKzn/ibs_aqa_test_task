"""Модуль содержит основные методы для взаимодействия с страницами"""
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """Функция открывает страницу по URL"""
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """Функция возвращает видимый элемент, представленный в DOM"""
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_present(self, locator, timeout=5):
        """Функция возвращает элемент, представленный в DOM"""
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_presents(self, locator, timeout=5):
        """Функция возвращает элементы, представленный в DOM"""
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """Функция возвращает элемент, представленный в DOM, доступный для нажатия"""
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def refresh(self, driver):
        """Функция обновляет страницу"""
        driver.refresh()
