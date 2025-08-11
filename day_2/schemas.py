from marshmallow import Schema, fields

class BookSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True, example="The Lord of the Rings")
    author = fields.String(required=True, example="J.R.R. Tolkien")