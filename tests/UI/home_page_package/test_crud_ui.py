import allure
import pytest

from utils import custom_asserts
import locators.home_page_locators as hpl
from api.custom_request import send_custom_request

@allure.epic("UI")
@allure.feature("CRUD")
@allure.suite("CRUD")
@pytest.mark.WEB
class TestCRUD:
    @allure.title("Проверка кнопки создания пользователя")
    @allure.story("Проверка создания пользователя")
    @allure.tag("Positive")
    def test_create_user(self, hp):
        with allure.step("Нажатие на кнопку"):
            hp.click_on_button(hpl.CREATE_USER_BTN)
        response = send_custom_request(method=hp.get_method(hpl.CREATE_USER_BTN),
                                       endpoint=hp.get_endpoint(),
                                       data=hp.get_body())
        with allure.step("Проверка статус кода"):
            assert response.status_code == int(hp.get_status_code()), "Различный статус код"
        with allure.step("Сравнение ответа API и WEB"):
            custom_asserts.compare_dict(response.json(), hp.get_text_response(), ['id', 'createdAt'], "Ответы различны")

    @allure.tag("Positive")
    @pytest.mark.parametrize('locator_btn, method', (
            (hpl.UPDATE_USER_PUT_BTN, 'PUT'),
            (hpl.UPDATE_USER_PATCH_BTN, 'PATCH')))
    def test_update_user(self, hp, locator_btn, method):
        allure.dynamic.story(f"Проверка обновления пользователя ({method})")
        allure.dynamic.title(f"Проверка кнопки обновления пользователя ({method})")
        with allure.step("Нажатие на кнопку"):
            hp.click_on_button(locator_btn)
        response = send_custom_request(method=hp.get_method(locator_btn),
                                       endpoint=hp.get_endpoint(),
                                       data=hp.get_body())
        with allure.step("Проверка статус кода"):
            assert response.status_code == int(hp.get_status_code()), "Различный статус код"
        with allure.step("Сравнение ответа API и WEB"):
            custom_asserts.compare_dict(response.json(), hp.get_text_response(), ['updatedAt'], "Ответы различны")

    @allure.title("Проверка кнопки удаления пользователя")
    @allure.story("Проверка удаления пользователя")
    @allure.tag("Positive")
    def test_delete_user(self, hp):
        with allure.step("Нажатие на кнопку"):
            hp.click_on_button(hpl.DELETE_USER_BTN)
        response = send_custom_request(method=hp.get_method(hpl.DELETE_USER_BTN),
                                       endpoint=hp.get_endpoint())
        assert response.status_code == int(hp.get_status_code())
