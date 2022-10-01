import requests

from configuration import *

from src.baseclasses.response import Response


def test_get_all_characters():
    response = Response(requests.get(url=BASE_URL + CHARACTERS))
    response.assert_status_code(200).validate()


def test_get_single_character():
    response = Response(requests.get(url=BASE_URL + CHARACTERS + "/1"))
    response.assert_status_code(200).validate()


def test_get_multiple_characters():
    response = Response(requests.get(url=BASE_URL + CHARACTERS + "/1,48,135"))
    response.assert_status_code(200).validate()


def test_status_get_wrong_character():
    response = Response(requests.get(url=BASE_URL + CHARACTERS + "/-1"))
    response.assert_status_code(404)


# def test_get_only_human_characters():
#     response = requests.get(url=BASE_URL + CHARACTERS + "/?species=Human")
#     assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

