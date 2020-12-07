from flask import Flask,request

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello World! NginxFlask'

@app.route("/hello_get", methods=["GET"])
def hello_get():
    username = request.args.get("username")
    return username + '--NginxFlask'

# 客户端不用form表单形式POST提交
@app.route("/hello_post", methods=["POST"])
def hello_post():
    username = request.args.get("username")
    return username + '--NginxFlask'

# 客户端用form表单形式POST提交
@app.route("/hello_post_form", methods=["POST"])
def hello_post_form():
    username = request.form.get("username")
    return username + '--NginxFlask'

@app.route("/hello_getpost", methods=["GET", "POST"])
def hello_getpost():
    if request.method == "POST":
        username = request.form.get("username")
    else:
        username = request.args.get("username")
    return username + '--NginxFlask'

if __name__ == '__main__':
    app.run(host='10.5.9.57',port=5003)