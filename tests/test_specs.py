import jsonschema
from gemd_schema.property_and_conditions import property_and_conditions
from gemd_schema.object_templates import material_template, measurement_template
from gemd_schema.attribute import parameter, condition
from gemd_schema.specs import (
    process_spec,
    ingredient_spec,
    material_spec,
    measurement_spec,
)


def test_process_spec():
    data = {
        "type": "process_spec",
        "uids": {"id": "064148e6-1cce-4d89-bfde-7ecd0aa4632b"},
        "tags": ["baking::cookies"],
        "name": "Bake Cookies",
        "notes": "Process Spec for baking cookies in an oven",
        "template": {
            "type": "link_by_uid",
            "scope": "cookie_templates",
            "id": "baking_process_01",
        },
        "file_links": [
            {
                "filename": "nestle-tollhouse-recipe.pdf",
                "url": "https://example.com/file/d8f12919-b201-4186-be95-10525eb4256a/version/2",
            }
        ],
        "parameters": [
            {
                "type": "parameter",
                "name": "Oven Temperature",
                "origin": "specified",
                "template": {
                    "type": "link_by_uid",
                    "scope": "cookie_templates",
                    "id": "oven_temp",
                },
                "tags": ["oven_settings::duration"],
                "value": {"type": "nominal_real", "nominal": 450, "units": "kelvin"},
            },
            {
                "type": "parameter",
                "name": "Baking Time",
                "origin": "specified",
                "template": {
                    "type": "link_by_uid",
                    "scope": "cookie_templates",
                    "id": "oven_time",
                },
                "tags": ["oven_settings::duration"],
                "value": {"type": "nominal_real", "units": "seconds", "nominal": 600},
            },
        ],
        "ingredients": [
            {
                "type": "link_by_uid",
                "scope": "cookie ingredients",
                "id": "chocolate chip cookie batter",
            },
            {"type": "link_by_uid", "scope": "secret ingredients", "id": "love"},
        ],
        "output_material": {
            "type": "link_by_uid",
            "scope": "id",
            "id": "18d95397-4887-48f0-bdda-94a9a4c5ef45",
        },
    }
    jsonschema.validate(data, process_spec)


def test_ingredient_spec():
    material = {
        "type": "link_by_uid",
        "scope": "id",
        "id": "18d95397-4887-48f0-bdda-94a9a4c5ef45",
    }
    jsonschema.validate(material, material_spec)

    process = {"type": "link_by_uid", "scope": "my_scope", "id": "a-cool-process"}
    jsonschema.validate(process, process_spec)

    data = {
        "type": "ingredient_spec",
        "material": material,
        "process": process,
        "uids": {"cookie_ids": "choc_chip_spec_001_in_sandwich"},
        "notes": "Chocolate chip cookies used in making an ice cream sandwich",
        "absolute_quantity": {"type": "nominal_integer", "nominal": 2},
        "mass_fraction": {"type": "nominal_real", "nominal": 0.35},
        "name": "cookie",
        "labels": ["faces"],
    }
    jsonschema.validate(data, ingredient_spec)


def test_material_spec():
    template = {
        "type": "link_by_uid",
        "scope": "cookie_templates",
        "id": "choc_chip_001",
    }
    jsonschema.validate(template, material_template)

    pac1 = {
        "type": "property_and_conditions",
        "conditions": [
            {
                "type": "condition",
                "name": "ambient temperature",
                "origin": "unknown",
                "value": {
                    "nominal": 20.0,
                    "type": "nominal_real",
                    "units": "degree_Celsius",
                },
                "template": {
                    "type": "link_by_uid",
                    "scope": "cookie_templates",
                    "id": "amb_temp_01",
                },
            },
            {
                "type": "condition",
                "name": "atmospheric pressure",
                "origin": "unknown",
                "value": {
                    "nominal": 1.0,
                    "type": "nominal_real",
                    "units": "atm",
                },
                "template": {
                    "type": "link_by_uid",
                    "scope": "cookie_templates",
                    "id": "amb_pressure_01",
                },
            },
        ],
        "property": {
            "type": "property",
            "name": "density",
            "origin": "unknown",
            "value": {
                "nominal": 1.2,
                "type": "nominal_real",
                "units": "gram / cubic_centimeter",
            },
            "template": {
                "type": "link_by_uid",
                "scope": "cookie_templates",
                "id": "prop_density_01",
            },
        },
    }
    jsonschema.validate(pac1, property_and_conditions)
    pac2 = {
        "type": "property_and_conditions",
        "conditions": [],
        "property": {
            "name": "Cookie Composition",
            "origin": "specified",
            "type": "property",
            "template": {
                "type": "link_by_uid",
                "scope": "cookie_templates",
                "id": "choc_chip_comp_01",
            },
            "value": {
                "type": "nominal_composition",
                "quantities": {
                    "flour": 355,
                    "baking soda": 6,
                    "baking powder": 9,
                    "salt": 8,
                    "butter": 225,
                    "granulated sugar": 205,
                    "brown sugar": 225,
                    "vanilla extract": 15,
                    "eggs": 50,
                    "chocolate chips": 395,
                    "chopped nuts": 225,
                },
            },
        },
    }
    jsonschema.validate(pac2, property_and_conditions)

    process = {
        "type": "link_by_uid",
        "scope": "id",
        "id": "064148e6-1cce-4d89-bfde-7ecd0aa4632b",
    }
    jsonschema.validate(process, process_spec)

    data = {
        "type": "material_spec",
        "uids": {
            "cookie_ids": "choc_chip_spec_001",
            "id": "18d95397-4887-48f0-bdda-94a9a4c5ef45",
        },
        "name": "Chocolate Chip Cookie Spec",
        "notes": "Material Spec for chocolate chip cookies",
        "template": template,
        "properties": [pac1, pac2],
        "process": process,
    }
    jsonschema.validate(data, material_spec)


def test_measurement_spec():
    measurement_t = {
        "type": "link_by_uid",
        "scope": "cookie_templates",
        "id": "choc_chip_hedonic",
    }
    jsonschema.validate(measurement_t, measurement_template)

    par1 = {
        "type": "parameter",
        "name": "Cookie Quantity",
        "notes": "You'll want to eat at least this many cookies for the hedonic index test",
        "origin": "specified",
        "template": {
            "type": "link_by_uid",
            "scope": "cookie_templates",
            "id": "cookie_count",
        },
        "value": {"type": "nominal_integer", "nominal": 7},
    }
    jsonschema.validate(par1, parameter)

    cond1 = {
                "type": "condition",
                "name": "Cookie Temperature",
                "notes": "Let them cool, or you'll burn your mouth and ruin the test.",
                "origin": "specified",
                "template": {
                    "type": "link_by_uid",
                    "scope": "cookie_templates",
                    "id": "cookie_eating_temp",
                },
                "value": {"type": "nominal_real", "nominal": 320, "units": "kelvin"},
    }
    jsonschema.validate(cond1, condition)

    data = {
        "type": "measurement_spec",
        "uids": {"cookie_ids": "choc_chip_hedonic_spec"},
        "name": "Chocolate Chip Cookie Hedonic Index Measurement Spec",
        "notes": "Measurement Specs for measuring the hedonic index of chocolate chip cookies",
        "template": measurement_t,
        "parameters": [par1],
        "conditions": [cond1],
    }
    jsonschema.validate(data, measurement_spec)
