from gemd_schema.bounds import (
    real_bounds,
    integer_bounds,
    categorical_bounds,
    composition_bounds,
    molecular_structure_bounds,
)

import jsonschema


def test_real_bounds():
    data = {
        "type": "real_bounds",
        "default_units": "meters",
        "lower_bound": 0.0,
        "upper_bound": 10.0,
    }
    jsonschema.validate(data, real_bounds)


def test_integer_bounds():
    data = {
        "type": "integer_bounds",
        "lower_bound": -128,
        "upper_bound": 128,
    }
    jsonschema.validate(data, integer_bounds)


def test_categorical_bounds():
    data = {
        "type": "categorical_bounds",
        "categories": ["red", "green", "blue"],
    }
    jsonschema.validate(data, categorical_bounds)


def test_composition_bounds():
    data = {
        "type": "composition_bounds",
        "components": [
            "water",
            "ethanol",
            "contaminants",
        ],
    }
    jsonschema.validate(data, composition_bounds)


def test_molecular_structure_bounds():
    data = {
        "type": "molecular_structure_bounds",
    }
    jsonschema.validate(data, molecular_structure_bounds)
