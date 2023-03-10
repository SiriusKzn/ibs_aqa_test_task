import time

import allure
import pytest

import locators.home_page_locators as hpl
from api.custom_request import send_custom_request

@allure.epic("UI")
@allure.feature("Получение пользователей")
@allure.suite("Получение пользователей")
@pytest.mark.WEB
class TestUsers:
    @allure.tag("Positive")
    @allure.title("Проверка кнопки получения листа пользователей")
    @allure.story("Проверка кнопки получения листа пользователей")
    def test_user_list_button(self, hp):
        with allure.step("Нажатие на кнопку"):
            hp.click_on_button(hpl.LIST_USERS_BTN)
        response = send_custom_request(method=hp.get_method(hpl.LIST_USERS_BTN),
                                       endpoint=hp.get_endpoint())
        with allure.step("Проверка статус кода"):
            assert response.status_code == int(hp.get_status_code())
        with allure.step("Сравнение ответа API и WEB"):
            assert response.json() == hp.get_text_response()

    @allure.tag("Positive")
    @allure.title("Проверка кнопки получения пользователей")
    @allure.story("Проверка получения пользователей")
    def test_get_user_button(self, hp):
        with allure.step("Нажатие на кнопку"):
            hp.click_on_button(hpl.SINGLE_USERS_BTN)
        response = send_custom_request(method=hp.get_method(hpl.SINGLE_USERS_BTN),
                                       endpoint=hp.get_endpoint())
        with allure.step("Проверка статус кода"):
            assert response.status_code == int(hp.get_status_code())
        with allure.step("Сравнение ответа API и WEB"):
            assert response.json() == hp.get_text_response()

    @allure.tag("Negative")
    @allure.title("Проверка кнопки получения пользователей (Негативной)")
    @allure.story("Проверка получения пользователей")
    def test_get_user_neg_button(self, hp):
        with allure.step("Нажатие на кнопку"):
            hp.click_on_button(hpl.SINGLE_USERS_NEG_BTN)
        response = send_custom_request(method=hp.get_method(hpl.SINGLE_USERS_NEG_BTN),
                                       endpoint=hp.get_endpoint())
        with allure.step("Проверка статус кода"):
            assert response.status_code == int(hp.get_status_code())
        with allure.step("Сравнение ответа API и WEB"):
            assert response.json() == hp.get_text_response()

    @allure.tag("Positive")
    @allure.title("Проверка кнопки получения пользователей c задержкой")
    @allure.story("Проверка получения пользователей с задержкой")
    def test_get_user_list_with_delay(self, hp):
        with allure.step("Нажатие на кнопку"):
            hp.click_on_button(hpl.DELAYED_RESPONSE_BTN)
        with allure.step("Измеряем время появления элемента"):
            start_time = time.time()
            hp.element_is_visible(hpl.OUTPUT_RESPONSE_FIELD)
            time_response = time.time() - start_time
            allure.attach(f"Responce Time:{time_response}")
        assert int(time_response) == int(hp.get_endpoint()[-1]), "Время появления элемента не соответствует " \
                                                                 "отправленному"

