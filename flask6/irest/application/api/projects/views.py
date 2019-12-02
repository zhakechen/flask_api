from flask import Blueprint, render_template, flash, redirect, url_for, jsonify, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_
from application.common.status_code import *

from application.users.forms import *
from application.users.models import *
from application.api.projects.schemas import *

from application.api.users.schemas import *


# 生成蓝图对象
api_projects = Blueprint('api_projects', __name__)


@api_projects.route('/', methods=['GET'])
def index():
    get_projects = Project.query.all()
    project_schema = ProjectSchema(many=True,)
    json_data = project_schema.dump(get_projects)
    return jsonify({'code': SUCCESS, 'message': '成功', 'data': json_data})


