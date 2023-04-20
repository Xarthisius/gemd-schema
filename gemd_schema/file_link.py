file_link = {
    "type": "object",
    "properties": {
        "filename": {"type": "string", "description": "The name of the file"},
        "url": {
            "type": "string",
            "description": "The URL at which the file (and associated metadata) can be accessed",
        },
    },
    "required": ["filename", "url"],
}
