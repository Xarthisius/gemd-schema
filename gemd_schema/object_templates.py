from .identifier import identifier
from .bounds import one_of_bounds
from .attribute_templates import (
    condition_template,
    parameter_template,
    property_template,
)

process_template = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "properties": {
        "uids": {
            "$ref": "#/definitions/identifier",
        },
        "type": {
            "type": "string",
            "const": "process_template",
        },
        "tags": {
            "type": "array",
            "items": {"type": "string", "maxLength": 256},
            "maxItems": 100,
        },
        "name": {
            "type": "string",
            "description": "The name of the template",
            "maxLength": 128,
        },
        "description": {
            "type": "string",
            "description": "Some text describing what this template is",
            "maxLength": 32768,
        },
        "allowed_names": {
            "type": "array",
            "description": "The set of names that ingredients are allowed to use in their name field",
            "items": {"type": "string", "maxLength": 128},
            "maxItems": 100,
        },
        "allowed_labels": {
            "type": "array",
            "description": "The set of labels that ingredients are allowed to use in their labels field",
            "items": {"type": "string", "maxLength": 128},
            "maxItems": 100,
        },
        "conditions": {
            "type": "array",
            "description": "Templates for associated conditions and bounds narrowing the allowable range",
            "items": {
                "type": "array",
                "items": [
                    {
                        "$ref": "#/definitions/condition_template",
                    },
                    {
                        "$ref": "#/definitions/one_of_bounds",
                    },
                ],
            },
        },
        "parameters": {
            "type": "array",
            "description": "Templates for associated parameters and bounds narrowing the allowable range",
            "items": {
                "type": "array",
                "items": [
                    {
                        "$ref": "#/definitions/parameter_template",
                    },
                    {
                        "$ref": "#/definitions/one_of_bounds",
                    },
                ],
            },
        },
    },
    "required": ["name", "type"],
    "definitions": {
        "identifier": identifier,
        "one_of_bounds": one_of_bounds,
        "condition_template": condition_template,
        "parameter_template": parameter_template,
    },
}

material_template = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "properties": {
        "uids": {
            "$ref": "#/definitions/identifier",
        },
        "type": {
            "type": "string",
            "const": "material_template",
        },
        "tags": {
            "type": "array",
            "items": {"type": "string", "maxLength": 256},
            "maxItems": 100,
        },
        "name": {
            "type": "string",
            "description": "The name of the template",
            "maxLength": 128,
        },
        "description": {
            "type": "string",
            "description": "Some text describing what this template is",
            "maxLength": 32768,
        },
        "properties": {
            "type": "array",
            "description": "Templates for associated properties and bounds narrowing the allowable range",
            "items": {
                "type": "array",
                "items": [
                    {
                        "$ref": "#/definitions/property_template",
                    },
                    {
                        "$ref": "#/definitions/one_of_bounds",
                    },
                ],
            },
        },
    },
    "required": ["name", "type"],
    "definitions": {
        "identifier": identifier,
        "one_of_bounds": one_of_bounds,
        "property_template": property_template,
    },
}

measurement_template = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "properties": {
        "uids": {
            "$ref": "#/definitions/identifier",
        },
        "type": {
            "type": "string",
            "const": "measurement_template",
        },
        "tags": {
            "type": "array",
            "items": {"type": "string", "maxLength": 256},
            "maxItems": 100,
        },
        "name": {
            "type": "string",
            "description": "The name of the template",
            "maxLength": 128,
        },
        "description": {
            "type": "string",
            "description": "Some text describing what this template is",
            "maxLength": 32768,
        },
        "conditions": {
            "type": "array",
            "description": "Templates for associated conditions and bounds narrowing the allowable range",
            "items": {
                "type": "array",
                "items": [
                    {
                        "$ref": "#/definitions/condition_template",
                    },
                    {
                        "$ref": "#/definitions/one_of_bounds",
                    },
                ],
            },
        },
        "parameters": {
            "type": "array",
            "description": "Templates for associated parameters and bounds narrowing the allowable range",
            "items": {
                "type": "array",
                "items": [
                    {
                        "$ref": "#/definitions/parameter_template",
                    },
                    {
                        "$ref": "#/definitions/one_of_bounds",
                    },
                ],
            },
        },
        "properties": {
            "type": "array",
            "description": "Templates for associated properties and bounds narrowing the allowable range",
            "items": {
                "type": "array",
                "items": [
                    {
                        "$ref": "#/definitions/property_template",
                    },
                    {
                        "$ref": "#/definitions/one_of_bounds",
                    },
                ],
            },
        },
    },
    "required": ["name", "type"],
    "definitions": {
        "identifier": identifier,
        "one_of_bounds": one_of_bounds,
        "condition_template": condition_template,
        "parameter_template": parameter_template,
        "property_template": property_template,
    },
}
