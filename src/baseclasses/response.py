class Response:
    """
    Класс для валидации данных. Принимает объект респонса и разбирает его в соответствии с
    переданной схемой (модель данных pydantic).
    """

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for element in self.response_json:
                schema.parse_obj(element)
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def __str__(self):
        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Requested URL: {self.response.url} \n" \
            f"Response body: {self.response_json}"
