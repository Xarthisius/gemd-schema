from .attribute import attribute
from .value import (
    real_value,
    integer_value,
    categorical,
    composition,
    molecular_structure,
)

property_and_conditions = {
    "type": "object",
    "properties": {
        "type": {
            "const": "property_and_conditions"
        },
        "property": {
            "allOf": [attribute],
            "properties": {
                "type": {
                    "const": "property"
                },
                "name": True,
                "value": True,
                "origin": True,
                "template": True,
                "file_links": True,
            },
            "required": ["type"],
            "additionalProperties": False
        },
        "conditions": {
            "type": "array",
            "items": {
                "properties": {
                    "type": {
                        "const": "condition"
                    },
                    "name": True,
                    "value": True,
                    "origin": True,
                    "template": True,
                    "file_links": True,
                },
                "required": ["type"],
                "additionalProperties": False
            },
            "minItems": 0
        },
    },
    "required": ["type", "property", "conditions"],
    "additionalProperties": False,
    "definitions": {
        "real_value": real_value,
        "integer_value": integer_value,
        "categorical": categorical,
        "composition": composition,
        "molecular_structure": molecular_structure,
        "attribute": attribute
    },
}
