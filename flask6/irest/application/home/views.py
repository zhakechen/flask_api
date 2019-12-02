from flask import Blueprint, render_template
from flask_login import login_user, login_required
from werkzeug.security import generate_password_hash

from application.users.models import *
from application import db

# 生成蓝图对象
home = Blueprint('home', __name__)

# 登录后的首页
@home.route('/', methods=['GET'])
@login_required
def index():
    return render_template('home/index.html')    





