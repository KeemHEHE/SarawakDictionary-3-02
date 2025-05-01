import sqlite3
import click
from flask import Flask, request, redirect, url_for, render_template, flash, session, g, current_app

app = Flask(__name__)
app.secret_key = "sarawakdictionary"

# HTML template with delete option


@app.route('/', methods=['GET'])
def index():
    # Only show dictionary content if logged in
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    query = request.args.get('query', '')
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

# Database utility functions
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('sarawak_dictionary.db')
    return g.db

def close_db(e=None):
    """Close the database at the end of the request."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

# Authentication routes
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Check if username already exists
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            conn.close()
            flash('Username already exists. Please choose another one.')
            return redirect(url_for('signup'))
        
        # Insert new user
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session['logged_in'] = True
            session['username'] = username
            flash('Login successful! Welcome, ' + username)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
    
    return render_template('sign_in.html')

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('You have been logged out')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

init_app(app)