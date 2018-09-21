# -*- coding:utf-8 -*-
'''
@Time    : 2018/9/13 9:56
@Author  : Fate
@File    : user.py 用户视图
'''
import os
from flask import Blueprint, render_template, redirect, url_for, request, flash
from App.forms import UserLogin, UserRegister
from werkzeug.security import generate_password_hash
from App.extensions import photos
from App.models import Users
from App.extensions import db
import uuid
from flask_mail import Message
from flask import current_app
from App.extensions import mail

user = Blueprint('user', __name__)


@user.route('/login/', methods=['GET', 'POST'])
def user_login():
    form = UserLogin()

    # 提交判断
    if form.validate_on_submit():
        # 成功后重定向 到首页
        # check_password_hash() 校验密码
        response = redirect(url_for('main.hello_main'))
        return response
    return render_template('user/login.html', form=form)


@user.route('/index/')
def user_index():
    return 'user Index'


@user.route('/register/', methods=['GET', 'POST'])
def user_register():
    # 注册表单对象
    form = UserRegister()
    # 判断提交
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # 密码需要加密
        password = generate_password_hash(password)
        # 保存图片
        avatar = form.avatar.data
        avatar_name = avatar.filename
        # 图片后缀
        suffix = os.path.splitext(avatar_name)[1]
        affix = uuid.uuid4()
        avatar_name = str(affix) + suffix

        # 使用上传集保存图片
        photos.save(avatar, name=avatar_name)

        # 保存到数据库
        user = Users()
        user.username = username
        user.password = password
        user.avatar = avatar_name
        db.session.add(user)

        flash('注册成功')

    return render_template('user/register.html', form=form)


@user.route('/send_mail/')
def send_email():
    from App.email import send_mail
    send_mail(subject='激活',
              recipients='fate9527@aliyun.com',
              email_tmp='active',
              username='fate')

    return '邮箱发送成功'
