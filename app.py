import sqlite3
import click
import random
from flask import Flask, request, redirect, url_for, render_template, flash, session, g, current_app
from datetime import datetime

app = Flask(__name__)
app.secret_key = "sarawakdictionary"

@app.route('/', methods=['GET'])
def index():
    # Only show dictionary content if logged in
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    query = request.args.get('query', '')
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    if query:
        cursor.execute("SELECT id, word, definition, dialect FROM words WHERE word LIKE ? AND approved = 1", (f"%{query}%",))
    else:
        cursor.execute("SELECT id, word, definition, dialect FROM words WHERE approved = 1")
    rows = cursor.fetchall()
    conn.close()
    
    # Check if user is admin
    is_admin_user = is_admin()
    
    return render_template("home.html", rows=rows, is_admin=is_admin_user)

@app.route('/add', methods=['POST'])
def add():
    word = request.form['word']
    definition = request.form['definition']
    dialect = request.form['dialect']
    
    # Check if user is admin
    admin_status = is_admin()
    
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    
    # If admin, auto-approve the word, otherwise mark as pending
    approved = 1 if admin_status else 0
    
    cursor.execute(
        "INSERT INTO words (word, definition, dialect, approved) VALUES (?, ?, ?, ?)",
        (word, definition, dialect, approved)
    )
    conn.commit()
    conn.close()
    
    if approved:
        flash('Perkataan ditambah dengan jayanya!')
    else:
        flash('Perkataan dihantar untuk kelulusan. Ia akan muncul selepas semakan pentadbir.')
    
    return redirect(url_for('index'))

@app.route("/jawapan", methods=['POST'])
def jawapan():
    soal = request.form['query']
    return render_template("jawapan.html", answer=soal)

@app.route('/delete', methods=['POST'])
def delete():
    # Only allow admin to delete words
    if not is_admin():
        flash('Kebenaran ditolak: Hanya pentadbir boleh memadamkan entri.')
        return redirect(url_for('index'))
    
    word_id = request.form['id']
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM words WHERE id = ?", (word_id,))
    conn.commit()
    conn.close()
    
    flash('Entri dipadam dengan jayanya')
    return redirect(url_for('index'))

@app.route('/edit/<int:word_id>', methods=['GET'])
def edit(word_id):
    # Get word data
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, word, definition, dialect FROM words WHERE id = ?", (word_id,))
    word = cursor.fetchone()
    conn.close()
    
    if not word:
        flash('Entri tidak dijumpai')
        return redirect(url_for('index'))
    
    # Both admin and normal users can access the edit page
    # but the form submission will be handled differently
    is_admin_user = is_admin()
        
    return render_template('edit.html', word=word, is_admin=is_admin_user)

@app.route('/update', methods=['POST'])
def update():
    word_id = request.form['id']
    word = request.form['word']
    definition = request.form['definition']
    dialect = request.form['dialect']
    
    # Check if user is admin
    admin_status = is_admin()
    
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    
    if admin_status:
        # Admin edits are applied directly
        cursor.execute(
            "UPDATE words SET word = ?, definition = ?, dialect = ? WHERE id = ?", 
            (word, definition, dialect, word_id)
        )
        conn.commit()
        conn.close()
        
        flash('Entri dikemaskini dengan jayanya')
    else:
        # For normal users, create a pending edit
        # First, get the original word data
        cursor.execute("SELECT word, definition, dialect FROM words WHERE id = ?", (word_id,))
        original = cursor.fetchone()
        
        if not original:
            conn.close()
            flash('Entri asal tidak dijumpai')
            return redirect(url_for('index'))
        
        # Create pending_edits table if it doesn't exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS pending_edits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_id INTEGER NOT NULL,
            word TEXT NOT NULL,
            definition TEXT NOT NULL,
            dialect TEXT NOT NULL,
            submitted_by TEXT NOT NULL,
            submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Store the edit request
        cursor.execute(
            "INSERT INTO pending_edits (original_id, word, definition, dialect, submitted_by) VALUES (?, ?, ?, ?, ?)",
            (word_id, word, definition, dialect, session.get('username', 'unknown'))
        )
        conn.commit()
        conn.close()
        
        flash('Permintaan pengeditan telah dihantar untuk kelulusan pentadbir')
    
    return redirect(url_for('index'))

# Admin Panel Routes
@app.route('/admin', methods=['GET'])
def admin_panel():
    if not is_admin():
        flash('Kebenaran ditolak: Akses pentadbir diperlukan')
        return redirect(url_for('index'))
    
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    
    # Get pending words
    cursor.execute(
        "SELECT id, word, definition, dialect FROM words WHERE approved = 0"
    )
    pending_words = cursor.fetchall()
    
    # Create pending_edits table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pending_edits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_id INTEGER NOT NULL,
        word TEXT NOT NULL,
        definition TEXT NOT NULL,
        dialect TEXT NOT NULL,
        submitted_by TEXT NOT NULL,
        submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Get pending edits with original data
    cursor.execute('''
    SELECT pe.id, pe.original_id, w.word AS original_word, w.definition AS original_definition, 
           w.dialect AS original_dialect, pe.word AS new_word, pe.definition AS new_definition, 
           pe.dialect AS new_dialect, pe.submitted_by
    FROM pending_edits pe
    JOIN words w ON pe.original_id = w.id
    ''')
    pending_edits = cursor.fetchall()
    
    conn.close()
    return render_template('admin_panel.html', pending_words=pending_words, pending_edits=pending_edits)

@app.route('/approve', methods=['POST'])
def approve_word():
    if not is_admin():
        flash('Kebenaran ditolak: Akses pentadbir diperlukan')
        return redirect(url_for('index'))
    
    word_id = request.form['id']
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE words SET approved = 1 WHERE id = ?", (word_id,))
    conn.commit()
    conn.close()
    
    flash('Perkataan diluluskan dan ditambah ke kamus')
    return redirect(url_for('admin_panel'))

@app.route('/reject', methods=['POST'])
def reject_word():
    if not is_admin():
        flash('Kebenaran ditolak: Akses pentadbir diperlukan')
        return redirect(url_for('index'))
    
    word_id = request.form['id']
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM words WHERE id = ?", (word_id,))
    conn.commit()
    conn.close()
    
    flash('Sumbangan ditolak dan dipadamkan')
    return redirect(url_for('admin_panel'))

@app.route('/approve_edit', methods=['POST'])
def approve_edit():
    if not is_admin():
        flash('Kebenaran ditolak: Akses pentadbir diperlukan')
        return redirect(url_for('index'))
    
    edit_id = request.form['edit_id']
    
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    
    # Get the edit details
    cursor.execute(
        "SELECT original_id, word, definition, dialect FROM pending_edits WHERE id = ?", 
        (edit_id,)
    )
    edit = cursor.fetchone()
    
    if edit:
        original_id, word, definition, dialect = edit
        
        # Apply the edit
        cursor.execute(
            "UPDATE words SET word = ?, definition = ?, dialect = ? WHERE id = ?", 
            (word, definition, dialect, original_id)
        )
        
        # Remove the pending edit
        cursor.execute("DELETE FROM pending_edits WHERE id = ?", (edit_id,))
        
        conn.commit()
        flash('Pengeditan diluluskan dan dikemaskini')
    else:
        flash('Permintaan pengeditan tidak dijumpai')
    
    conn.close()
    return redirect(url_for('admin_panel'))

@app.route('/reject_edit', methods=['POST'])
def reject_edit():
    if not is_admin():
        flash('Kebenaran ditolak: Akses pentadbir diperlukan')
        return redirect(url_for('index'))
    
    edit_id = request.form['edit_id']
    
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    
    # Remove the pending edit
    cursor.execute("DELETE FROM pending_edits WHERE id = ?", (edit_id,))
    conn.commit()
    conn.close()
    
    flash('Permintaan pengeditan ditolak')
    return redirect(url_for('admin_panel'))

# Helper function to check if current user is admin
def is_admin():
    if not session.get('logged_in'):
        return False
    
    username = session.get('username')
    
    # Create users database if it doesn't exist
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    
    # Check if admin column exists, if not create it
    cursor.execute("PRAGMA table_info(users)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'admin' not in columns:
        cursor.execute("ALTER TABLE users ADD COLUMN admin INTEGER DEFAULT 0")
        conn.commit()
    
    cursor.execute("SELECT admin FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    
    return bool(result and result[0] == 1)

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
        
        conn = sqlite3.connect('sarawak_dictionary.db')
        cursor = conn.cursor()
        
        # Create users table if it doesn't exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            admin INTEGER DEFAULT 0
        )
        ''')
        
        # Check if username already exists
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            conn.close()
            flash('Username sudah wujud. Sila pilih yang lain.')
            return redirect(url_for('signup'))
        
        # Insert new user (default admin=0)
        cursor.execute('INSERT INTO users (username, password, admin) VALUES (?, ?, 0)', (username, password))
        conn.commit()
        conn.close()
        
        flash('Pendaftaran berjaya! Sila log masuk.')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('sarawak_dictionary.db')
        cursor = conn.cursor()
        
        # Create users table if it doesn't exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            admin INTEGER DEFAULT 0
        )
        ''')
        
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session['logged_in'] = True
            session['username'] = username
            flash('Log masuk berjaya! Selamat datang, ' + username)
            return redirect(url_for('index'))
        else:
            flash('Username atau kata laluan tidak sah')
            return redirect(url_for('login'))
    
    return render_template('sign_in.html')

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('Anda telah log keluar')
    return redirect(url_for('login'))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("sarawak_dictionary.db")
    db.row_factory = sqlite3.Row
    return db

# sorting dialect
@app.route('/', methods=['GET'])
def dialect():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    query = request.args.get('query', '')
    selected_dialect = request.args.get('dialect', '')

    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()

    if query and selected_dialect:
        cursor.execute("SELECT id, word, definition, dialect FROM words WHERE word LIKE ? AND dialect = ? AND approved = 1",
                       (f"%{query}%", selected_dialect))
    elif query:
        cursor.execute("SELECT id, word, definition, dialect FROM words WHERE word LIKE ? AND approved = 1",
                       (f"%{query}%",))
    elif selected_dialect:
        cursor.execute("SELECT id, word, definition, dialect FROM words WHERE dialect = ? AND approved = 1",
                       (selected_dialect,))
    else:
        cursor.execute("SELECT id, word, definition, dialect FROM words WHERE approved = 1")

    rows = cursor.fetchall()
    conn.close()

    return render_template("home.html", words=rows, selected_dialect=selected_dialect, query=query, is_admin=is_admin())

@app.route('/quiz')
def quiz():
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    
    # 5 random questions
    cursor.execute("SELECT word, definition FROM words ORDER BY RANDOM() LIMIT 5")
    rows = cursor.fetchall()

    questions = []
    for word, correct_meaning in rows:
        # 3 meaning that is wrong
        cursor.execute("SELECT definition FROM words WHERE definition != ? ORDER BY RANDOM() LIMIT 3", (correct_meaning,))
        wrongs = [row[0] for row in cursor.fetchall()]
        
        choices = wrongs + [correct_meaning]
        random.shuffle(choices)
        
        questions.append({
            "word": word,
            "choices": choices,
            "answer": correct_meaning
        })

    conn.close()
    return render_template('quiz.html', questions=questions)

@app.route('/quiz-result', methods=['POST'])
def quiz_result():
    score = 0
    total = 0
    results = []

    for i in range(total): 
        user_answer = request.form.get(f'q{i}')
        correct_answer = request.form.get(f'answer{i}')
        if not correct_answer:
            break
        total += 1
        results.append({
            "index": i + 1,
            "user": user_answer,
            "correct": correct_answer,
            "status": "✔️" if user_answer == correct_answer else "❌"
        })
        if user_answer == correct_answer:
            score += 1

    return render_template('quiz_result.html', score=score, total=total, results=results)



if __name__ == '_main_':
    app.run(debug=True)

init_app(app)