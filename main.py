from flask import Flask, render_template, g, current_app, url_for, request
import sqlite3
import base64

app = Flask(__name__)

@app.template_filter('b64encode')
def b64encode(text):
    return base64.b64encode(text).decode('utf-8')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/shop', methods=['GET', 'POST'])
def shop():
    category = request.form.get('category', 'all')
    size = request.form.get('size', 'all')
    color = request.form.get('color', 'all')

    query = 'SELECT * FROM clothing WHERE 1'
    query_params = []

    if category != 'all':
        query += ' AND type = ?'
        query_params.append(category)

    if size != 'all':
        query += ' AND size = ?'
        query_params.append(size)

    if color != 'all':
        query += ' AND color = ?'
        query_params.append(color)

    conn = get_db_connection()
    items = conn.execute(query, query_params).fetchall()
    conn.close()

    tops = [item for item in items if item['type'] == 'top']
    bottoms = [item for item in items if item['type'] == 'bottom']

    return render_template('shop.html', tops=tops, bottoms=bottoms)

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



