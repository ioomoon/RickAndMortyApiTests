"""
В данном проекте JSON Schema приведена  для примера. Для валидации данных используется Pydantic.
"""

CHARACTER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "status": {"type": "string", "enum": ["Alive", "Dead", "Unknown"]},
        "species": {"type": "string"},
        "type": {"type": "string"},
        "gender": {"type": "string", "enum": ["Male", "Female", "Genderless", "Unknown"]},
        "origin": {
            "name": {"type": "string"},
            "url": {"type": "string"},
        },
        "image": {"type": "string"},
        "episode": {"type": "array"},
        "url": {"type": "string"},
        "created": {"type": "string"}
    },
    "required": ["id"]
}
