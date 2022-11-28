from flask import Flask, request, render_template

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
    currency_list = [
        {"bank": "a1", "date": "2022-11-25", "currency": "UAH", "buy_rate": 0.025, "sale_rate": 0.023},
        {"bank": "a1", "date": "2022-11-25", "currency": "EUR", "buy_rate": 0.9, "sale_rate": 0.95},
        {"bank": "a1", "date": "2022-11-25", "currency": "USD", "buy_rate": 1, "sale_rate": 1},
        {"bank": "a1", "date": "2022-11-25", "currency": "GPB", "buy_rate": 1.15, "sale_rate": 1.2},
    ]
    if request.method == 'POST':
        user_bank = request.form["bank"]
        user_currency_1 = request.form["currency_1"]
        user_currency_2 = request.form["currency_2"]
        user_date = request.form["date"]
    else:
        return render_template("data_form.html")
    return "Hello"


app.run()
