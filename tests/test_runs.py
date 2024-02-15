import jsonschema
from gemd_schema.run import (
    source,
    process_run,
    ingredient_run,
    measurement_run,
    material_run,
)


def test_source():
    data = {
        "type": "performed_source",
        "performed_by": "joe@abc.com",
        "performed_date": "2015-03-14T15:09:27",
    }
    jsonschema.validate(data, source)


def test_process_run():
    data = {
        "type": "process_run",
        "uids": {
            "cookie_ids": "choc_chip_proc_001_run_006",
            "id": "ea7af3f4-8dbf-41ba-8084-c6f2e31907a5",
        },
        "tags": ["baking::cookies"],
        "name": "Bake Cookies Fo' Real",
        "notes": "Process Run baking some chocolate chip cookies in an oven",
        "spec": {
            "type": "link_by_uid",
            "scope": "id",
            "id": "064148e6-1cce-4d89-bfde-7ecd0aa4632b",
        },
        "parameters": [
            {
                "type": "parameter",
                "name": "Oven Temperature",
                "origin": "measured",
                "template": {
                    "type": "link_by_uid",
                    "scope": "cookie_templates",
                    "id": "oven_temp",
                },
                "tags": ["oven_settings::temperature"],
                "value": {
                    "type": "uniform_real",
                    "lower_bound": 447.5,
                    "upper_bound": 452.5,
                    "units": "kelvin",
                },
            },
            {
                "type": "parameter",
                "name": "Baking Time",
                "origin": "measured",
                "template": {
                    "type": "link_by_uid",
                    "scope": "cookie_templates",
                    "id": "oven_time",
                },
                "tags": ["oven_settings::duration"],
                "value": {"type": "nominal_real", "units": "seconds", "nominal": 614},
            },
        ],
        "ingredients": [
            {
                "type": "link_by_uid",
                "scope": "cookie ingredients",
                "id": "chocolate chip cookie batter #45 in cookie 6",
            },
            {
                "type": "link_by_uid",
                "scope": "secret ingredients",
                "id": "love #724 in cookie 6",
            },
        ],
        "output_material": {
            "type": "link_by_uid",
            "scope": "cookie ids",
            "id": "chocolate_chip_00038",
        },
    }
    jsonschema.validate(data, process_run)


def test_ingredient_run():
    data = {
        "type": "ingredient_run",
        "material": {
            "type": "link_by_uid",
            "scope": "id",
            "id": "18d95397-4887-48f0-bdda-94a9a4c5ef45",
        },
        "process": {"type": "link_by_uid", "scope": "my_scope", "id": "a-cool-process"},
        "uids": {"cookie_ids": "choc_chip_run_4_in_sandwich_7"},
        "notes": "Chocolate chip cookie batch 4 used in making an ice cream sandwich batch 7",
        "absolute_quantity": {
            "type": "uniform_integer",
            "lower_bound": 2,
            "upper_bound": 2,
        },
        "mass_fraction": {"type": "normal_real", "mean": 0.347, "std": 0.002},
        "spec": {
            "type": "link_by_uid",
            "scope": "my_scope",
            "id": "a-cool-ingridient-spec",
        },
    }
    jsonschema.validate(data, ingredient_run)


def test_material_run():
    data = {
        "type": "material_run",
        "uids": {"cookie_ids": "choc_chip_001_run_006"},
        "name": "Chocolate Chip Cookie Run 006",
        "notes": "Material Run for chocolate chip cookies",
        "sample_type": "production",
        "spec": {"type": "link_by_uid", "scope": "cookie_ids", "id": "choc_chip_001"},
        "process": {
            "type": "link_by_uid",
            "scope": "cookie_ids",
            "id": "choc_chip_proc_001_run_006",
        },
        "measurements": [
            {
                "type": "link_by_uid",
                "scope": "cookie_ids",
                "id": "choc_chip_001_hedonic_006",
            }
        ],
    }
    jsonschema.validate(data, material_run)


def test_measurement_run():
    data = {
        "type": "measurement_run",
        "uids": {"cookie_ids": "choc_chip_hedonic_run_006"},
        "name": "Chocolate Chip Hedonic Measurement",
        "notes": "Rate the cookies on a scale from 9.9-10",
        "spec": {
            "type": "link_by_uid",
            "scope": "cookie_ids",
            "id": "choc_chip_hedonic_spec",
        },
        "material": {
            "type": "link_by_uid",
            "scope": "cookie_ids",
            "id": "choc_chip_001_run_006",
        },
        "properties": [
            {
                "type": "property",
                "name": "Chocolate Chip Cookie Hedonic Index",
                "notes": "delish",
                "origin": "measured",
                "template": {
                    "type": "link_by_uid",
                    "scope": "cookie_templates",
                    "id": "hedonic_index_prop",
                },
                "value": {"type": "nominal_real", "nominal": 9.997, "units": ""},
            }
        ],
        "conditions": [
            {
                "type": "condition",
                "name": "Measured Cookie Temperature",
                "notes": "used a thermopen",
                "origin": "measured",
                "template": {
                    "type": "link_by_uid",
                    "scope": "cookie_templates",
                    "id": "cookie_eating_temp",
                },
                "value": {
                    "type": "uniform_real",
                    "lower_bound": 318.15,
                    "upper_bound": 318.25,
                    "units": "kelvin",
                },
            }
        ],
        "parameters": [
            {
                "type": "parameter",
                "name": "Cookie Quantity",
                "notes": "I kept going and lost count.",
                "origin": "measured",
                "template": {
                    "type": "link_by_uid",
                    "scope": "cookie_templates",
                    "id": "cookie_count",
                },
                "value": {
                    "type": "uniform_integer",
                    "lower_bound": 7,
                    "upper_bound": 12,
                },
            }
        ],
    }
    jsonschema.validate(data, measurement_run)
