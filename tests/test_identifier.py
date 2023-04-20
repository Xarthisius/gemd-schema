import jsonschema
import pytest

from gemd_schema.identifier import identifier


def test_identifier():
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "uids": {
                "$ref": "#/definitions/identifier_schema",
            },
        },
        "definitions": {
            "identifier_schema": identifier,
        },
    }

    data = {"uids": {"id": "f36099b9-2ca1-4ff7-afd2-dd226dc79e66"}}
    jsonschema.validate(data, schema)

    data = {"uids": {"id": "f36099b9-2ca1-4ff7-afd2-dd226dc79e66", "NIST-SRM": "141e"}}
    jsonschema.validate(data, schema)

    with pytest.raises(jsonschema.ValidationError):
        data = {"uids": {"NIST-SRM": "141e"}}
        jsonschema.validate(data, schema)
