# from gemd_schema.object_templates import process_template, material_template, measurement_template
from gemd_schema.value import (
    real_value,
    integer_value,
    categorical,
    composition,
    molecular_structure,
)
from gemd_schema.file_link import file_link
from gemd_schema.specs import (
    process_spec,
    ingredient_spec,
    material_spec,
    measurement_spec,
)
from gemd_schema.identifier import identifier, link
from gemd_schema.attribute import condition, parameter, property_
from gemd_schema.attribute_templates import (
    attribute_template,
    parameter_template,
    condition_template,
    property_template,
)

source = {
    "type": "object",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "properties": {
        "type": {"type": "string", "const": "performed_source"},
        "performed_by": {
            "type": "string",
            "description": "The person who performed the measurement",
        },
        "performed_date": {
            "type": "string",
            "format": "date",
            "description": (
                "The date the measurement was performed; "
                "ISO-8601 date-formatted string (YYYY-MM-DD or YYYY-MM-DDTHH:mm:SS)"
            ),
        },
    },
    "required": ["type"],
    "additionalProperties": False,
}

_process_run = {
    "type": "object",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "properties": {
        "uids": {
            "$ref": "#/definitions/identifier",
        },
        "type": {
            "type": "string",
            "const": "process_run",
        },
        "name": {
            "type": "string",
            "description": "The name of the Process Run",
            "maxLength": 128,
        },
        "notes": {
            "type": "string",
            "description": "Some free-form notes about the Run",
        },
        "tags": {
            "type": "array",
            "items": {"type": "string", "maxLength": 256},
            "maxItems": 100,
        },
        "file_links": {
            "type": "array",
            "description": "Links to associated files, with resource paths into the files API",
            "items": {"$ref": "#/definitions/file_link"},
        },
        "source": {"$ref": "#/definitions/source"},
        "spec": {"$ref": "#/definitions/process_spec"},
        "parameters": {
            "type": "array",
            "description": "Specified parameters for the Process Spec",
            "items": {"$ref": "#/definitions/parameter"},
        },
        "conditions": {
            "type": "array",
            "description": "Specified conditions for the Process Spec",
            "items": {"$ref": "#/definitions/condition"},
        },
        "ingredients": {
            "type": "array",
            "description": "Ingredient specs",
            "items": {
                "anyOf": [
                    {"$ref": "#/definitions/link"},
                    {"$ref": "#/definitions/ingredient_run"},
                ]
            },
        },
        "output_material": {
            "oneOf": [
                {"$ref": "#/definitions/material_run"},
                {"$ref": "#/definitions/link"},
            ],
        },
    },
    "required": ["name", "type", "spec"],
}

_ingredient_run = {
    "type": "object",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "properties": {
        "uids": {
            "$ref": "#/definitions/identifier",
        },
        "type": {
            "type": "string",
            "const": "ingredient_run",
        },
        "name": {
            "type": "string",
            "description": "The name of the Ingredient Run (inherited from spec)",
            "$ref": "#/spec/name",
            "maxLength": 128,
        },
        "labels": {
            "type": "array",
            "description": (
                "Additional labels on the ingredient for describing the type or role of the "
                "ingredient (inherited from spec)"
            ),
            "$ref": "#/spec/labels",
        },
        "material": {
            "oneOf": [
                {"$ref": "#/definitions/material_run"},
                {"$ref": "#/definitions/link"},
            ]
        },
        "process": {
            "oneOf": [
                {"$ref": "#/definitions/process_run"},
                {"$ref": "#/definitions/link"},
            ]
        },
        "notes": {
            "type": "string",
            "description": "Some free-form notes about the Spec",
        },
        "tags": {
            "type": "array",
            "items": {"type": "string", "maxLength": 256},
            "maxItems": 100,
        },
        "file_links": {
            "type": "array",
            "description": "Links to associated files, with resource paths into the files API",
            "items": {"$ref": "#/definitions/file_link"},
        },
        "mass_fraction": {
            "description": "The mass fraction of the ingredient in the process",
            "$ref": "#/definitions/real_value",
        },
        "volume_fraction": {
            "description": "The volume fraction of the ingredient in the process",
            "$ref": "#/definitions/real_value",
        },
        "number_fraction": {
            "description": "The number fraction (i.e., mole fraction) of the ingredient in the process",
            "$ref": "#/definitions/real_value",
        },
        "absolute_quantity": {
            "description": "The absolute quantity of the ingredient in the process",
            "$ref": "#/definitions/integer_value",
        },
        "spec": {"$ref": "#/definitions/ingredient_spec"},
    },
    "required": ["type", "material", "process", "spec"],
}

_material_run = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "properties": {
        "uids": {
            "$ref": "#/definitions/identifier",
        },
        "type": {
            "type": "string",
            "const": "material_run",
        },
        "name": {
            "type": "string",
            "description": "The name of the Run",
            "maxLength": 128,
        },
        "notes": {
            "type": "string",
            "description": "Some free-form notes about the Spec",
        },
        "tags": {
            "type": "array",
            "items": {"type": "string", "maxLength": 256},
            "maxItems": 100,
        },
        "file_links": {
            "type": "array",
            "description": "Links to associated files, with resource paths into the files API",
            "items": {"$ref": "#/definitions/file_link"},
        },
        "spec": {"$ref": "#/definitions/material_spec"},
        "process": {
            "oneOf": [
                {"$ref": "#/definitions/process_run"},
                {"$ref": "#/definitions/link"},
            ]
        },
        "measurements": {
            "type": "array",
            "description": "characterizations of this Material Run",
            "items": {
                "oneOf": [
                    {"$ref": "#/definitions/measurement_run"},
                    {"$ref": "#/definitions/link"},
                ]
            },
        },
        "sample_type": {
            "type": "string",
            "description": "Context of how this material was made to be",
            "enum": ["experimental", "production", "virtual", "unknown"],
            "default": "unknown",
        },
    },
    "required": ["name", "type", "process", "spec"],
}

_measurement_run = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "uids": {
            "$ref": "#/definitions/identifier",
        },
        "type": {
            "type": "string",
            "const": "measurement_run",
        },
        "name": {
            "type": "string",
            "description": "The name of the Run",
            "maxLength": 128,
        },
        "notes": {
            "type": "string",
            "description": "Some free-form notes about the Spec",
        },
        "tags": {
            "type": "array",
            "items": {"type": "string", "maxLength": 256},
            "maxItems": 100,
        },
        "file_links": {
            "type": "array",
            "description": "Links to associated files, with resource paths into the files API",
            "items": {"$ref": "#/definitions/file_link"},
        },
        "source": {"$ref": "#/definitions/source"},
        "spec": {"$ref": "#/definitions/measurement_spec"},
        "material": {
            "oneOf": [
                {"$ref": "#/definitions/material_run"},
                {"$ref": "#/definitions/link"},
            ]
        },
        "parameters": {
            "type": "array",
            "description": "Specified parameters for the Measurement Run",
            "items": {"$ref": "#/definitions/parameter"},
        },
        "conditions": {
            "type": "array",
            "description": "Specified conditions for the Measurement Run",
            "items": {"$ref": "#/definitions/condition"},
        },
        "properties": {
            "type": "array",
            "description": "Specified properties for the Measurement Run",
            "items": {"$ref": "#/definitions/property"},
        },
    },
    "required": ["name", "type", "spec", "material"],
}

definitions = {
    "source": source,
    "file_link": file_link,
    "identifier": identifier,
    "process_spec": process_spec,
    "ingredient_spec": ingredient_spec,
    "material_spec": material_spec,
    "measurement_spec": measurement_spec,
    "parameter": parameter,
    "condition": condition,
    "property": property_,
    "link": link,
    "ingredient_run": _ingredient_run,
    "material_run": _material_run,
    "process_run": _process_run,
    "measurement_run": _measurement_run,
    "real_value": real_value,
    "integer_value": integer_value,
    "categorical": categorical,
    "composition": composition,
    "molecular_structure": molecular_structure,
    "attribute_template": attribute_template,
    "parameter_template": parameter_template,
    "condition_template": condition_template,
    "property_template": property_template,
}

process_run = {
    "type": "object",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "oneOf": [
        _process_run,
        {"$ref": "#/definitions/link"},
    ],
    "definitions": definitions,
}

ingredient_run = {
    "type": "object",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "oneOf": [
        _ingredient_run,
        {"$ref": "#/definitions/link"},
    ],
    "definitions": definitions,
}

material_run = {
    "type": "object",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "oneOf": [
        _material_run,
        {"$ref": "#/definitions/link"},
    ],
    "definitions": definitions,
}

measurement_run = {
    "type": "object",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "oneOf": [
        _measurement_run,
#        {"$ref": "#/definitions/link"},
    ],
    "definitions": definitions,
}
