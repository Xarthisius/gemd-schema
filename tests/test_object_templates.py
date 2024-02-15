# We are going to test the process_template object template
import jsonschema
from gemd_schema.attribute_templates import parameter_template
from gemd_schema.bounds import real_bounds, one_of_bounds
from gemd_schema.object_templates import process_template


def test_process_template():
    parameter1 = {
        "name": "Oven Temperature",
        "type": "parameter_template",
        "uids": {
            "cookie_templates": "oven_temp",
        },
        "tags": ["oven_settings::temperature"],
        "description": "A template for valid temperature ranges for baking cookies. Below 328K you're not even pasteurizing the dough.",
        "bounds": {
            "default_units": "kelvin",
            "type": "real_bounds",
            "lower_bound": 328,
            "upper_bound": 750,
        },
    }
    jsonschema.validate(parameter1, parameter_template)
    bounds1 = {
        "type": "real_bounds",
        "default_units": "kelvin",
        "lower_bound": 400,
        "upper_bound": 500,
    }
    jsonschema.validate(bounds1, real_bounds)
    jsonschema.validate(bounds1, one_of_bounds)

    parameter2 = {
        "name": "Baking Time",
        "type": "parameter_template",
        "uids": {
            "cookie_templates": "oven_time",
        },
        "tags": ["oven_settings::duration"],
        "description": "A template for valid duration ranges for baking cookies.",
        "bounds": {
            "default_units": "seconds",
            "type": "real_bounds",
            "lower_bound": 0,
            "upper_bound": 86400,
        },
    }
    jsonschema.validate(parameter2, parameter_template)

    data = {
        "type": "process_template",
        "uids": {
            "cookie_templates": "baking_process_01",
            "id": "064148e6-1cce-4d89-bfde-7ecd0aa4632b",
        },
        "tags": ["baking::cookies"],
        "name": "Bake Cookies",
        "description": "Template for baking cookies in an oven",
        "parameters": [
            [parameter1, bounds1],
            [
                parameter2,
                {
                    "type": "real_bounds",
                    "default_units": "seconds",
                    "lower_bound": 300,
                    "upper_bound": 7200,
                },
            ],
        ],
    }

    jsonschema.validate(data, process_template)
