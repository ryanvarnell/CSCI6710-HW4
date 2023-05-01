from flask import Flask, render_template, g, current_app
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/carousel")
def carousel():
    return render_template("carousel.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/community")
def community():
    return render_template("community.html")

@app.route("/user")
def user():
    return render_template("user.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)



