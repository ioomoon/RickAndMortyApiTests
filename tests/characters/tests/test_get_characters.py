from src.pydantic_schemas.characters import Character, Characters


def test_get_all_characters(get_all_characters):
    get_all_characters.assert_status_code(200).validate(Characters)


def test_get_single_character(get_character_by_id):
    get_character_by_id(1).assert_status_code(200).validate(Character)


def test_get_multiple_characters(get_characters_by_ids):
    get_characters_by_ids(1, 48, 148).assert_status_code(200).validate(Character)


def test_status_get_character_with_wrong_id(get_character_by_id):
    get_character_by_id(1000).assert_status_code(404)
    get_character_by_id("-1").assert_status_code(404)


def test_get_characters_by_name(get_character_by_parameters):
    get_character_by_parameters("?name=rick").assert_status_code(200).validate(Characters)


def test_get_characters_by_name_and_status(get_character_by_parameters):
    get_character_by_parameters("?name=rick&status=alive").assert_status_code(200).validate(Characters)
