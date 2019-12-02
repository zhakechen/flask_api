from flask_login import UserMixin
from application import db, login_manager

# 用户团队关联表
class UsersTeam(db.Model):
    __tablename__ = 'users_team'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), primary_key=True)

# 用户表
class Users(UserMixin, db.Model):
    # 定义表名
    __tablename__ = 'users'

    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 用户名
    username = db.Column(db.String(128), nullable=False)
    # 手机号
    mobile = db.Column(db.String(32), nullable=False, unique=True)
    # 密码
    password = db.Column(db.String(256), nullable=False)

    # 多对多
    teams = db.relationship('UsersTeam', foreign_keys=[UsersTeam.user_id], backref=db.backref('users', lazy='joined'), lazy='dynamic', cascade='all, delete-orphan') 

    def __repr__(self):
        return self.username

# flask-login获取用户的回调函数，会在login成功后自动执行
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# 团队表
class Team(db.Model):
    # 定义表名
    __tablename__ = 'team'

    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 团队名
    name = db.Column(db.String(512), nullable=False)
    # 项目描述
    info = db.Column(db.String(1024), nullable=True)
    # 创建人
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # 创建时间
    created_time = db.Column(db.DateTime, nullable=False)
    # 最后修改人
    updator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    # 最后修改时间
    updated_time = db.Column(db.DateTime, nullable=True)

    # 多对多
    users = db.relationship('UsersTeam', foreign_keys=[UsersTeam.team_id], backref=db.backref('team', lazy='joined'), lazy='dynamic', cascade='all, delete-orphan') 

    def __repr__(self):
        return self.name


# 项目表
class Project(db.Model):
    # 定义表名
    __tablename__ = 'project'

    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 项目名
    name = db.Column(db.String(512), nullable=False)
    # 项目描述
    info = db.Column(db.String(1024), nullable=True)

    # 模块列表
    modules = db.relationship('Module', backref='project')
    # 接口列表
    interfaces = db.relationship('Interface', backref='project')

    # 创建人
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # Users是relationship另一端的模型
    creator = db.relationship("Users", foreign_keys=[creator_id])
    # 创建时间
    created_time = db.Column(db.DateTime, nullable=False)
    
    # 最后修改人
    updator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    updator = db.relationship("Users", foreign_keys=[updator_id])
    # 最后修改时间
    updated_time = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return self.name


# 模块
class Module(db.Model):
    # 定义表名
    __tablename__ = 'module'

    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 模块名
    name = db.Column(db.String(512), nullable=False)
    # 模块描述
    info = db.Column(db.String(1024), nullable=True)
    # 项目id
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

    # 接口列表
    interfaces = db.relationship('Interface', backref='module')

    # 创建人
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    creator = db.relationship("Users", foreign_keys=[creator_id])
    # 创建时间
    created_time = db.Column(db.DateTime, nullable=False)

    # 最后修改人
    updator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    updator = db.relationship("Users", foreign_keys=[updator_id])
    # 最后修改时间
    updated_time = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return self.name

# 接口
class Interface(db.Model):
    # 定义表名
    __tablename__ = 'interface'

    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 接口名
    name = db.Column(db.String(512), nullable=False)
    # 描述
    info = db.Column(db.String(1024), nullable=True)
    # 地址
    url = db.Column(db.String(1024), nullable=True)
    # 类型
    method_type = db.Column(db.String(16), nullable=False)
    
    # 请求参数体(json表示)
    request_body = db.Column(db.Text, nullable=True)
    # 响应体(json表示)
    response_body = db.Column(db.Text, nullable=True)

    # 项目id
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    # 模块id
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=True)

    # 创建人
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    creator = db.relationship("Users", foreign_keys=[creator_id])
    # 创建时间
    created_time = db.Column(db.DateTime, nullable=False)

    # 最后修改人
    updator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    updator = db.relationship("Users", foreign_keys=[updator_id])
    # 最后修改时间
    updated_time = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return self.name

    # 转换成字典
    def to_dict(self):
        item_dict = {'id': self.id, 'name': self.name, 'info': self.info, 'url': self.url, 'method_type': self.method_type, 'request_body': self.request_body, 'response_body': self.response_body}
        return item_dict

