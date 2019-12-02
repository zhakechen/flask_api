
from flask import Flask


def test_app(app):
    # assert 表示断言
    assert isinstance(app, Flask)
