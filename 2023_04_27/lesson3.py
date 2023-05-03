from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route("/")
def index():
    message = "<h1>request headers</h1>"
    message += f"<ul><li>host:{request.headers.get('Host')}</li>"
    message += f"<li>host_url:{request.headers.get('host_url')}</li>"
    message += f"<li>user_agent:{request.headers.get('User-Agent')}</li>"
    message +=  f"<li>Accept-Language:{request.headers.get('Accept-Language')}</li>"
    message += f"<li>methos:{request.method}</li></ul>"
    return message

#一. 
#cmd指令輸入'flask --app lesson3 --debug run', 可以隨時更新網頁內容。

#或是

#二.
#在終端機(bash)輸入:
#1. 'export FLASK_APP=lesson3.py'
#2. 'export FLASK_DEBUG=1'
#3. 'flask run'
#也能完成跟上述一樣的事情, 
#不過在關閉終端機(bash)後就失效, 需要再全部重新輸入。

@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello!{name}</h1>"

@app.route("/error")
def error():
    response = make_response("<h1>error</h1>",405)
    response.set_cookie("aa","aaa")
    return response

@app.route("/leeWei")
def leeWei():
    return render_template("index.html")