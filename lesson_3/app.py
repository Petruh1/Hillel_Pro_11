from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login_user():
    if request.method == "GET":
        pass
    else:
        pass
    return "<p>Login!</p>"


@app.route("/logout", methods=["GET"])
def logout_user():
    return "<p>Logout!</p>"

@app.route("/register", methods=["GET", "POST"])
def register_user():
    return "Registration form"

@app.route("/user_page", methods=["GET"])
def user_access():
    return "More functions"

@app.route("/currency", methods=["GET", "POST"])
def currency_converter():
    return "Currency converter"