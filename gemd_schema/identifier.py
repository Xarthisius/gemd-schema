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

link = {
    "type": "object",
    "properties": {
        "type": {"type": "string", "const": "link_by_uid"},
        "scope": {"type": "string"},
        "id": {"type": "string"},
    },
    "required": ["type", "scope", "id"],
}
