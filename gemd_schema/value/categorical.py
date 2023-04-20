discrete_categorical = {
    "type": "object",
    "properties": {
        "type": {"const": "discrete_categorical"},
        "probabilities": {
            "type": "object",
            "properties": {},
            "additionalProperties": {"type": "number", "minimum": 0, "maximum": 1},
        },
    },
    "required": ["type", "probabilities"],
    "additionalProperties": False,
}

nominal_categorical = {
    "type": "object",
    "properties": {
        "type": {"const": "nominal_categorical"},
        "category": {
            "type": "string",
            "description": "The category of the value",
        },
    },
    "required": ["type", "category"],
    "additionalProperties": False,
}

categorical = {
    "anyOf": [
        discrete_categorical,
        nominal_categorical,
    ]
}
