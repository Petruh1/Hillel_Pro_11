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
        {"bank": "A1", "date": "2022-11-25", "currency": "UAH", "buy_rate": 0.025, "sale_rate": 0.023},
        {"bank": "A1", "date": "2022-11-25", "currency": "EUR", "buy_rate": 0.9, "sale_rate": 0.95},
        {"bank": "A1", "date": "2022-11-25", "currency": "USD", "buy_rate": 1, "sale_rate": 1},
        {"bank": "A1", "date": "2022-11-25", "currency": "GPB", "buy_rate": 1.15, "sale_rate": 1.2},

        {"bank": "Monobank", "date": "2022-11-25", "currency": "UAH", "buy_rate": 0.026, "sale_rate": 0.03},
        {"bank": "Monobank", "date": "2022-11-25", "currency": "EUR", "buy_rate": 0.95, "sale_rate": 0.97},
        {"bank": "Monobank", "date": "2022-11-25", "currency": "USD", "buy_rate": 1, "sale_rate": 1},
        {"bank": "Monobank", "date": "2022-11-25", "currency": "GPB", "buy_rate": 1.16, "sale_rate": 1.6},
    ]
    if request.method == 'POST':
        user_bank = request.form["bank"]
        user_currency_1 = request.form["currency_1"]
        user_currency_2 = request.form["currency_2"]
        user_date = request.form["date"]
        buy_rate_1 = 0
        buy_rate_2 = 0
        sale_rate_1 = 0
        sale_rate_2 = 0
        for one_currency_info in currency_list:
            if user_bank == one_currency_info["bank"] and user_currency_1 == one_currency_info["currency"] \
                and user_date == one_currency_info["date"]:
                buy_rate_1 = one_currency_info["buy_rate"]
                sale_rate_1 = one_currency_info["sale_rate"]
            if user_bank == one_currency_info["bank"] and user_currency_2 == one_currency_info["currency"] \
                    and user_date == one_currency_info["date"]:
                buy_rate_2 = one_currency_info["buy_rate"]
                sale_rate_2 = one_currency_info["sale_rate"]

        cur_exchange_buy = buy_rate_2 / buy_rate_1
        cur_exchange_sale = sale_rate_2 / sale_rate_1
        return render_template("data_form.html", cur_exchange_buy=cur_exchange_buy,
                               user_currency_1=user_currency_1, user_currency_2=user_currency_2, cur_exchange_sale=cur_exchange_sale)
    else:
        return render_template("data_form.html")

app.run()
