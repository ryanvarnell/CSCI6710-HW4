import sqlite3
import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

"""
import sqlite3
from flask import Flask, g

app = Flask(__name__)
app.config['DATABASE'] = '/path/to/database.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

@app.before_app_request
def before_request():
    g.db = get_db()

@app.teardown_appcontext
def teardown_request(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()
        """
