from jsonschema import validate

from src.enums.global_enums import GlobalErrorMessages
from src.json_schema.character import CHARACTER_SCHEMA
from src.json_schema.info import INFO_SCHEMA



class Response:
    """
    Класс для валидации данных. Принимает объект респонса и разбирает его в соответствии с
    переданной схемой (модель данных pydantic).
    """

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self):
        for item in self.response_json:
            if isinstance(item, list):
                for element in item:
                    validate(element, CHARACTER_SCHEMA)
            else:
                validate(item, INFO_SCHEMA)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self
