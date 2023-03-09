

import allure
import pytest

import locators.home_page_locators as hpl
from utils.custom_request import send_custom_request


@allure.epic("UI")
@allure.feature("Получение ресурсов")
@allure.suite("Получение ресурсов")
@pytest.mark.WEB
class TestResource:
    @allure.tag("Positive")
    @allure.title("Проверка кнопки получения листа ресурсов")
    @allure.story("Проверка кнопки получения листа ресурсов")
    def test_list_resources(self, hp):
        with allure.step(f"Нажатие на кнопку"):
            hp.click_on_button(hpl.UNKNOWN_BTN)
        response = send_custom_request(method=hp.get_method(hpl.UNKNOWN_BTN),
                                       endpoint=hp.get_endpoint())
        with allure.step("Проверка статус кода"):
            assert response.status_code == int(hp.get_status_code())
        with allure.step(f"Сравнение ответа API и WEB"):
            assert response.json() == hp.get_text_response()

    @allure.tag("Positive")
    @allure.title("Проверка кнопки получения ресурса")
    @allure.story("Проверка кнопки получения ресурса")
    def test_get_resource_btn(self, hp):
        with allure.step(f"Нажатие на кнопку"):
            hp.click_on_button(hpl.SINGLE_UNKNOWN_BTN)
        response = send_custom_request(method=hp.get_method(hpl.SINGLE_UNKNOWN_BTN),
                                       endpoint=hp.get_endpoint())
        with allure.step("Проверка статус кода"):
            assert response.status_code == int(hp.get_status_code())
        with allure.step(f"Сравнение ответа API и WEB"):
            assert response.json() == hp.get_text_response()

    @allure.tag("Negative")
    @allure.title("Проверка кнопки получения ресурса (Негативной)")
    @allure.story("Проверка кнопки получения ресурса (Негативной)")
    def test_get_resource_btn(self, hp):
        with allure.step(f"Нажатие на кнопку"):
            hp.click_on_button(hpl.SINGLE_UNKNOWN_NEG_BTN)
        response = send_custom_request(method=hp.get_method(hpl.SINGLE_UNKNOWN_NEG_BTN),
                                       endpoint=hp.get_endpoint())
        with allure.step("Проверка статус кода"):
            assert response.status_code == int(hp.get_status_code())
        with allure.step(f"Сравнение ответа API и WEB"):
            assert response.json() == hp.get_text_response()


