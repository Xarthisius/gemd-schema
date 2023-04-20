import jsonschema
from gemd_schema.attribute import attribute


def test_attribute():
    jsonschema.Draft7Validator.check_schema(attribute)
    data = {
        "type": "property",
        "name": "A Real Valued Property",
        "value": {
            "type": "uniform_real",
            "lower_bound": 1.995,
            "upper_bound": 2.005,
            "units": "inch",
        },
        "origin": "measured",
        "template": {
            "name": "A Property Template",
            "type": "property_template",
            "bounds": {
                "type": "real_bounds",
                "lower_bound": 0.0,
                "upper_bound": 10.0,
                "default_units": "meters",
            },
        },
        "file_links": [
            {
                "filename": "How-to-make-lucky-charms.pdf",
                "url": (
                    "http://example.com/files/"
                    "file/d8f12919-b201-4186-be95-10525eb4256a/version/2"
                ),
            }
        ],
    }
    jsonschema.validate(data, attribute)

    data = {
        "type": "condition",
        "name": "A Real Valued Condition",
        "value": {
            "type": "uniform_real",
            "lower_bound": 1.0,
            "upper_bound": 2.0,
            "units": "degC",
        },
        "origin": "measured",
        "template": {
            "type": "condition_template",
            "name": "temperature",
            "bounds": {
                "type": "real_bounds",
                "lower_bound": 0.0,
                "upper_bound": 1.0e6,
                "default_units": "Kelvin",
            },
        },
    }
    jsonschema.validate(data, attribute)

    data = {
        "type": "parameter",
        "name": "A Real Valued Parameter",
        "value": {"type": "nominal_real", "nominal": 1.0, "units": "degC"},
        "origin": "specified",
    }
    jsonschema.validate(data, attribute)
    print(attribute)
