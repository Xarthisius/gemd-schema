from .identifier import identifier
from .bounds import (
    real_bounds,
    integer_bounds,
    categorical_bounds,
    composition_bounds,
    molecular_structure_bounds,
)


attribute_template = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "definitions": {
        "identifier": identifier,
        "real_bounds": real_bounds,
        "integer_bounds": integer_bounds,
        "categorical_bounds": categorical_bounds,
        "composition_bounds": composition_bounds,
        "molecular_structure_bounds": molecular_structure_bounds,
    },
    "type": "object",
    "properties": {
        "type": {
            "type": "string",
            "enum": [
                "property_template",
                "condition_template",
                "parameter_template",
            ],
        },
        "name": {
            "type": "string",
            "description": "The name of the template",
            "maxLength": 128,
        },
        "bounds": {
            "oneOf": [
                {"$ref": "#/definitions/real_bounds"},
                {"$ref": "#/definitions/integer_bounds"},
                {"$ref": "#/definitions/categorical_bounds"},
                {"$ref": "#/definitions/composition_bounds"},
                {"$ref": "#/definitions/molecular_structure_bounds"},
            ],
        },
        "uids": {
            "$ref": "#/definitions/identifier",
        },
        "description": {
            "type": "string",
            "description": "Some text describing what this template is",
            "maxLength": 32768,
        },
        "tags": {
            "type": "array",
            "items": {"type": "string", "maxLength": 256},
            "maxItems": 100,
        },
    },
    "required": ["name", "type", "bounds"],
}
