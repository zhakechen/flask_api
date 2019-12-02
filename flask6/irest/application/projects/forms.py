from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

# 项目表单
class ProjectForm(FlaskForm):
    project_name = StringField('项目名称', validators=[DataRequired(), Length(max=256, message='项目名称不能超过256个字')])
    project_info = StringField('项目描述', validators=[Length(max=512, message='项目描述不能超过512个字')])
    submit = SubmitField('提交')

# 模块表单
class ModuleForm(FlaskForm):
    module_name = StringField('模块名称', validators=[DataRequired(), Length(max=256, message='模块名称不能超过256个字')])
    module_info = StringField('模块描述', validators=[Length(max=512, message='模块描述不能超过512个字')])
    submit = SubmitField('提交')

# 接口表单
class InterfaceForm(FlaskForm):
    name = StringField('接口名称', validators=[DataRequired(), Length(max=256, message='接口名称不能超过256个字')])
    url = StringField('接口地址', validators=[Length(max=512, message='接口地址不能超过512位')])
    info = StringField('接口描述', validators=[Length(max=512, message='接口描述不能超过512个字')])
    method_type = SelectField('请求类型') # coerce=int option value转成整型

    submit = SubmitField('提交')

    def __init__(self, *args, **kwargs):
        super(InterfaceForm, self).__init__(*args, **kwargs)
        result_list = [ ('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT'), ('DELETE', 'DELETE'), ('OPTIONS', 'OPTIONS'), ('PATCH', 'PATCH'), ('HEAD', 'HEAD') ]
        self.method_type.choices = result_list

