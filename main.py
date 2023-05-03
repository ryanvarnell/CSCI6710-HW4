import base64
import sqlite3
from functools import wraps
from flask import Flask, render_template, redirect, g, url_for, request, jsonify, session

# Initialize database and flask app.
DATABASE = 'styles.db'
app = Flask(__name__)


# Grabs the database.
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# Closes connection to the database.
@app.teardown_appcontext
def close_connection(self):
    db = get_db()
    if db is not None:
        db.close()


# Should redirect the user to sign in if they are not.
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            session['next_url'] = request.url
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# Home page.
@app.route("/")
def home():
    # Grabs random images to display as products on the front page.
    random_images = get_random_images()
    return render_template("home.html", random_images=random_images)


# About page.
@app.route("/about")
def about():
    return render_template("about.html")


# Login page.
@app.route('/login', methods=['GET', 'POST'])
def login():
    check = "Failed to login"
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # Checks to see if the user exists. If the user does not exist, or the username or password is incorrect, it
        # will respond as needed.
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        login_user = cursor.fetchone()
        conn.close()
        if login_user:
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


# Logout page.
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


# User page.
@app.route('/user', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Checks to see if the username already exists. If so, will say so. If not, will create no user.
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


# Gets top and bottom products for display.
def get_tops_and_bottoms(type_filter, size_filter, price_filter, color_filter):
    # Grabs items from styles database.
    conn = sqlite3.connect('styles.db')
    cursor = conn.cursor()
    query = "SELECT * FROM clothing"
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

    # Sorts items into tops and bottoms arrays, indexing is as follows:
    # item[name, type, price, size, color, image].
    tops = []
    bottoms = []
    for row in rows:
        image_data = row[6]
        if row[2] == 'top':
            tops.append((row[0], row[1], row[2], row[3], row[4], row[5], b64encode(image_data)))
        else:
            bottoms.append(
                (row[0], row[1], row[2], row[3], row[4], row[5], b64encode(image_data)))

    conn.close()
    return tops, bottoms


# Shop/carousel page.
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
    return render_template('shop.html', tops=tops, bottoms=bottoms, types=types, sizes=sizes, prices=prices,
                           colors=colors)


# Get filters from database.
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
def item_filter():
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


# Community page.
@app.route("/community")
@login_required
def community():
    return render_template("community.html")


# User page.
@app.route("/user")
@login_required
def user():
    return render_template("user.html")


# Function to save outfit.
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
        cursor.execute("INSERT INTO outfits (user_id, top_id, bottom_id) VALUES (?, ?, ?)",
                       (user_id, top_id, bottom_id))
        conn.commit()
        response_data = {'status': 'success'}
    except sqlite3.Error as e:
        print(e)
        response_data = {'status': 'error'}

    conn.close()

    return jsonify(response_data)


# Get an object connected to the database.
def get_db_connection():
    conn = sqlite3.connect('styles.db')
    conn.row_factory = sqlite3.Row
    return conn


# Function for encoding data into base 64.
@app.template_filter()
def b64encode(data):
    return base64.b64encode(data).decode('utf-8')


# Gets random images of products.
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
