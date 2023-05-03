from flask import Flask, render_template, redirect, g, current_app, url_for, request, jsonify, session
import sqlite3
from functools import wraps
import base64

DATABASE = 'styles.db'
app = Flask(__name__)
app.secret_key = 'your_secret_key'

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

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            session['next_url'] = request.url
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def home():
    random_images = get_random_images()
    return render_template("home.html", random_images=random_images)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    check = "Failed to login"
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['username'] = username
            next_url = session.pop('next_url', None)
            if next_url:
                return redirect(next_url)
            else:
                return redirect(url_for('user'))
        else:
            check = "Invalid username or password"
            return render_template('login.html', Check=check)
    else:
        return render_template('login.html', Check=check)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/user', methods=['POST'])
def register():
    check = ""
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        check = "Username already taken"
        return render_template('login.html', Check=check)
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        check = "Registration successful, Welcome {}".format(username)
        return render_template('user.html', Check=check)

# get images for tops and bottom slideshows
def get_tops_and_bottoms(type_filter, size_filter, price_filter, color_filter):
    conn = sqlite3.connect('styles.db')
    cursor = conn.cursor()

    query = "SELECT * FROM clothing WHERE 1=1"
    if type_filter != 'all':
        query += f" AND type='{type_filter}'"
    if size_filter != 'all':
        query += f" AND size='{size_filter}'"
    if price_filter != 'all':
        query += f" AND price='{price_filter}'"
    if color_filter != 'all':
        query += f" AND color='{color_filter}'"

    cursor.execute(query)
    rows = cursor.fetchall()

    tops = []
    bottoms = []
    for row in rows:
        image_data = row[6]
        if row[2] == 'top':
            tops.append((row[0], row[1], row[2], row[3], row[4], row[5], base64.b64encode(image_data).decode('utf-8')))
        else:
            bottoms.append((row[0], row[1], row[2], row[3], row[4], row[5], base64.b64encode(image_data).decode('utf-8')))

    conn.close()
    return tops, bottoms

# 
@app.route('/shop', methods=['GET', 'POST'])
@login_required
def shop():
    if request.method == 'POST':
        type_filter = request.form['type']
        size_filter = request.form['size']
        price_filter = request.form['price']
        color_filter = request.form['color']
    else:
        type_filter = 'all'
        size_filter = 'all'
        price_filter = 'all'
        color_filter = 'all'

    tops, bottoms = get_tops_and_bottoms(type_filter, size_filter, price_filter, color_filter)
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

@app.route('/filter', methods=['POST'])
def filter():
    type_filter = request.form.get('type')
    size_filter = request.form.get('size')
    price_filter = request.form.get('price')
    color_filter = request.form.get('color')

    tops, bottoms = get_tops_and_bottoms(type_filter, size_filter, price_filter, color_filter)

    response_data = {
        'tops': tops,
        'bottoms': bottoms
    }

    return jsonify(response_data)

@app.route('/filter_images', methods=['POST'])
def filter_images():
    filter_data = request.get_json()

    type_filter = filter_data.get('type', 'all')
    size_filter = filter_data.get('size', 'all')
    price_filter = filter_data.get('price', 'all')
    color_filter = filter_data.get('color', 'all')

    tops, bottoms = get_tops_and_bottoms(type_filter, size_filter, price_filter, color_filter)

    response_data = {
        'tops': tops,
        'bottoms': bottoms
    }

    return jsonify(response_data)

@app.route("/community")
@login_required
def community():
    return render_template("community.html")

@app.route("/user")
@login_required
def user():
    return render_template("user.html")

@app.route('/save_outfit', methods=['POST'])
@login_required
def save_outfit():
    outfit_data = request.get_json()

    top_id = outfit_data.get('top_id')
    bottom_id = outfit_data.get('bottom_id')
    user_id = session.get('user_id')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO outfits (user_id, top_id, bottom_id) VALUES (?, ?, ?)", (user_id, top_id, bottom_id))
        conn.commit()
        response_data = {'status': 'success'}
    except sqlite3.Error as e:
        print(e)
        response_data = {'status': 'error'}

    conn.close()

    return jsonify(response_data)


def get_db_connection():
    conn = sqlite3.connect('styles.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.template_filter()
def b64encode(data):
    return base64.b64encode(data).decode('utf-8')


def get_random_images(num_images=4):
    conn = sqlite3.connect('styles.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM clothing ORDER BY RANDOM() LIMIT {num_images}")
    rows = cursor.fetchall()

    images = []
    for row in rows:
        image_data = row[6]
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        images.append({'id': row[0], 'name': row[1], 'price': row[3], 'image_base64': image_base64})

    conn.close()
    return images



if __name__ == "__main__":
    app.run(debug=True)
