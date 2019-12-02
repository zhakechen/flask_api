import pytest
from application import create_app, db as database


@pytest.fixture(scope='session')
def app():
    app = create_app('test_settings')
    return app

# 准备db.session表示该fixture只在测试的时候创建一次
@pytest.fixture(scope='session')
def db(app, request):
    database.app = app
    database.create_all()

    # 销毁
    def teardown():
        database.drop_all()
    request.addfinalizer(teardown)
    return database

# 准备数据库session
@pytest.fixture(scope='function')
def session(db, request):
    session = db.create_scoped_session()
    db.session = session

    def teardown():
        session.remove()

    request.addfinalizer(teardown)
    return session







