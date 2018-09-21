# -*- coding:utf-8 -*-
'''
@Time    : 2018/9/14 15:32
@Author  : Fate
@File    : userModel.py 用户数据模型
'''

from App.extensions import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    # 用户名
    username = db.Column(db.String(32), unique=True)
    # 密码
    password = db.Column(db.String(128), nullable=False)
    # 头像 保存图片名 或图片路径
    avatar = db.Column(db.String(128), nullable=True)
