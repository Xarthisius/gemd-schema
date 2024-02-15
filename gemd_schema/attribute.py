from .attribute_templates import (
    attribute_template,
    parameter_template,
    condition_template,
    property_template,
)
from .bounds import one_of_bounds
from .identifier import identifier, link
from .file_link import file_link
from .value import (
    real_value,
    integer_value,
    categorical,
    composition,
    molecular_structure,
)

definitions = {
    "real_value": real_value,
    "integer_value": integer_value,
    "categorical": categorical,
    "composition": composition,
    "molecular_structure": molecular_structure,
    "attribute_template": attribute_template,
    "parameter_template": parameter_template,
    "condition_template": condition_template,
    "property_template": property_template,
    "file_link": file_link,
    "identifier": identifier,
    "one_of_bounds": one_of_bounds,
    "link": link,
}

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
            "oneOf": [
                {"$ref": "#/definitions/attribute_template"},
                {"$ref": "#/definitions/link"},
            ],
        },
        "file_links": {
            "type": "array",
            "items": {"$ref": "#/definitions/file_link"},
            "description": "A list of file links associated with this attribute",
        },
    },
    "definitions": definitions,
}

parameter = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "definitions": definitions,
    "allOf": [
        attribute,
        {
            "properties": {
                "type": {
                    "const": "parameter",
                },
                "template": {"$ref": "#/definitions/parameter_template"},
            },
        },
    ],
}

condition = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "definitions": definitions,
    "allOf": [
        attribute,
        {
            "properties": {
                "type": {
                    "const": "condition",
                },
                "template": {"$ref": "#/definitions/condition_template"},
            },
        },
    ],
}

property_ = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "definitions": definitions,
    "allOf": [
        attribute,
        {
            "properties": {
                "type": {
                    "const": "property",
                },
                "template": {"$ref": "#/definitions/property_template"},
            },
        },
    ],
}
