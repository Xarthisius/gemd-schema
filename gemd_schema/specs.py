from gemd_schema.value import (
    real_value,
    integer_value,
    categorical,
    composition,
    molecular_structure,
)
from gemd_schema.bounds import one_of_bounds
from gemd_schema.object_templates import process_template, material_template, measurement_template
from gemd_schema.file_link import file_link
from gemd_schema.property_and_conditions import property_and_conditions
from gemd_schema.identifier import identifier, link
from gemd_schema.attribute import condition, parameter
from gemd_schema.attribute_templates import attribute_template, parameter_template, condition_template


_process_spec = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "properties": {
        "uids": {
            "$ref": "#/definitions/identifier",
        },
        "type": {
            "type": "string",
            "const": "process_spec",
        },
        "name": {
            "type": "string",
            "description": "The name of the template",
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
        "template": {"$ref": "#/definitions/process_template"},
        "conditions": {
            "type": "array",
            "description": "Specified conditions for the Process Spec",
            "items": {"$ref": "#/definitions/condition"},
        },
        "parameters": {
            "type": "array",
            "description": "Specified parameters for the Process Spec",
            "items": {"$ref": "#/definitions/parameter"},
        },
        "ingredients": {
            "type": "array",
            "description": "Ingredient specs",
            "items": {"$ref": "#/definitions/link"},
        },
        "output_material": {
            "$ref": "#/definitions/link",
        },
    },
    "required": ["name", "type"],
}

_material_spec = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "properties": {
        "uids": {
            "$ref": "#/definitions/identifier",
        },
        "type": {
            "type": "string",
            "const": "material_spec",
        },
        "name": {
            "type": "string",
            "description": "The name of the Spec",
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
        "template": {"$ref": "#/definitions/material_template"},
        "properties": {
            "type": "array",
            "description": "Expected properties for the Material Spec at the given conditions",
            "items": {"$ref": "#/definitions/property_and_conditions"},
        },
        "process": {
            "oneOf": [{"$ref": "#/definitions/process_spec"}, {"$ref": "#/definitions/link"}],
        },
    },
    "required": ["name", "type", "process"],
}

_ingredient_spec = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "properties": {
        "uids": {
            "$ref": "#/definitions/identifier",
        },
        "type": {
            "type": "string",
            "const": "ingredient_spec",
        },
        "name": {
            "type": "string",
            "description": "The name of the ingredient",
            "maxLength": 128,
        },
        "labels": {
            "type": "array",
            "description": (
                "Additional labels on the ingredient for describing the type "
                "or role of the ingredient"
            ),
            "items": {"type": "string", "maxLength": 256},
        },
        "material": {"oneOf": [{"$ref": "#/definitions/material_spec"}, {"$ref": "#/definitions/link"}]},
        "process": {"oneOf": [{"$ref": "#/definitions/process_spec"}, {"$ref": "#/definitions/link"}]},
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
    },
    "required": ["name", "type", "material", "process"],
}

_measurement_spec = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "properties": {
        "uids": {
            "$ref": "#/definitions/identifier",
        },
        "type": {
            "type": "string",
            "const": "measurement_spec",
        },
        "name": {
            "type": "string",
            "description": "The name of the Spec",
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
        "template": {"$ref": "#/definitions/measurement_template"},
        "parameters": {
            "type": "array",
            "description": "Specified parameters for the Measurement Spec",
            "items": {"$ref": "#/definitions/parameter"},
        },
        "conditions": {
            "type": "array",
            "description": "Specified conditions for the Measurement Spec",
            "items": {"$ref": "#/definitions/condition"},
        },
    },
    "required": ["name", "type"],
}


ingredient_spec = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "oneOf": [_ingredient_spec.copy(), link],
}
ingredient_spec["definitions"] = {
    "identifier": identifier,
    "link": link,
    "one_of_bounds": one_of_bounds,
    "condition": condition,
    "parameter": parameter,
    "process_spec": _process_spec,
    "material_spec": _material_spec,
    "integer_value": integer_value,
    "real_value": real_value,
    "file_link": file_link,
}

process_spec = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "oneOf": [_process_spec.copy(), link],
}
process_spec["definitions"] = {
    "identifier": identifier,
    "link": link,
    "one_of_bounds": one_of_bounds,
    "condition": condition,
    "parameter": parameter,
    "process_template": process_template,
    "ingredient_spec": _ingredient_spec,
    "material_spec": _material_spec,
    "file_link": file_link,
    "real_value": real_value,
    "integer_value": integer_value,
    "categorical": categorical,
    "composition": composition,
    "molecular_structure": molecular_structure,
    "attribute_template": attribute_template,
    "parameter_template": parameter_template,
}

material_spec = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "oneOf": [_material_spec.copy(), link],
}
material_spec["definitions"] = {
    "identifier": identifier,
    "link": link,
    "one_of_bounds": one_of_bounds,
    "condition": condition,
    "parameter": parameter,
    "process_spec": _process_spec,
    "property_and_conditions": property_and_conditions,
    "material_template": material_template,
    "file_link": file_link,
    "real_value": real_value,
    "integer_value": integer_value,
    "categorical": categorical,
    "composition": composition,
    "molecular_structure": molecular_structure,
    "attribute_template": attribute_template,
    "parameter_template": parameter_template,
}

measurement_spec = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "oneOf": [_measurement_spec.copy(), link],
}
measurement_spec["definitions"] = {
    "identifier": identifier,
    "link": link,
    "one_of_bounds": one_of_bounds,
    "condition": condition,
    "parameter": parameter,
    "process_spec": _process_spec,
    "material_spec": _material_spec,
    "measurement_template": measurement_template,
    "real_value": real_value,
    "integer_value": integer_value,
    "categorical": categorical,
    "composition": composition,
    "molecular_structure": molecular_structure,
    "attribute_template": attribute_template,
    "parameter_template": parameter_template,
    "condition_template": condition_template,
    "file_link": file_link,
}
