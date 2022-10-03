"""
В данном проекте JSON Schema приведена  для примера. Для валидации данных используется Pydantic.
"""

INFO_SCHEMA = {
    "info": {
        "count": {"type": "number"},
        "pages": {"type": "number"},
        "next": {"type": "string"},
        "prev": {"type": "string"},
    },
}