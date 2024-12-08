from marshmallow import Schema, fields

class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    status = fields.Str()
