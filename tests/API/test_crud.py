import allure
import pytest

from utils.validation import *
from utils.allure_attach import *
from api.request_regres_in import *

payload_create_user = [
    {
        'user_data': {
            "name": "morpheus",
            "job": "leader"
        }
    }
]

payload_update_user = [{
    'id': 2,
    'user_data': {
        "name": "morpheus",
        "job": "zion resident"
    }
}
]

payload_delete_user = [{
    'id': 2
}]


@pytest.mark.API
@allure.epic("API")
@allure.suite("CRUD")
@allure.feature("CRUD пользователя")
class TestCRUD:
    @allure.tag('Positive')
    @allure.title("Проверка создания пользователя.")
    @allure.story("Создание пользователя")
    @pytest.mark.parametrize('payload', payload_create_user)
    def test_create_user(self, payload):
        user_data = payload['user_data']
        response = create_user(payload=user_data)
        allure_attach_responce(response)
        with allure.step("Проверка кода ответа."):
            assert response.status_code == 201, "Статус код не 201"
        with allure.step("Проверка схемы ответа."):
            assert validate_json_schema(response.json(), get_json_schema('crud_schemas/create_user_schema.json'))
        with allure.step("Проверка имени в ответе."):
            assert response.json()['name'] == user_data['name'], "Имя в ответе не совпадает"
        with allure.step("Проверка должности в ответе."):
            assert response.json()['job'] == user_data['job'], "Должность в ответе не совпадает"

    @allure.tag('Positive')
    @pytest.mark.parametrize('payload', payload_update_user)
    @allure.title("Проверка изменения пользователя. (PUT)")
    @allure.story("Изменение пользователя (PUT)")
    def test_update_user_put(self, payload):
        id_user, user_data = payload['id'], payload['user_data']
        response = update_put_user(id_user=id_user, payload=user_data)
        allure_attach_responce(response)
        with allure.step("Проверка кода ответа."):
            assert response.status_code == 200, "Статус код не 200"
        with allure.step("Проверка схемы ответа."):
            assert validate_json_schema(response.json(), get_json_schema('crud_schemas/update_user_schema.json'))
        with allure.step("Проверка имени в ответе."):
            assert response.json()['name'] == user_data['name'], "Имя в ответе не совпадает"
        with allure.step("Проверка должности в ответе."):
            assert response.json()['job'] == user_data['job'], "Должность в ответе не совпадает"

    @allure.tag('Positive')
    @pytest.mark.parametrize('payload', payload_update_user)
    @allure.title("Проверка изменения пользователя. (PATCH)")
    @allure.story("Изменение пользователя (PATCH)")
    def test_update_user_patch(self, payload):
        id_user, user_data = payload['id'], payload['user_data']
        response = update_patch_user(id_user=id_user, payload=user_data)
        allure_attach_responce(response)
        with allure.step("Проверка кода ответа."):
            assert response.status_code == 200, "Статус код не 200"
        with allure.step("Проверка схемы ответа."):
            assert validate_json_schema(response.json(), get_json_schema('crud_schemas/update_user_schema.json'))
        with allure.step("Проверка имени в ответе."):
            assert response.json()['name'] == user_data['name'], "Имя в ответе не совпадает"
        with allure.step("Проверка должности в ответе."):
            assert response.json()['job'] == user_data['job'], "Должность в ответе не совпадает"

    @allure.tag('Positive')
    @pytest.mark.parametrize('payload', payload_delete_user)
    @allure.title("Проверка удаления пользователя.")
    @allure.story("Удаление пользователя")
    def test_delete_user(self, payload):
        id_user = payload['id']
        response = delete_user(id_user=id_user)
        allure_attach_responce(response)
        with allure.step("Проверка кода ответа."):
            assert response.status_code == 204, "Статус код не 204"
