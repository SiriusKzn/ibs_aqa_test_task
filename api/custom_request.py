"""Модуль содержит метод отправки кастомных запросов"""
import allure
import requests

from config import HOST
from utils.allure_attach import allure_attach_responce


def send_custom_request(method, endpoint, host=HOST, **kwargs):
    """Функция для отправки кастомного запроса"""
    with allure.step("Отправка API запроса на сервер"):
        responce = requests.request(url=f"{host}{endpoint}", method=method, timeout=5, **kwargs)
        allure_attach_responce(responce)
    return responce
