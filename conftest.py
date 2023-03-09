import os

import webdriver_manager.chrome
from webdriver_manager.core.utils import ChromeType

import pytest
import webdriver_manager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import config
from pages.home_page import HomePage


def add_env_properties(capabilities={}):
    """Функция добавляет в отчёт Allure данные об окружении"""
    if not os.path.exists(config.ALLURE_PATH):
        os.mkdir(f'{config.ALLURE_PATH}')
    with open(f'{config.ALLURE_PATH}/environment.properties', 'w') as file:
        if len(capabilities) > 0:
            file.write(f'Host={config.HOST}\n')
            file.write(f'Browser={config.BROWSER}\n')
            file.write(f'Version={capabilities["browserVersion"]}\n')
            file.write(f'Env={config.ENV}')


@pytest.fixture(scope="package")
def driver():
    """Функция инициализирует браузер """
    if config.BROWSER == "Chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif config.BROWSER == "Firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    add_env_properties(driver.capabilities)
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture(scope="package")
def hp(driver):
    """Открытие главной страницы"""
    hp = HomePage(driver, config.HOST)
    hp.open()
    return hp
