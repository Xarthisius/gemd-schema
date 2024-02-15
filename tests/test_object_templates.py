# We are going to test the process_template object template
import jsonschema
from gemd_schema.attribute_templates import (
    parameter_template,
    property_template,
    condition_template,
)
from gemd_schema.bounds import real_bounds, one_of_bounds
from gemd_schema.object_templates import (
    process_template,
    material_template,
    measurement_template,
)


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


def test_material_template():
    data = {
        "type": "material_template",
        "uids": {
            "cookie_templates": "choc_chip",
            "id": "2e1bec7e-bda4-441d-bebb-1215bfa6ee0f",
        },
        "tags": [],
        "name": "Chocolate Chip Cookie Template",
        "description": "Template for chocolate chip cookie materials",
        "properties": [
            [
                {
                    "uids": {"cookie_templates": "choc_chip_comp_01"},
                    "tags": ["ingredients::cookies::nutsallowed"],
                    "name": "Chocolate Chip Cookie Composition",
                    "type": "property_template",
                    "description": "Specifying the composition of the linked cookie",
                    "bounds": {
                        "type": "categorical_bounds",
                        "categories": [
                            "flour",
                            "baking soda",
                            "baking powder",
                            "salt",
                            "butter",
                            "granulated sugar",
                            "brown sugar",
                            "vanilla extract",
                            "eggs",
                            "chocolate chips",
                            "chopped nuts",
                        ],
                    },
                },
                {
                    "type": "categorical_bounds",
                    "categories": [
                        "flour",
                        "baking soda",
                        "baking powder",
                        "salt",
                        "butter",
                        "granulated sugar",
                        "brown sugar",
                        "vanilla extract",
                        "eggs",
                        "chocolate chips",
                        "chopped nuts",
                    ],
                },
            ]
        ],
    }
    jsonschema.validate(data, material_template)


def test_measurement_template():
    property1_template = {
        "uids": {"cookie_templates": "hedonic_index_prop"},
        "tags": [],
        "type": "property_template",
        "name": "Chocolate Chip Cookie Hedonic Index",
        "description": "The allowable range for the hedonic index of chocolate chip cookies.",
        "bounds": {
            "type": "real_bounds",
            "lower_bound": 9.99,
            "upper_bound": 10,
            "default_units": "",
        },
    }
    jsonschema.validate(property1_template, property_template)

    property1_bounds = {
        "type": "real_bounds",
        "lower_bound": 9.99,
        "upper_bound": 10,
        "default_units": "",
    }
    jsonschema.validate(property1_bounds, one_of_bounds)

    condition1_template = {
        "name": "Cookie Temperature",
        "uids": {"cookie_templates": "cookie_eating_temp"},
        "tags": [],
        "type": "condition_template",
        "description": "A template for valid temperature ranges for eating cookies.",
        "bounds": {
            "default_units": "kelvin",
            "type": "real_bounds",
            "lower_bound": 250,
            "upper_bound": 380,
        },
    }
    jsonschema.validate(condition1_template, condition_template)

    condition1_bounds = {
        "default_units": "kelvin",
        "type": "real_bounds",
        "lower_bound": 250,
        "upper_bound": 380,
    }

    parameter1_template = {
        "name": "Number of Cookies",
        "uids": {"cookie_templates": "cookie_count"},
        "tags": ["chocula"],
        "type": "parameter_template",
        "description": "A template for the number of cookies to eat for a hedonic index test.",
        "bounds": {
            "type": "integer_bounds",
            "lower_bound": 1,
            "upper_bound": 1000,
        },
    }
    jsonschema.validate(parameter1_template, parameter_template)

    data = {
        "type": "measurement_template",
        "uids": {
            "cookie_templates": "choc_chip_hedonic",
            "id": "664e5b79-4c16-46db-aa9e-ff70d79d2f79",
        },
        "tags": [],
        "name": "Chocolate Chip Cookie Hedonic Index Measurement Template",
        "description": "Template for chocolate chip cookie materials",
        "properties": [[property1_template, property1_bounds]],
        "conditions": [[condition1_template, condition1_bounds]],
        "parameters": [
            [
                parameter1_template,
                {"type": "integer_bounds", "lower_bound": 1, "upper_bound": 1000},
            ]
        ],
    }
    jsonschema.validate(data, measurement_template)
