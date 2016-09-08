# -*- coding: utf-8 -*-
__author__ = 'Administrator'

from flask import Flask, request, render_template, url_for, flash, redirect
from werkzeug.utils import secure_filename
import os
import configparser

app = Flask(__name__)
# UPLOAD_FOLDER='g:\\'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# configs = {
#     'db': {
#         'host': '127.0.0.1',
#         'port': 3306,
#         'user': 'www-data',
#         'password': 'www-data',
#         'database': 'awesome'
#     },
#     'DEFAULT': {
#         'UPLOAD_FOLDER': 'g:\\'
#     }
# }

def getConfig(section, key):
    config = configparser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/config/config.properties'
    config.read(path)
    return config.get(section, key)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'welcome, %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


# 接收参数
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return "登录"
    else:
        # request.args.get('username','defaultUser'),如果接收到为None，则会用第二个参数值替代
        if valid_login(request.args.get('username', 'defaultUser'), request.args.get('password')):
            return "跳转去登录页面"
    return "用户名密码错误"


def valid_login(username, password):
    if username != None:
        print("用户名：" + username)
    if password != None:
        print("密  码：" + password)

    if username == "abc" and password == "123":
        return 1
    else:
        return 0


# 模板渲染,需要引入render_template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


ALLOWED_EXTENSIONS =set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET'])
def upload_file_page():
    return render_template('upload.html')


# 表单加上 enctype="multipart/form-data"  ,<input type=file>
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(os.path.join(getConfig('DEFAULT','UPLOAD_FOLDER'), filename))
            return "上传成功，请到文件夹"+getConfig('DEFAULT','UPLOAD_FOLDER')+"下查看！"

        else:
            return "文件格式不支持"

    return 'fail'



# 放最后
if __name__ == "__main__":
    app.run()
