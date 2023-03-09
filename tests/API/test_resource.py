import allure
import pytest

from utils.validation import *
from utils.allure_attach import *
from api.request_regres_in import *

payload_get_resources = [
    {
        'id': 1,
        'negative_id': 23
    },
    {
        'id': 12,
        'negative_id': 0
    },
]

@pytest.mark.API
@allure.epic("API")
@allure.suite("Resource")
@allure.feature("Получение ресурсов")
@allure.epic("API")
class TestResource:
    @allure.tag('Positive')
    @allure.title("Проверка получения списка ресурсов")
    @allure.story("Получение списка ресурсов")
    def test_get_unknown_list(self):
        response = get_list_resources()
        allure_attach_responce(response)
        with allure.step("Проверка кода ответа."):
            assert response.status_code == 200, "Статус код не 200"
        with allure.step("Проверка схемы ответа."):
            assert validate_json_schema(response.json(), get_json_schema('resource_list_schema.json'))

    @pytest.mark.parametrize('payload', payload_get_resources)
    @allure.title("Проверка получения ресурса")
    @allure.story("Получение ресурсов c существующим id")
    @allure.tag('Positive')
    def test_get_resource(self, payload):
        id_resource = payload['id']
        response = get_resource(id_resource=id_resource)
        allure_attach_responce(response)
        with allure.step("Проверка кода ответа."):
            assert response.status_code == 200, "Статус код не 200"
        with allure.step("Проверка схемы ответа."):
            assert validate_json_schema(response.json(), get_json_schema('resource_schema.json'))
        with allure.step("Проверка id в ответе."):
            assert response.json()['data']['id'] == id_resource, "Неверный id ресурса"

    @pytest.mark.parametrize('payload', payload_get_resources)
    @allure.title("Проверка получения ресурса (Негативный)")
    @allure.tag("Negative")
    @allure.story("Получение ресурсов c несуществующим id")
    def test_get_resource_negative(self, payload):
        id_resource = payload['negative_id']
        response = get_resource(id_resource=id_resource)
        allure_attach_responce(response)
        with allure.step("Проверка кода ответа."):
            assert response.status_code == 404, "Статус код не 404"
        with allure.step("Проверка схемы ответа."):
            assert validate_json_schema(response.json(), get_json_schema('empty_schema.json'))
