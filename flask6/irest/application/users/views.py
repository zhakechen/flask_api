from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_

from application.users.forms import *
from application.users.models import *
from application import db

# 生成蓝图对象
users = Blueprint('users', __name__)

# 注册
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # 验证表单
    if form.validate_on_submit():      # validate_on_submit表单提交时才执行
        users = Users()
        users.username = form.username.data
        password = form.password.data
        # 对密码hash
        password_hash = generate_password_hash(password)
        users.password = password_hash
        users.mobile = form.mobile.data
        db.session.add(users)
        db.session.commit()
        # 自动登录
        login_user(users, remember=dyse)     # login_user自动登录，remember=false当时登录有效
        flash('恭喜你，登录成功')
        # 跳转到首页
        return redirect(url_for('projects.index'))

    return render_template('users/register.html', form=form)


# 登录
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 查询用户是否存在
        username = form.username.data
        # 或者用户名登录，或者用户电话登录
        user = Users.query.filter(or_(Users.username == username, Users.mobile == username)).first()
        if user is None:
            flash('用户名或密码错误')
            return render_template('users/login.html', form=form)        

        password = form.password.data
        password_hash = user.password
        remember_me = form.remember_me.data
        if check_password_hash(password_hash, password):
            login_user(user, remember=remember_me)
            flash('恭喜你，登录成功')
            # 跳转到首页
            return redirect(url_for('projects.index'))    # 进入项目文件下的index页面
        else:
            flash('用户名或密码错误')

    return render_template('users/login.html', form=form)

# 登出
@users.route('/logout')
def logout():
    logout_user()
    flash('登出成功')
    # 跳转到首页
    return redirect(url_for('home.index'))



