# -*- coding:utf-8 -*-
'''
@Time    : 2018/9/13 11:01
@Author  : Fate
@File    : userForm.py
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf.file import FileField, FileRequired, FileAllowed
from App.extensions import photos


# 登陆表单
class UserLogin(FlaskForm):
    # 用户名
    username = StringField(label='用户名',  # 标签
                           validators=[DataRequired('用户名不能为空')],  # 过滤器
                           )

    # 密码
    password = PasswordField(label='密码',
                             validators=[DataRequired('密码不能为空')])
    # 验证码
    code = StringField(label='验证码',
                       validators=[DataRequired('请输入验证码')])

    # 提交
    submit = SubmitField(label='登录')


# 注册表单
class UserRegister(FlaskForm):
    # 用户名
    username = StringField(label='用户名',
                           validators=[DataRequired('用户名不能为空')])
    # 密码
    password = PasswordField(label='密码',
                             validators=[DataRequired('密码不能为空'),
                                         Length(min=6, max=18, message=('密码太长或太短'))])

    # 确认密码
    rePassword = PasswordField(label='确认密码',
                               validators=[DataRequired('重复密码'),
                                           EqualTo('password', message='两次密码不一致')])
    # 头像
    avatar = FileField(label='头像',
                       validators=[FileRequired('请上传一张图片'),
                                   FileAllowed(photos, message='图片格式不正确')])
    # 提交
    submit = SubmitField(label='注册')
