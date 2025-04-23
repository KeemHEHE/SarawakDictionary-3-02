import sqlite3
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# HTML template with delete option
template = """
"""

@app.route('/', methods=['GET'])
def index():
    query = request.args.get('query', '')
    results = []
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    if query:
        cursor.execute("SELECT id, word, definition, dialect FROM words WHERE word LIKE ?", (f"%{query}%",))
    else:
        cursor.execute("SELECT id, word, definition, dialect FROM words")
    results = cursor.fetchall()
    conn.close()
    return render_template("home.html")

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

# Setup for sign in and sign up button
def init_db():
    conn = sqlite3.connect('users.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    conn.close()

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

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

