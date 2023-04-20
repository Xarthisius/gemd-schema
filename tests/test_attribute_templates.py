from gemd_schema.attribute_templates import attribute_template
import jsonschema


def test_attribute_template():
    data = {
        "type": "property_template",
        "uids": {"id": "2e1bec7e-bda4-441d-bebb-1215bfa6ee0f"},
        "tags": [
            "hardness::indentation::vickers",
            "Newage MT91 Tester::004",
            "astm_hardness::ASTM E-384",
        ],
        "name": "Vickers Hardness on Machine 4",
        "description": (
            "A Vickers indentation hardness test on the Newage MT91 Tester "
            "with machine id #4. Conforms to ASTM standard E-384."
        ),
        "bounds": {
            "type": "real_bounds",
            "default_units": "HV30/15",
            "lower_bound": 0.0,
            "upper_bound": 10000.0,
        },
    }
    jsonschema.validate(data, attribute_template)

    data = {
        "type": "property_template",
        "uids": {"id": "2e1bec7e-bda4-441d-bebb-1215bfa6ee0f"},
        "tags": [
            "#noindigo::newtonwaswrong",
            "taste::therainbow",
            "things_they_are_after::my_lucky_charms",
            "marketing::commercials::candy::skittles",
            "marketing::characters::cereal::leprechaun",
        ],
        "name": "Rainbow Colors",
        "description": "Colors in the rainbow",
        "bounds": {
            "type": "categorical_bounds",
            "categories": ["red", "orange", "yellow", "green", "blue", "violet"],
        },
    }
    jsonschema.validate(data, attribute_template)
