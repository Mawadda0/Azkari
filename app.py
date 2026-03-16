import os

from flask import Flask, render_template, request, redirect, session,  url_for
from flask_session import Session
from cs50 import SQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///data.db")


def apology(message):
    return render_template("apology.html", message = message)

@app.route("/")
def index():
    return render_template("index.html")

    
@app.route("/home")
def home():

    if "user_id" not in session:
        return redirect("/login")

    return render_template("home.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    if (request.method == "POST"):
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return apology("Make sure to enter username and password.")
        
        if password != confirmation:
            return apology("Password and confirmation must match.")
        
        existing = db.execute("SELECT * FROM users WHERE username = ?", username)
        if existing:
            return apology("This username is already used.")
        
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))
        return redirect("/login")
    
    else:
        return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        session.clear()

        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return apology("Make sure to enter username and password.")

        user = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(user) != 1 or not check_password_hash(user[0]["hash"], password):
            return apology("Invalid username or password")

        session["user_id"] = user[0]["id"]

        return redirect("/home")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/morning")
def morning():
    return render_template("alsabah.html")

@app.route("/evening")
def evening():
    return render_template("almasaa.html")

@app.route("/tasbeeh")
def tasbeeh():
    return render_template("askare.html")