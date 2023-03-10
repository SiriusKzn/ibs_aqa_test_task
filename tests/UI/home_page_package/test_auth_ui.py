import allure
import pytest

import locators.home_page_locators as hpl
from api.custom_request import send_custom_request


@allure.epic("UI")
@allure.feature("Авторизация пользователей")
@allure.suite("Авторизация пользователей")
@pytest.mark.WEB
class TestAuth:

    @allure.story("Проверка логина пользователя")
    @allure.title("Проверка кнопки логина пользователя")
    @allure.tag("Positive")
    def test_login(self, hp):
        with allure.step("Нажатие на кнопку"):
            hp.click_on_button(hpl.LOGIN_BTN)
        response = send_custom_request(method=hp.get_method(hpl.LOGIN_BTN),
                                       endpoint=hp.get_endpoint(),
                                       data=hp.get_body())
        with allure.step("Проверка статус кода"):
            assert response.status_code == int(hp.get_status_code()), "Различный статус код"
        with allure.step("Сравнение ответа API и WEB"):
            assert response.json() == hp.get_text_response(), "Ответы не совпадают"

    @allure.story("Проверка логина пользователя")
    @allure.title("Проверка кнопки логина пользователя (Негативной)")
    @allure.tag("Negative")
    def test_login_negative(self, hp):
        with allure.step("Нажатие на кнопку"):
            hp.click_on_button(hpl.LOGIN_NEG_BTN)
        response = send_custom_request(method=hp.get_method(hpl.LOGIN_NEG_BTN),
                                       endpoint=hp.get_endpoint(),
                                       data=hp.get_body())
        with allure.step("Проверка статус кода"):
            assert response.status_code == int(hp.get_status_code()), "Различный статус код"
        with allure.step("Сравнение ответа API и WEB"):
            assert response.json() == hp.get_text_response(), "Ответы не совпадают"

    @allure.story("Проверка регистрации пользователя")
    @allure.title("Проверка кнопки регистрации пользователя")
    @allure.tag("Positive")
    def test_register(self, hp):
        with allure.step("Нажатие на кнопку"):
            hp.click_on_button(hpl.REGISTER_BTN)
        response = send_custom_request(method=hp.get_method(hpl.REGISTER_BTN),
                                       endpoint=hp.get_endpoint(),
                                       data=hp.get_body())
        with allure.step("Проверка статус кода"):
            assert response.status_code == int(hp.get_status_code()), "Различный статус код"
        with allure.step("Сравнение ответа API и WEB"):
            assert response.json() == hp.get_text_response(), "Ответы не совпадают"

    @allure.story("Проверка регистрации пользователя")
    @allure.title("Проверка кнопки регистрации пользователя (Негативной)")
    @allure.tag("Negative")
    def test_register_negative(self, hp):
        with allure.step("Нажатие на кнопку"):
            hp.click_on_button(hpl.REGISTER_NEG_BTN)
        response = send_custom_request(method=hp.get_method(hpl.REGISTER_NEG_BTN),
                                       endpoint=hp.get_endpoint(),
                                       data=hp.get_body())
        with allure.step("Проверка статус кода"):
            assert response.status_code == int(hp.get_status_code()), "Различный статус код"
        with allure.step("Сравнение ответа API и WEB"):
            assert response.json() == hp.get_text_response(), "Ответы не совпадают"
