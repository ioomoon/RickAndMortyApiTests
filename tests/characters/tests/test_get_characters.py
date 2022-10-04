import pytest

from src.pydantic_schemas.characters import Character, Characters
from src.pydantic_schemas.error import Error


def test_get_all_characters(get_all_characters):
    get_all_characters.assert_status_code(200).validate(Characters)


def test_get_single_character(get_character_by_id):
    get_character_by_id(1).assert_status_code(200).validate(Character)


@pytest.mark.parametrize('id1, id2, id3', [
    (1, 48, 148),
    (0, 48, 148),
    (0, 0, 148)
])
def test_get_multiple_characters(id1, id2, id3, get_characters_by_ids):
    get_characters_by_ids(id1, id2, id3).assert_status_code(200).validate(Character)


@pytest.mark.parametrize('wrong_id', [
    -1, 827, 1000
])
def test_get_character_with_wrong_id(wrong_id, get_character_by_id):
    get_character_by_id(wrong_id).assert_status_code(404).validate(Error)


@pytest.mark.parametrize('invalid_id', [
    'abc', '&', ' '
])
def test_get_character_with_invalid_id(invalid_id, get_character_by_id):
    get_character_by_id(invalid_id).assert_status_code(500).validate(Error)


@pytest.mark.parametrize('name_parameter', [
    '?name=rick', '?name=morty'
])
def test_get_characters_by_name(name_parameter, get_character_by_parameters):
    get_character_by_parameters(name_parameter).assert_status_code(200).validate(Characters)


def test_get_characters_by_wrong_name(get_character_by_parameters):
    get_character_by_parameters("?name=alice").assert_status_code(404).validate(Error)


@pytest.mark.parametrize('parameters', [
    '?name=rick&status=alive', '?status=alive&name=rick', '?status=dead&species=human', '?species=human&gender=male',
    '?name=&status=', '?status=alive&name='
])
def test_get_characters_by_name_and_status(parameters, get_character_by_parameters):
    get_character_by_parameters(parameters).assert_status_code(200).validate(Characters)


@pytest.mark.parametrize('invalid_parameters', [
    '?status=_&species=&', '?species=1&gender=2'
])
def test_get_characters_by_invalid_name_and_status(invalid_parameters, get_character_by_parameters):
    get_character_by_parameters(invalid_parameters).assert_status_code(404).validate(Error)
