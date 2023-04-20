nominal_composition = {
    "type": "object",
    "properties": {
        "type": {"const": "nominal_composition"},
        "quantities": {
            "type": "object",
            "properties": {},
            "additionalProperties": {"type": "number", "minimum": 0.0},
        },
    },
    "required": ["type", "quantities"],
    "additionalProperties": False,
}

empirical_formula = {
    "type": "object",
    "properties": {
        "type": {"const": "empirical_formula"},
        "formula": {
            "type": "string",
            "description": "Chemical formula to be parsed as an empirical formula",
        },
    },
    "required": ["type", "formula"],
    "additionalProperties": False,
}

composition = {"anyOf": [nominal_composition, empirical_formula]}
