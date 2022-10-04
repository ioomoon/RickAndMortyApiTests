from enum import Enum

from pydantic import BaseModel


class Error(BaseModel):
    error: str


class ErrorMessage(str, Enum):
    not_found = "Character not found"
    id_not_recognized = "Hey! you must provide an id"
    bad_array = "Bad... bad array :/"
    nothing_here = "There is nothing here"
