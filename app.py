import os
import json
import sqlite3
import click
from flask import Flask, request, redirect, url_for, render_template, g, current_app, flash, jsonify


app = Flask(__name__)
DB_FILE = 'dictionary.json'


# HTML template with delete option
template = """
"""

@app.route('/', methods=['GET'])
def index():
    query = request.args.get('query', '')
    row = []
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    if query:
        cursor.execute("SELECT id, word, definition, dialect FROM words WHERE word LIKE ?", (f"%{query}%",))
    else:
        cursor.execute("SELECT id, word, definition, dialect FROM words")
    rows = cursor.fetchall()
    conn.close()
    return render_template("home.html", rows=rows)

@app.route('/add', methods=['POST'])
def add():
    word = request.form['word']
    definition = request.form['definition']
    dialect = request.form['dialect']

    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO words (word, definition, dialect) VALUES (?, ?, ?)", (word, definition, dialect))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route("/jawapan", methods=['POST'])
def jawapan():
    soal = request.form['query']
    return render_template("jawapan.html", answer=soal)

@app.route('/delete', methods=['POST'])
def delete():
    word_id = request.form['id']
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM words WHERE id = ?", (word_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('sarawak_dictionary.db')  # change name if needed
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:  # Make sure schema.sql exists
        db.executescript(f.read().decode('utf8'))

def close_db(e=None):
    """Close the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        flash('Signup berjaya! Sila log masuk.')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cur.fetchone()
        conn.close()
        if user:
            return 'Selamat datang, anda berjaya login!'
        else:
            flash('Username atau password salah')
            return redirect(url_for('login'))
    return render_template('login.html')

if not os.path.exists(DB_FILE):
    with open(DB_FILE, 'w') as f:
        json.dump([], f)

@app.route('/api/add-word', methods=['POST'])
def add_word():
    try:
        data = request.get_json()  # Changed from request.json for better error handling
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        word = data.get('word')
        definition = data.get('definition')
        dialect = data.get('dialect')

        if not word or not definition or not dialect:
            return jsonify({'error': 'Missing word, definition, or dialect'}), 400

        # Read existing words
        with open(DB_FILE, 'r') as f:
            dictionary = json.load(f)

        # Check if word already exists
        if any(entry['word'].lower() == word.lower() and entry['dialect'].lower() == dialect.lower() for entry in dictionary):
            return jsonify({'error': 'Word already exists in this dialect'}), 400

        # Add new word
        dictionary.append({
            'word': word,
            'definition': definition,
            'dialect': dialect
        })

        # Save back to file
        with open(DB_FILE, 'w') as f:
            json.dump(dictionary, f, indent=2)

        return jsonify({'message': 'Word added successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)

if __name__ == '__main__':
    app.run(debug=True)
    init_db()

init_app(app)