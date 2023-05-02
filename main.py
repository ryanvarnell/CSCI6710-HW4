from flask import Flask, render_template, g, current_app, url_for, request, jsonify
import sqlite3
import base64

DATABASE = 'styles.db'
app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/home")
def home():
    conn = get_db()
    cursor = conn.cursor()
    # Rest of the code
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

# get images for tops and bottom slideshows
def get_tops_and_bottoms():
    conn = sqlite3.connect('styles.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clothing WHERE type='top'")
    tops = cursor.fetchall()

    cursor.execute("SELECT * FROM clothing WHERE type='bottom'")
    bottoms = cursor.fetchall()

    conn.close()
    return tops, bottoms

# populate shop.html with top and bottom photos
@app.route('/shop')
def shop():
    tops, bottoms = get_tops_and_bottoms()
    types, sizes, prices, colors = fetch_filter_data()
    return render_template('shop.html', tops=tops, bottoms=bottoms, types=types, sizes=sizes, prices=prices, colors=colors)

# get filters from database
def fetch_filter_data():
    conn = sqlite3.connect('styles.db')
    c = conn.cursor()

    c.execute("SELECT DISTINCT type FROM clothing")
    types = [row[0] for row in c.fetchall()]

    c.execute("SELECT DISTINCT size FROM clothing")
    sizes = [row[0] for row in c.fetchall()]

    c.execute("SELECT DISTINCT price FROM clothing")
    prices = [row[0] for row in c.fetchall()]

    c.execute("SELECT DISTINCT color FROM clothing")
    colors = [row[0] for row in c.fetchall()]

    conn.close()

    return types, sizes, prices, colors



@app.route("/community")
def community():
    return render_template("community.html")

@app.route("/user")
def user():
    return render_template("user.html")

@app.route("/login")
def login():
    return render_template("login.html")


def get_db_connection():
    conn = sqlite3.connect('styles.db')
    conn.row_factory = sqlite3.Row
    return conn


if __name__ == "__main__":
    app.run(debug=True)
