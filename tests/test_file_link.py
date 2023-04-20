import jsonschema
from gemd_schema.file_link import file_link


def test_file_link():
    data = {
        "filename": "How-to-make-lucky-charms.pdf",
        "url": "https://example.com/files/file/d8f12919-b201-4186-be95-10525eb4256a/version/2",
    }
    jsonschema.validate(data, file_link)
