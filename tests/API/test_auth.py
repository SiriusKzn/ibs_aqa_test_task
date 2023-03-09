import pytest

from utils.validation import *
from utils.allure_attach import *
from api.request_regres_in import *


@pytest.mark.API
@allure.epic("API")
@allure.suite("Auth")
@allure.feature("Авторизация пользователя")
class TestAuth:
    @pytest.mark.parametrize('auth_data', [{
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }])
    @allure.title("Проверка регистрации")
    @allure.tag('Positive')
    @allure.story('Регистрация пользователя')
    def test_register(self, auth_data):
        response = register_user(payload=auth_data)
        allure_attach_responce(response)
        with allure.step("Проверка статус кода"):
            assert response.status_code == 200, "Статус код не 200"
        with allure.step("Проверка схемы ответа."):
            assert validate_json_schema(response.json(),
                                        get_json_schema('auth_schemas/register_successful_schema.json'))

    @pytest.mark.parametrize('auth_data', [{
        "email": "sydney@fife"
    }])
    @allure.title("Проверка регистрации(Негативный)")
    @allure.tag("Negative")
    @allure.story('Регистрация пользователя')
    def test_register_negative(self, auth_data):
        response = register_user(payload=auth_data)
        allure_attach_responce(response)
        with allure.step("Проверка статус кода"):
            assert response.status_code == 400, "Статус код не 400"
        with allure.step("Проверка схемы ответа."):
            assert validate_json_schema(response.json(), get_json_schema('auth_schemas/unsuccessful_schema.json'))

    @pytest.mark.parametrize('auth_data', [{
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }])
    @allure.title("Проверка авторизации")
    @allure.story('Логин пользователя')
    @allure.tag("Positive")
    def test_login(self, auth_data):
        response = login_user(payload=auth_data)
        allure_attach_responce(response)
        with allure.step("Проверка статус кода"):
            assert response.status_code == 200, "Статус код не 200"
        with allure.step("Проверка схемы ответа."):
            assert validate_json_schema(response.json(), get_json_schema('auth_schemas/login_successful_schema.json'))

    @pytest.mark.parametrize('auth_data', [{
        "email": "peter@klaven"
    }, {
        "password": "qwerty123"
    }])
    @allure.title("Проверка авторизации (Негативный)")
    @allure.tag("Negative")
    @allure.story('Логин пользователя')
    def test_login_negative(self, auth_data):
        response = login_user(payload=auth_data)
        allure_attach_responce(response)
        with allure.step("Проверка статус кода"):
            assert response.status_code == 400, "Статус код не 400"
        with allure.step("Проверка схемы ответа."):
            assert validate_json_schema(response.json(), get_json_schema('auth_schemas/unsuccessful_schema.json'))
