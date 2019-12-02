from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError
from application.users.models import *

# 注册表单
class RegisterForm(FlaskForm):
    username = StringField('用户名c', validators=[DataRequired(), Length(max=8, message='用户名不能超过128个字')])
    mobile = StringField('手机号', validators=[DataRequired(), Length(max=32, message='手机号不能超过32位')])
    password = PasswordField('密码', validators=[DataRequired(), Length(min=6, max=32, message='密码不能小于6位')])    
    submit = SubmitField('提交')

    # 验证用户名是否存在
    def validate_username(self, field):
        username = field.data
        if Users.query.filter_by(username=username).first():
            raise ValidationError('该用户名已存在')

    # 验证手机号是否存在
    def validate_mobile(self, field):
        mobile = field.data
        if Users.query.filter_by(mobile=mobile).first():
            raise ValidationError('该手机号已存在')

# 登录表单
class LoginForm(FlaskForm):
    username = StringField('用户名/手机号', validators=[DataRequired('用户名不能为空')])
    password = PasswordField('密码', validators=[DataRequired('密码不能为空')])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')

