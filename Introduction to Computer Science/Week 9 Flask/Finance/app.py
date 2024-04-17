import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Get all stocks from history
    # Stock is list of dictionaries with values "symbol" and "count"
    stocks = db.execute(
        "SELECT symbol, SUM(shares) AS shares FROM history WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",
        session["user_id"],
    )
    # print(stocks)
    # Save amount of of cash in variable
    cash = round(
        db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0][
            "cash"
        ],
        2,
    )
    # print(cash)
    total_cash = cash

    for stock in stocks:
        symbol = lookup(stock["symbol"])
        # update stocks price
        stock["price"] = symbol["price"]
        stock["value"] = round(stock["price"] * stock["shares"], 2)
        total_cash = round(total_cash + stock["value"], 2)
        # print(stock)

    # print(total_cash)

    return render_template(
        "index.html", stocks=stocks, cash=cash, total_cash=total_cash
    )
    # return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Symbol is a dictionary
        symbol = lookup(request.form.get("symbol").strip())
        # Shares are number of shares user want to buy
        try:
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("invalid shares")
        if not symbol:
            return apology("invalid symbol")
        # Check for valid shares
        elif shares <= 0:
            return apology("please enter the valid number of shares.")
        # Check how much cash ve have
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0][
            "cash"
        ]
        # Calculate price of shares
        price = round(symbol["price"] * shares, 2)
        # If have cash buy shares
        if cash < price:
            return apology("insufficient funds")
        # Update users table and purchased share to table
        db.execute(
            "UPDATE users SET cash = cash - ? WHERE id = ?", price, session["user_id"]
        )
        # Add transaction to history table
        db.execute(
            "INSERT INTO history (user_id, symbol, shares, price) VALUES (?, ?, ? ,?)",
            session["user_id"],
            symbol["symbol"],
            shares,
            symbol["price"],
        )
        name = symbol["symbol"]
        flash(f"Bought {shares} {name} at price of {usd(price)} per share.")
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    # Select all data from table for current user
    history = db.execute(
        "SELECT * FROM history WHERE user_id = ? ORDER BY timestamp DESC",
        session["user_id"],
    )
    return render_template("history.html", history=history)
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)
        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        # Redirect user to home page
        return redirect("/")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        # Symbol is a dictionary with keys name, symbol and price
        symbol = lookup(request.form.get("symbol"))
        # If lookup dosent find symbol it returns None
        if symbol:
            return render_template("quote.html", symbol=symbol)
        return apology("invalid symbol")
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # Forget any user_id
    session.clear()
    # Ensure username was submitted
    if request.method == "POST":
        # Ensure ussername is submitted
        if not request.form.get("username"):
            return apology("must provide username")
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")
        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide confirmation")
        # Ensure that passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match")
        # Query database for username
        user_data = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        # Ensure username is not already taken
        if len(user_data):
            return apology("username already taken")
        else:
            db.execute(
                "INSERT INTO users (username, hash) values (?, ?)",
                request.form.get("username"),
                generate_password_hash(request.form.get("password")),
            )
        user_data = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        # Remember which user has logged in
        session["user_id"] = user_data[0]["id"]
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    # Stocks is a list of dictionarys
    stocks = db.execute(
        "SELECT symbol, SUM(shares) AS shares FROM history WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",
        session["user_id"],
    )

    if request.method == "POST":
        symbol = lookup(request.form.get("symbol"))
        try:
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("shares required")
        if not symbol:
            return apology("symbol required")
        elif shares <= 0:
            return apology("invalid number of shares")
        # Insert into hystory
        for stock in stocks:
            if stock["symbol"] == symbol["symbol"]:
                if stock["shares"] < shares:
                    return apology("invalid number of shares")
                db.execute(
                    "INSERT INTO history (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                    session["user_id"],
                    symbol["symbol"],
                    -abs(shares),
                    symbol["price"],
                )
                # Update users portfolio
                profit = round(symbol["price"] * shares, 2)
                db.execute(
                    "UPDATE users SET cash = cash + ? WHERE id = ?",
                    profit,
                    session["user_id"],
                )
                # Flash
                name = symbol["symbol"]
                price = symbol["price"]
                flash(f"Sold {shares} {name} at price of {usd(price)} per share.")
                return redirect("/")
    else:
        return render_template("sell.html", stocks=stocks)


@app.route("/topup", methods=["GET", "POST"])
@login_required
def topup():
    # User data
    data = db.execute("SELECT username, cash FROM users WHERE id = ?", session["user_id"])[0]
    if request.method == "POST":
        try:
            cash = round(int(request.form.get("cash")), 2)
            if cash < 15:
                return apology("minimal topup is 15$")
        except ValueError:
            return apology("invalid input")
        # update db
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", cash, session["user_id"])
        flash(f"Deposited {usd(cash)}.")
        return redirect("topup")

    else:
        return render_template("topup.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
