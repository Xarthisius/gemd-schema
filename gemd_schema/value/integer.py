uniform_integer = {
    "type": "object",
    "properties": {
        "type": {"const": "uniform_integer"},
        "lower_bound": {"type": "integer"},
        "upper_bound": {"type": "integer"},
    },
    "required": ["type", "lower_bound", "upper_bound"],
}

nominal_integer = {
    "type": "object",
    "properties": {
        "type": {"const": "nominal_integer"},
        "nominal": {"type": "integer"},
    },
    "required": ["type", "nominal"],
}

integer_value = {
    "anyOf": [uniform_integer, nominal_integer]
}
