import allure
import pytest

from utils.validation import *
from utils.allure_attach import *
from api.request_regres_in import *

payload_user_list = [
    {
        'page': 1
    },
    {
        'page': 2
    }
]

payload_get_user = [
    {
        'id': 2,
        'negative_id': 23
    },
    {
        'id': 4,
        'negative_id': 13
    }
]

payload_get_delay_user = [
    {
        'delay': 1
    },
    {
        'delay': 2
    }
]


@pytest.mark.API
@allure.epic("API")
@allure.suite("Users")
@allure.feature("Получение пользователей")
class TestUsers:
    @pytest.mark.parametrize('payload', payload_user_list)
    @allure.title("Проверка получения списка пользователей")
    @allure.story("Получение списка пользователей")
    def test_get_user_list(self, payload):
        page = payload['page']
        response = get_list_users(params={'page': page})
        allure_attach_responce(response)
        with allure.step("Проверка кода ответа."):
            assert response.status_code == 200, "Статус код не 200"
        with allure.step("Проверка схемы ответа."):
            assert validate_json_schema(response.json(), get_json_schema('user_list_schema.json'))
        with allure.step("Проверка номера страницы в ответе"):
            assert response.json()['page'] == page, 'Неверная страница'

    @pytest.mark.parametrize('payload', payload_get_user)
    @allure.title("Проверка получения пользователя")
    @allure.story("Получение пользователя")
    def test_get_user(self, payload):
        id_user = payload['id']
        response = get_user(id_user=id_user)
        allure_attach_responce(response)
        with allure.step("Проверка кода ответа."):
            assert response.status_code == 200, "Статус код не 200"
        with allure.step("Проверка схемы ответа."):
            assert validate_json_schema(response.json(), get_json_schema('user_schema.json'))
        with allure.step("Проверка id пользователя в ответе"):
            assert response.json()['data']['id'] == id_user, 'Неверный id пользователя'

    @pytest.mark.parametrize('payload', payload_get_delay_user)
    @allure.title("Проверка задержки получения списка пользователей")
    @allure.story("Получение списка пользователей c задержкой ")
    def test_get_user_with_delay(self, payload):
        delay = payload['delay']
        response = get_list_users(params={'delay': delay})
        with allure.step("Проверка кода ответа."):
            assert response.status_code == 200, "Статус код не 200"
        with allure.step("Проверка схемы ответа."):
            assert validate_json_schema(response.json(), get_json_schema('user_list_schema.json'))
        with allure.step("Проверка задержки ответа"):
            assert int(response.elapsed.total_seconds()) == delay, "Выставленная задержка не соответствует реальной."

    @pytest.mark.parametrize('payload', payload_get_user)
    @allure.title("Проверка получения пользователя (Негативный)")
    @allure.tag("Negative")
    @allure.story("Получение пользователя с несуществующим id")
    def test_get_user_negative(self, payload):
        id_user = payload['negative_id']
        response = get_user(id_user=id_user)
        allure_attach_responce(response)
        with allure.step("Проверка кода ответа."):
            assert response.status_code == 404, "Статус код не 404"
        with allure.step("Проверка схемы ответа."):
            assert validate_json_schema(response.json(), get_json_schema('empty_schema.json'))
