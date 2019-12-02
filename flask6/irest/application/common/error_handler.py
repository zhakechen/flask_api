from flask import Blueprint, render_template, flash, redirect, url_for, jsonify, request
from marshmallow.exceptions import ValidationError
from application.common.status_code import *
from sqlalchemy.exc import IntegrityError
error = Blueprint('error', __name__)

# 捕获错误
@error.app_errorhandler(ValidationError)
def valid_valid_error(e):
    return jsonify({'code': 400, 'message': e.messages})


@error.app_errorhandler(IntegrityError)
def valid_valid_error(e):
    return jsonify({'code': 400, 'message': '违反唯一约束条件'})