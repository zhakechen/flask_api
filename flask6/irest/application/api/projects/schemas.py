

# 定义Users model 到marshmallow的映射
# model -> json    json -> model
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from application import db
from application.users.models import Users, Project, Module, Interface


class InterfacetSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Interface
        sqla_session = db.session
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=lambda s: len(s.strip()) > 0, error_messages={
        'required': '接口名必填', 'validator_failed':'项目名不能为空'})
    info = fields.String(required=True, validate=lambda s: len(s.strip()) > 0, error_messages={
        'validator_failed': '接口名不能为空'})
    # laod_only只允许从json序列化成model


class ModelSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Module
        sqla_session = db.session
    #     id 是自动生成的，不需要客户端穿给我们，所以只需要从Model序列化成json
    # dump_only=True不是读取操作
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=lambda s: len(s.strip()) > 0, error_messages={
        'required': '模块名必填', 'validator_failed':'项目名不能为空'})
    info = fields.String(required=True, validate=lambda s: len(s.strip()) > 0, error_messages={
        'validator_failed': '模块名不能为空'})
    Interface = fields.Nested(InterfacetSchema, many=True)
    project = fields.Nested('ProjectSchema')


#
class ProjectSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Project
        sqla_session = db.session
    #     id 是自动生成的，不需要客户端穿给我们，所以只需要从Model序列化成json
    # dump_only=True不是读取操作
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True, validate=lambda s: len(s.strip()) > 0, error_messages={
        'required': '项目名必填', 'validator_failed': '项目名不能为空'})
    mobile = fields.String(required=True, validate=lambda s: len(s.strip()) > 0, error_messages={
        'validator_failed': '用户名不能为空'})
    # laod_only只允许从json序列化成model
    info = fields.String(load_only=True, only=['info'])
    interface = fields.Nested(ModelSchema, many=True, only=['interface.name'])





