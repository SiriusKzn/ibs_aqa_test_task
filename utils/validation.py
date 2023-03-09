"""Модуль содержит методы для валидации"""
import json
import jsonschema


def validate_json_schema(json_data, schema) -> bool:
    """Функция для валидации json схем"""
    try:
        jsonschema.validate(instance=json_data, schema=schema, )
        return True
    except jsonschema.exceptions.ValidationError:
        return False


def get_json_schema(path):
    """Функция для получения schema из файла по пути path"""
    with open(f'schemas/{path}', 'r', encoding='UTF-8') as file:
        json_schema = json.load(file)
        return json_schema
