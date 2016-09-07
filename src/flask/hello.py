# -*- coding: utf-8 -*-
__author__ = 'Administrator'

from flask import Flask,request,render_template

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/usr/<username>')
def show_user_profile(username):
    return 'welcome,' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "登录"
    else:
        return "跳转去登录页面"



#模板渲染,需要引入render_template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)