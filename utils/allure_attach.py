"""Модуль содержит методы для взаимодействия с Allure"""
import allure
from requests import Response


def allure_attach_responce(response: Response):
    """
    Функция для прикрепления данных к тестам
    """
    attach_data = f'Request URL: {response.request.url}\n' \
                  f'Request method: {response.request.method}\n' \
                  f'Request body: {response.request.body}\n' \
                  f'Response status code: {response.status_code}\n' \
                  f'Response text: {response.text}'
    allure.attach(body=attach_data, name="Request Data")
