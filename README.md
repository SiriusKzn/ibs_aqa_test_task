# aqa_test_task
Для запуска проекта необходимо установить зависимости 

pip install -r requirements.txt


Запуск тестов выполняется командой 

pytest -s -v --alluredir=allure-result

При смене директории Allure необходимо изменить параметр ALLURE_PATH в файле config.py



В проекте предусмотрены маркеры тестов

WEB - запуск UI тестов

API - запуск API тестов
