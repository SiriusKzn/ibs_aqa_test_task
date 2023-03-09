import allure
import pytest

import locators.home_page_locators as hpl
from utils.custom_request import send_custom_request


@allure.epic("UI")
@allure.feature("Авторизация пользователей")
@allure.suite("Авторизация пользователей")
@pytest.mark.WEB
class TestAuth:
    @pytest.mark.parametrize('locator_btn, allure_data',
                             ([hpl.LOGIN_BTN, {
                                 'tag': 'Positive',
                                 'title': 'Проверка кнопки логина пользователя'
                             }],
                              [hpl.LOGIN_NEG_BTN, {
                                  'tag': 'Negative',
                                  'title': 'Проверка кнопки логина пользователя (Негативный)'
                              }
                               ]))
    def test_login(self, hp, locator_btn, allure_data: dict):
        allure.dynamic.title(allure_data['title'])
        allure.dynamic.tag(allure_data['tag'])
        allure.dynamic.story(allure_data['title'])
        with allure.step("Нажатие на кнопку"):
            hp.click_on_button(locator_btn)
        response = send_custom_request(method=hp.get_method(locator_btn),
                                       endpoint=hp.get_endpoint(),
                                       data=hp.get_body())
        with allure.step("Проверка статус кода"):
            assert response.status_code == int(hp.get_status_code()), "Различный статус код"
        with allure.step("Сравнение ответа API и WEB"):
            assert response.json() == hp.get_text_response(), "Ответы не совпадают"

    @pytest.mark.parametrize('locator_btn, allure_data',
                             ([hpl.REGISTER_BTN, {'tag': 'Positive',
                                                  'title': 'Проверка логина пользователя'}],
                              [hpl.LOGIN_NEG_BTN, {'tag': 'Negative',
                                                   'title': 'Проверка логина пользователя (Негативный)'}]))
    def test_register(self, hp, locator_btn, allure_data: dict):
        allure.dynamic.title(allure_data['title'])
        allure.dynamic.tag(allure_data['tag'])
        allure.dynamic.story(allure_data['title'])
        with allure.step("Нажатие на кнопку"):
            hp.click_on_button(locator_btn)
        response = send_custom_request(method=hp.get_method(locator_btn),
                                       endpoint=hp.get_endpoint(),
                                       data=hp.get_body())
        with allure.step("Проверка статус кода"):
            assert response.status_code == int(hp.get_status_code()), "Различный статус код"
        with allure.step("Сравнение ответа API и WEB"):
            assert response.json() == hp.get_text_response(), "Ответы не совпадают"
