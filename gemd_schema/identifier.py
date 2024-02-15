identifier = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string",
            "description": "string representation of a random Version 4 UUID",
            "minLength": 36,
            "maxLength": 36,
            "format": "uuid",
        },
    },
    "additionalProperties": {
        "type": "string",
        "maxLength": 512,
    },
    "propertyNames": {"not": {"pattern": "::"}},
    "minProperties": 1,
    "maxProperties": 8,
}
