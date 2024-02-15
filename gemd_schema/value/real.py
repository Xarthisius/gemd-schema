normal_real_value = {
    "type": "object",
    "properties": {
        "type": {"const": "normal_real"},
        "mean": {
            "type": "number",
            "description": "Mean of the normal distribution",
        },
        "std": {
            "type": "number",
            "description": "Standard deviation of the normal distribution",
            "minimum": 0.0,
        },
        "units": {
            "type": "string",
            "description": "A string describing the units",
        },
    },
    "required": ["type", "mean", "std"],
}

uniform_real_value = {
    "type": "object",
    "properties": {
        "type": {"const": "uniform_real"},
        "lower_bound": {
            "type": "number",
            "description": "Lower bound of the uniform distribution",
        },
        "upper_bound": {
            "type": "number",
            "description": "Upper bound of the uniform distribution",
        },
        "units": {
            "type": "string",
            "description": "A string describing the units",
        },
    },
    "required": ["type", "lower_bound", "upper_bound", "units"],
}

nominal_real_value = {
    "type": "object",
    "properties": {
        "type": {"const": "nominal_real"},
        "nominal": {
            "type": "number",
            "description": "Nominal value - not assumed to be exact",
        },
        "units": {
            "type": "string",
            "description": "A string describing the units",
        },
    },
    "required": ["type", "nominal"],
}

real_value = {
    "oneOf": [
        normal_real_value,
        uniform_real_value,
        nominal_real_value,
    ],
}
