"""Модуль содержит методы для взаимодействия с страницей HomePage"""
import json

from locators import home_page_locators

from pages.base_page import BasePage


class HomePage(BasePage):
    def click_on_button(self, locators):
        """Функция нажимает на кнопку"""
        self.element_is_clickable(locators).click()

    def get_text_response(self):
        """Функция получает текст из поля с ответом"""
        output_response = self.element_is_present(home_page_locators.OUTPUT_RESPONSE_FIELD).text
        return json.loads(output_response)

    def get_status_code(self):
        """Функция получает статус код из поля"""
        return self.element_is_present(home_page_locators.OUTPUT_STATUS_CODE_TXT).text

    def get_endpoint(self):
        """Функция получает endpoint из поля"""
        return self.element_is_present(home_page_locators.ENDPOINT_TXT).text

    def get_body(self):
        """Функция получает и строит словарь из поля"""
        body = {}
        keys = self.elements_are_presents(home_page_locators.REQUEST_KEY_TXT)
        strings = self.elements_are_presents(home_page_locators.REQUEST_STRING_TXT)
        for i in range(len(keys)):
            body[keys[i].text.strip(':"')] = strings[i].text.strip('"')
        return body

    def get_method(self, locator):
        """Функция получает method из поля"""
        return self.element_is_present(locator).get_attribute("data-http").upper()
