

# 定义Users model 到marshmallow的映射
# model -> json    json -> model
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from application import db
from application.users.models import Users


class UsersSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Users
        sqla_session = db.session
    #     id 是自动生成的，不需要客户端穿给我们，所以只需要从Model序列化成json
    # dump_only=True不是读取操作
    id = fields.Integer(dump_only=True)
    username = fields.String(attribute='username', required=True, validate=lambda s: len(s.strip()) > 0, error_messages={'required': '用户名必填', 'validator_failed':'用户名不能为空'})
    mobile = fields.String(required=True, validate=lambda s: len(s.strip()) > 0, error_messages={'required': '电话必填', 'validator_failed': '用户名不能为空'})
    # laod_only只允许从json序列化成model
    password = fields.String(load_only=True)




