# validation/schemas.py
from pydantic import BaseModel, field_validator
from typing import List, Any
from exceptions.errors import NonNumericDataError

class ArraySchema(BaseModel):
    data: List[Any]

    @field_validator('data')
    @classmethod
    def check_numeric_data(cls, value):
        def validate_item(item):
            if isinstance(item, list):
                for sub_item in item:
                    validate_item(sub_item)
            elif not isinstance(item, (int, float)):
                raise NonNumericDataError(f"'{item}' is not a number.")
        validate_item(value)
        return value
