real_bounds = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "description": "A template for a real-valued attribute",
    "type": "object",
    "properties": {
        "type": {
            "const": "real_bounds",
        },
        "default_units": {
            "type": "string",
            "description": "Unit used to express the bounds",
        },
        "lower_bound": {
            "type": "number",
            "description": "the lower bound",
        },
        "upper_bound": {
            "type": "number",
            "description": "the upper bound",
        },
    },
    "required": ["type", "default_units", "lower_bound", "upper_bound"],
}

integer_bounds = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "properties": {
        "type": {
            "const": "integer_bounds",
        },
        "lower_bound": {
            "type": "integer",
            "description": "the inclusive lower bound",
        },
        "upper_bound": {
            "type": "integer",
            "description": "the inclusive upper bound",
        },
    },
    "required": ["type", "lower_bound", "upper_bound"],
}

categorical_bounds = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "properties": {
        "type": {
            "const": "categorical_bounds",
        },
        "categories": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 1,
            "description": "A set of valid categorical values",
        },
    },
    "required": ["type", "categories"],
}

composition_bounds = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "properties": {
        "type": {
            "const": "composition_bounds",
        },
        "components": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 1,
            "description": "A set of valid component names",
        },
    },
    "required": ["type", "components"],
}

molecular_structure_bounds = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "properties": {
        "type": {
            "const": "molecular_structure_bounds",
        },
    },
    "required": ["type"],
}
