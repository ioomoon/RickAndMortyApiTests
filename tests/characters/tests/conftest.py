import pytest
import requests
from src.baseclasses.response import Response

from configuration import *


@pytest.fixture()
def get_all_characters():
    response = Response(requests.get(url=BASE_URL + CHARACTERS))
    return response


@pytest.fixture()
def get_character_by_id():
    def _get_characters_by_id(character_id):
        response = Response(requests.get(url=BASE_URL + CHARACTERS + "/" + str(character_id)))
        return response

    return _get_characters_by_id


@pytest.fixture()
def get_characters_by_ids():
    def _get_characters_by_ids(*characters_ids):
        ids_string = ""
        for character_id in characters_ids:
            ids_string += str(character_id) + ","
        response = Response(requests.get(url=BASE_URL + CHARACTERS + "/" + ids_string))
        return response

    return _get_characters_by_ids


@pytest.fixture()
def get_character_by_parameters():
    def _get_characters_by_parameters(parameters):
        response = Response(requests.get(url=BASE_URL + CHARACTERS + "/" + str(parameters)))
        return response

    return _get_characters_by_parameters
