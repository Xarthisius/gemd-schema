from .bounds import (
    one_of_bounds,
)
from .identifier import identifier, link
from .value import real_value

attribute_template = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "definitions": {
        "identifier": identifier,
        "one_of_bounds": one_of_bounds,
        "real_value": real_value,
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
        "bounds": {"$ref": "#/definitions/one_of_bounds"},
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

property_template = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "definitions": {
        "identifier": identifier,
        "one_of_bounds": one_of_bounds,
    },
    "oneOf": [
        {
            "allOf": [
                attribute_template,
                {
                    "properties": {
                        "type": {
                            "const": "property_template",
                        },
                    },
                },
            ]
        },
        link,
    ],
}

condition_template = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "definitions": {
        "identifier": identifier,
        "one_of_bounds": one_of_bounds,
    },
    "oneOf": [
        {
            "allOf": [
                attribute_template,
                {
                    "properties": {
                        "type": {
                            "const": "condition_template",
                        },
                    },
                },
            ]
        },
        link,
    ],
}

parameter_template = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "definitions": {
        "identifier": identifier,
        "one_of_bounds": one_of_bounds,
        "real_value": real_value,
    },
    "oneOf": [
        {
            "allOf": [
                attribute_template,
                {
                    "properties": {
                        "type": {
                            "const": "parameter_template",
                        },
                    },
                },
            ],
        },
        link,
    ],
}
