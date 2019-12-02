from flask import Blueprint, render_template, flash, redirect, url_for, jsonify, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_
from application.common.status_code import *
from flask_jwt_extended import create_access_token, jwt_required

from application.users.forms import *
from application.users.models import *

from application.api.users.schemas import *


# 生成蓝图对象
api_users = Blueprint('api_users', __name__)

# 取用户列表
@api_users.route('/', methods=['GET'])
@jwt_required
def insex():
    get_users = Users.query.all()
    users_schema = UsersSchema(many=True)
    users = users_schema.dump(get_users)

    return jsonify({'code': 200, 'msg': '成功', 'data': users})

# 去单个用户
@api_users.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    one_user = Users.query.get(int(user_id))
    user_schema = UsersSchema()
    users = user_schema.dump(one_user)

    return jsonify({'code': SUCCESS, 'msg': '成功', 'data': users})


# 新增用户
@api_users.route('/', methods=['POST'])
def add_user():
    json_data = request.get_json()
    json_data['password'] = generate_password_hash(
        json_data['password'])
    user_schema = UsersSchema()
    user = user_schema.load(json_data)
    db.session.add(user)
    db.session.commit()

    return jsonify({'code': SUCCESS, 'msg': '成功', 'data': {'user_id': user.id}})

# 修改用户
@api_users.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    json_data = request.get_json()
    user = Users.query.get(int(user_id))
    if 'password' in json_data:
        user.password = generate_password_hash(
            json_data['password'])
        if 'username' in json_data:
            user.username = json_data['username']
        if 'mobile' in json_data:
            user.mobile = json_data['mobile']
        db.session.add(user)
        db.session.commit()

        user_schema = UsersSchema()
        user_json = user_schema.dump(user)
        return jsonify({'code': 200, 'msg': '成功', 'data': {'user_json': user_json}})


# 删除
@api_users.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Users.query.get(int(user_id))
    db.session.delete(user)
    db.session.commit()
    return jsonify({'code': 200, 'msg': '成功', 'data': {'user_id': user_id}})

# 部分更新
@api_users.route('/<int:user_id>', methods=['PATCH'])
def updata_user_part(user_id):
    json_data = request.get_json()
    user = Users.query.get(int(user_id))
    users_schema = UsersSchema()
    get_user = users_schema.load(json_data, partial=('username',))
    user.mobile = get_user.mobile

    db.session.add(user)
    db.session.commit()

    user_schema = UsersSchema()
    user_json = user_schema.dump(user)
    return jsonify({'code': 200, 'msg': '成功', 'data': {'user_json': user_json}})

# 登录
@api_users.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()
    user_schema = UsersSchema()
    user_schema.load(json_data, partial=('mobile',))
    username = json_data['username']
    user = Users.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'code': ERROR_USER_PASSWORD_ERROR[0], 'message': ERROR_USER_PASSWORD_ERROR[0]})
    if check_password_hash(user.password, json_data['password']):
    # 验证通过jwt令牌
        jwt_token = create_access_token(identity=username)
        return jsonify({'code': SUCCESS, 'message': '成功', 'token': jwt_token})
    return jsonify({'code': ERROR_USER_PASSWORD_ERROR[0], 'message': ERROR_USER_PASSWORD_ERROR[0]})






