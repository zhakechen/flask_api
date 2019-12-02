# 测试注册方法
from flask import get_flashed_messages
from werkzeug.security import check_password_hash
from flask_login import current_user
from application.users.models import Users, db as database



def test_users_register(client):
    response = client.get('/users/register')
    assert response.status_code == 200
    assert '欢迎注册' in bytes.decode(response.data)

    # post方法注册
    data = {'username': '王伟', 'password': '123321', 'mobile': '123456'}
    response = client.post('/users/register', data=data)
    # 判断是否跳转302 代表跳转。
    assert response.status_code == 200
    assert len(get_flashed_messages()) == 1
    assert '登录成功' in get_flashed_messages()[0]

    assert '我的项目' in bytes.decode(response.data)

    #
    user = Users.query.filter_by(username='扎克').first()
    assert user.password != '123456'
    assert check_password_hash(user.password, '123456')

    #
    assert current_user.username == '召开'


# 测试登录失败情况
def test_users_login(client):
    response = client.get('/users/login')
    assert response.status_code == 200

    data = {'username': '    ', 'password': '123456'}
    response = client.post('/users/login', data=data)
    html = bytes.decode(response.data)
    assert '用户名不能为空' in html

    data = {'username': '  ww  ', 'password': '123456'}
    response = client.post('/users/login', data=data)
    assert response.status_code == 302
    assert current_user.username == 'ww'

    data = {'username': '  ww  ', 'password': '1234567'}
    response = client.post('/users/login', data=data)
    assert len(get_flashed_messages()) == 1
    assert '用户名或密码错误' in ''.join((get_flashed_messages()))

    data = {'username': '  ww  ', 'password': '123456'}
    response = client.post('/users/login', data=data)
    assert response.status_code == 302
