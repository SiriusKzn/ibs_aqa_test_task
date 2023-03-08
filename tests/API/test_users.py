import pytest

from utils.http import *
from api.regres_in_requests import *


class TestUsers:

    @pytest.mark.parametrize('page', range(1, 2))
    def test_get_user_list(self, page):
        response = get_list_users(params={'page': page})
        text = response.text
        assert response.status_code == 200, "Статус код не 200"
        assert validate_json_schema(response.json(), get_json_schema('user_list_schema.json'))
        assert response.json()['page'] == page, 'Неверная страница'

    @pytest.mark.parametrize('id', (1, 3, 12))
    def test_get_user(self, id):
        response = get_user(id=id)
        assert response.status_code == 200, "Статус код не 200"
        assert validate_json_schema(response.json(), get_json_schema('user_schema.json'))
        assert response.json()['data']['id'] == id, 'Неверный id пользователя'

    @pytest.mark.parametrize('id', (23, 25, 0))
    def test_get_user_negative(self, id):
        response = get_user(id=id)
        assert response.status_code == 404, "Статус код не 404"
        assert validate_json_schema(response.json(), get_json_schema('empty_schema.json'))



class TestUnknown:
    def test_get_unknown_list(self):
        response = get_list_resources()
        assert response.status_code == 200, "Статус код не 200"
        assert validate_json_schema(response.json(), get_json_schema('resource_list_schema.json'))

    @pytest.mark.parametrize('id', (1, 3, 12))
    def test_get_resource(self, id):
        response = get_resource(id=id)
        assert response.status_code == 200, "Статус код не 200"
        assert validate_json_schema(response.json(), get_json_schema('resource_schema.json'))
        assert response.json()['data']['id'] == id, "Неверный id ресурса"

    @pytest.mark.parametrize('id', (23, 25, 0))
    def test_get_user_negative(self, id):
        response = get_resource(id=id)
        assert response.status_code == 404, "Статус код не 404"
        assert validate_json_schema(response.json(), get_json_schema('empty_schema.json'))
