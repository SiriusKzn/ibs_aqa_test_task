"""Модуль содержит запросы к API"""
import allure
import requests

from config import HOST


USERS = "/api/users/"
UNKNOWN = "/api/unknown/"
REGISTER = "/api/register/"
LOGIN = "/api/login/"


def get_list_users(params: dict, **kwargs):
    """Функция для отправки запроса GET /api/users/"""
    with allure.step("Отправка запроса на получение списка пользователей"):
        response = requests.get(url=f'{HOST}{USERS}', params=params, timeout=5, **kwargs)
    return response


def get_user(id_user: int, **kwargs):
    """Функция для отправки запроса GET /api/users/ с передачей id пользователя"""
    with allure.step(f"Отправка запроса на получение пользователя с id = {id_user}"):
        response = requests.get(url=f'{HOST}{USERS}{id_user}', timeout=5, ** kwargs)
    return response


def get_list_resources(**kwargs):
    """Функция для отправки запроса GET /api/unknown/"""
    with allure.step("Отправка запроса на получение списка ресурсов"):
        response = requests.get(url=f'{HOST}{UNKNOWN}', timeout=5, ** kwargs)
    return response


def get_resource(id_resource, **kwargs):
    """Функция для отправки запроса GET /api/unknown/ с передачей id ресурса"""
    with allure.step(f"Отправка запроса на получение ресурса с id = {id_resource}"):
        response = requests.get(url=f'{HOST}{UNKNOWN}{id_resource}', timeout=5, ** kwargs)
    return response


def create_user(payload: dict, **kwargs):
    """Функция для отправки запроса POST /api/users/ с телом payload"""
    with allure.step("Отправка запроса на создание пользователя"):
        response = requests.post(url=f'{HOST}{USERS}', data=payload, timeout=5, ** kwargs)
    return response


def update_put_user(id_user: int, payload: dict, **kwargs):
    """Функция для отправки запроса PUT /api/users/ с телом payload"""
    with allure.step(f"Отправка запроса на обновление пользователя с id = {id_user}"):
        response = requests.put(url=f'{HOST}{USERS}{id_user}', data=payload, timeout=5, ** kwargs)
    return response


def update_patch_user(id_user: int, payload: dict, **kwargs):
    """Функция для отправки запроса PATCH /api/users/ с телом payload"""
    with allure.step(f"Отправка запроса на обновление пользователя с id = {id_user}"):
        response = requests.patch(url=f'{HOST}{USERS}/{id_user}', data=payload, timeout=5, ** kwargs)
    return response


def delete_user(id_user: int, **kwargs):
    """Функция для отправки запроса DELETE /api/users/ с id пользователя"""
    with allure.step(f"Отправка запроса на удаление пользователя с id = {id_user}"):
        response = requests.delete(url=f'{HOST}{USERS}/{id_user}', timeout=5, ** kwargs)
    return response


def register_user(payload: dict, **kwargs):
    """Функция для отправки запроса POST /api/register/ с телом payload"""
    with allure.step("Отправка запроса на регистрацию"):
        response = requests.post(url=f'{HOST}{REGISTER}', data=payload, timeout=5, **kwargs)
    return response


def login_user(payload: dict, **kwargs):
    """Функция для отправки запроса POST /api/login/ с телом payload"""
    with allure.step("Отправка запроса на авторизацию"):
        response = requests.post(url=f'{HOST}{LOGIN}', data=payload, timeout=5, **kwargs)
    return response
