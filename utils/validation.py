import json
import os

import jsonschema
import schemas
import requests
from requests import Response


def validate_json_schema(json_data, schema) -> bool:
    try:
        jsonschema.validate(instance=json_data, schema=schema, )
        return True
    except jsonschema.exceptions.ValidationError:
        return False


def get_json_schema(path):
    with open(f'schemas/{path}') as file:
        json_schema = json.load(file)
        return json_schema



