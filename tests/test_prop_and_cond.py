import jsonschema
import pytest
from gemd_schema.property_and_conditions import property_and_conditions

def test_prop_and_cond():
    data = {
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
            },
            {
                "type": "condition",
                "name": "atmospheric pressure",
                "origin": "unknown",
                "value": {"nominal": 1.0, "type": "nominal_real", "units": "atm"},
            },
        ],
        "property": {
            "type": "property",
            "name": "density",
            "origin": "unknown",
            "value": {
                "nominal": 0.7893,
                "type": "nominal_real",
                "units": "gram / cubic_centimeter",
            },
        },
    }

    jsonschema.Draft7Validator.check_schema(property_and_conditions)
    jsonschema.validate(data, property_and_conditions)

    data["conditions"][0]["type"] = "property"
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(data, property_and_conditions)

    data["conditions"][0]["type"] = "condition"
    data["property"]["type"] = "parameter"
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(data, property_and_conditions)
