from .attribute_templates import attribute_template
from .bounds import (
    real_bounds,
    integer_bounds,
    categorical_bounds,
    composition_bounds,
    molecular_structure_bounds,
)
from .identifier import identifier
from .file_link import file_link
from .value import (
    real_value,
    integer_value,
    categorical,
    composition,
    molecular_structure,
)


attribute = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "properties": {
        "type": {
            "type": "string",
            "enum": [
                "property",
                "condition",
                "parameter",
            ],
        },
        "value": {
            "type": "object",
            "oneOf": [
                {"$ref": "#/definitions/real_value"},
                {"$ref": "#/definitions/integer_value"},
                {"$ref": "#/definitions/categorical"},
                {"$ref": "#/definitions/composition"},
                {"$ref": "#/definitions/molecular_structure"},
            ],
        },
        "name": {
            "type": "string",
            "description": "The name of the attribute",
            "maxLength": 128,
        },
        "notes": {
            "type": "string",
            "description": "Notes about the attribute",
            "maxLength": 32768,
        },
        "origin": {
            "type": "string",
            "enum": [
                "measured",
                "predicted",
                "summary",
                "specified",
                "computed",
                "unknown",
            ],
            "default": "unknown",
            "description": "The origin of the attribute",
        },
        "template": {
            "$ref": "#/definitions/attribute_template",
        },
        "file_links": {
            "type": "array",
            "items": {"$ref": "#/definitions/file_link"},
            "description": "A list of file links associated with this attribute",
        },
    },
    "definitions": {
        "real_value": real_value,
        "integer_value": integer_value,
        "categorical": categorical,
        "composition": composition,
        "molecular_structure": molecular_structure,
        "attribute_template": attribute_template,
        "file_link": file_link,
        "identifier": identifier,
        "real_bounds": real_bounds,
        "integer_bounds": integer_bounds,
        "categorical_bounds": categorical_bounds,
        "composition_bounds": composition_bounds,
        "molecular_structure_bounds": molecular_structure_bounds,
    },
}
