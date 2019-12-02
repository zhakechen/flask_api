# from application.users.models import *
# from application.users.models import Users, Team
# from werkzeug.security import check_password_hash, generate_password_hash
# import pymysql
# import pytest
#
# from irest.application.users.models import Team
#
#
# def test_create_user(session):
#     user = Users()
#
#     assert user.id is None
#     user.username = '老妈'
#     user.password = '123456'
#     user.mobile = '123321'
#     session.add(user)
#     session.commit()
#
#     assert Users.query.count() == 1
#     assert user.id is not None
#
#     user = Users.query.get(user.id)
#
#
#
#     user2 = Users()
#
#     user2.username = '老妈1'
#     user2.password = generate_password_hash('123456')
#     user2.mobile = '123321'
#
#     try:
#         session.add(user2)
#         session.commit()
#     except Exception as e:
#         session.rowback()
#
#     assert Users.query.count() == 1
#
#
# def test_team_module(session):
#     team = Team()
#     assert team.id is not None
#     team.name = '青蛙队'
#     team.info = 'qazwsxedcrfv'
#     session.add_all(team)
#     session.commit()
#
#     assert Team.query.count() == 1
#     assert team.created_time is not None
#     team = Team.query.get(team.created_time)
#
# # 测试视图
# def test_valid_register(client):
#
