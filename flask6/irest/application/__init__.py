from flask import Flask, request, make_response, redirect, abort, render_template
from flask_script import Manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_jwt_extended import JWTManager



# 设置数据库连接字符串
# 不跟踪修改，不设置会有警告
# 创建数据库连接
db = SQLAlchemy()
jwt = JWTManager()

# 初始化LoginManager
login_manager = LoginManager()
# 设为'strong'侦测ip地址和user-agent信息有无异常，有异常就登出
login_manager.session_protection = 'strong'
# 指定登录页面
login_manager.login_view = 'users.login'


#注册蓝图对象
from application.users.views import users
from application.home.views import home
from application.projects.views import projects
from application.api.users.views import api_users
from application.common.error_handler import error
from application.api.projects.views import api_projects


# 工厂方法创建app
def create_app(config=None):
    app = Flask(__name__)
    if config is not None:
        # 加载配置信息
        app.config.from_object(config)
        # 组测蓝图
    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(home, url_prefix='/home')
    app.register_blueprint(projects, url_prefix='/projects')
    app.register_blueprint(api_users, url_prefix='/api/users')
    app.register_blueprint(error, url_prefix='/error')
    app.register_blueprint(api_projects, url_prefix='/api/projects')
    # 跟app发生关系
    login_manager.init_app(app)
    db.init_app(app)

    jwt.init_app(app)
    return app


