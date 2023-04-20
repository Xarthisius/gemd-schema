# Description: JSON schema for molecular structure

molecular_structure = {
    "type": "object",
    "properties": {
        "type": {"type": "string", "enum": ["smiles", "inchi"]},
        "smiles": {
            "type": "string",
            "pattern": "^[A-Za-z0-9\\-\\+\\(\\)\\[\\]\\@\\:\\/\\=\\#\\$\\%\\&\\'\\*\\,\\.\\;\\_\\s]+$",
        },
        "inchi": {
            "type": "string",
            "pattern": "^[A-Za-z0-9\\-\\+\\(\\)\\[\\]\\@\\:\\/\\=\\#\\$\\%\\&\\'\\*\\,\\.\\;\\_\\s]+$",
        },
    },
    "required": ["type"],
    "oneOf": [{"required": ["smiles"]}, {"required": ["inchi"]}],
}
