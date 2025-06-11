import sqlite3
import click
from flask import Flask, request, redirect, url_for, render_template, flash, session, g, current_app
from datetime import datetime

app = Flask(__name__)
app.secret_key = "sarawakdictionary"

# ---------- DATABASE SETUP ----------

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("sarawak_dictionary.db")
    db.row_factory = sqlite3.Row
    return db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

init_app(app)

# ---------- HELPER FUNCTION ----------

def is_admin():
    if not session.get('logged_in'):
        return False

    username = session.get('username')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(users)")
    columns = [column[1] for column in cursor.fetchall()]

    if 'admin' not in columns:
        cursor.execute("ALTER TABLE users ADD COLUMN admin INTEGER DEFAULT 0")
        conn.commit()

    cursor.execute("SELECT admin FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    return bool(result and result[0] == 1)

# ---------- ROUTES ----------

@app.route('/', methods=['GET'])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    db = get_db()
    dialects = db.execute("SELECT DISTINCT dialect FROM words").fetchall()
    selected_dialect = request.args.get('dialect')
    query = request.args.get('query', '')

    if query:
        words = db.execute("SELECT id, word, definition, dialect FROM words WHERE word LIKE ? AND approved = 1", (f"%{query}%",)).fetchall()
    elif selected_dialect:
        words = db.execute("SELECT id, word, definition, dialect FROM words WHERE dialect = ? AND approved = 1", (selected_dialect,)).fetchall()
    else:
        words = db.execute("SELECT id, word, definition, dialect FROM words WHERE approved = 1").fetchall()

    return render_template('home.html', words=words, dialects=dialects, selected_dialect=selected_dialect, is_admin=is_admin())

@app.route('/add', methods=['POST'])
def add():
    word = request.form['word']
    definition = request.form['definition']
    dialect = request.form['dialect']
    approved = 1 if is_admin() else 0

    conn = get_db()
    conn.execute("INSERT INTO words (word, definition, dialect, approved) VALUES (?, ?, ?, ?)", (word, definition, dialect, approved))
    conn.commit()

    flash('Perkataan ditambah dengan jayanya!' if approved else 'Perkataan dihantar untuk kelulusan.')
    return redirect(url_for('index'))

@app.route("/jawapan", methods=['POST'])
def jawapan():
    soal = request.form['query']
    return render_template("jawapan.html", answer=soal)

@app.route('/delete', methods=['POST'])
def delete():
    if not is_admin():
        flash('Kebenaran ditolak: Hanya pentadbir boleh memadamkan entri.')
        return redirect(url_for('index'))

    word_id = request.form['id']
    conn = get_db()
    conn.execute("DELETE FROM words WHERE id = ?", (word_id,))
    conn.commit()

    flash('Entri dipadam dengan jayanya')
    return redirect(url_for('index'))

@app.route('/edit/<int:word_id>', methods=['GET'])
def edit(word_id):
    conn = get_db()
    word = conn.execute("SELECT id, word, definition, dialect FROM words WHERE id = ?", (word_id,)).fetchone()

    if not word:
        flash('Entri tidak dijumpai')
        return redirect(url_for('index'))

    return render_template('edit.html', word=word, is_admin=is_admin())

@app.route('/update', methods=['POST'])
def update():
    word_id = request.form['id']
    word = request.form['word']
    definition = request.form['definition']
    dialect = request.form['dialect']

    conn = get_db()

    if is_admin():
        conn.execute("UPDATE words SET word = ?, definition = ?, dialect = ? WHERE id = ?", (word, definition, dialect, word_id))
        conn.commit()
        flash('Entri dikemaskini dengan jayanya')
    else:
        conn.execute('''CREATE TABLE IF NOT EXISTS pending_edits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_id INTEGER NOT NULL,
            word TEXT NOT NULL,
            definition TEXT NOT NULL,
            dialect TEXT NOT NULL,
            submitted_by TEXT NOT NULL,
            submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.execute("INSERT INTO pending_edits (original_id, word, definition, dialect, submitted_by) VALUES (?, ?, ?, ?, ?)", (word_id, word, definition, dialect, session.get('username', 'unknown')))
        conn.commit()
        flash('Permintaan pengeditan telah dihantar untuk kelulusan pentadbir')

    return redirect(url_for('index'))

@app.route('/admin', methods=['GET'])
def admin_panel():
    if not is_admin():
        flash('Kebenaran ditolak: Akses pentadbir diperlukan')
        return redirect(url_for('index'))

    conn = get_db()
    pending_words = conn.execute("SELECT id, word, definition, dialect FROM words WHERE approved = 0").fetchall()

    conn.execute('''CREATE TABLE IF NOT EXISTS pending_edits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_id INTEGER NOT NULL,
        word TEXT NOT NULL,
        definition TEXT NOT NULL,
        dialect TEXT NOT NULL,
        submitted_by TEXT NOT NULL,
        submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')

    pending_edits = conn.execute('''
    SELECT pe.id, pe.original_id, w.word AS original_word, w.definition AS original_definition,
           w.dialect AS original_dialect, pe.word AS new_word, pe.definition AS new_definition,
           pe.dialect AS new_dialect, pe.submitted_by
    FROM pending_edits pe
    JOIN words w ON pe.original_id = w.id
    ''').fetchall()

    return render_template('admin_panel.html', pending_words=pending_words, pending_edits=pending_edits)

@app.route('/approve', methods=['POST'])
def approve_word():
    if not is_admin():
        flash('Kebenaran ditolak: Akses pentadbir diperlukan')
        return redirect(url_for('index'))

    word_id = request.form['id']
    conn = get_db()
    conn.execute("UPDATE words SET approved = 1 WHERE id = ?", (word_id,))
    conn.commit()
    flash('Perkataan diluluskan dan ditambah ke kamus')
    return redirect(url_for('admin_panel'))

@app.route('/reject', methods=['POST'])
def reject_word():
    if not is_admin():
        flash('Kebenaran ditolak: Akses pentadbir diperlukan')
        return redirect(url_for('index'))

    word_id = request.form['id']
    conn = get_db()
    conn.execute("DELETE FROM words WHERE id = ?", (word_id,))
    conn.commit()
    flash('Sumbangan ditolak dan dipadamkan')
    return redirect(url_for('admin_panel'))

@app.route('/approve_edit', methods=['POST'])
def approve_edit():
    if not is_admin():
        flash('Kebenaran ditolak: Akses pentadbir diperlukan')
        return redirect(url_for('index'))

    edit_id = request.form['edit_id']
    conn = get_db()
    edit = conn.execute("SELECT original_id, word, definition, dialect FROM pending_edits WHERE id = ?", (edit_id,)).fetchone()

    if edit:
        conn.execute("UPDATE words SET word = ?, definition = ?, dialect = ? WHERE id = ?", (edit['word'], edit['definition'], edit['dialect'], edit['original_id']))
        conn.execute("DELETE FROM pending_edits WHERE id = ?", (edit_id,))
        conn.commit()
        flash('Pengeditan diluluskan dan dikemaskini')
    else:
        flash('Permintaan pengeditan tidak dijumpai')

    return redirect(url_for('admin_panel'))

@app.route('/reject_edit', methods=['POST'])
def reject_edit():
    if not is_admin():
        flash('Kebenaran ditolak: Akses pentadbir diperlukan')
        return redirect(url_for('index'))

    edit_id = request.form['edit_id']
    conn = get_db()
    conn.execute("DELETE FROM pending_edits WHERE id = ?", (edit_id,))
    conn.commit()
    flash('Permintaan pengeditan ditolak')
    return redirect(url_for('admin_panel'))

# ---------- AUTH ROUTES ----------

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            admin INTEGER DEFAULT 0
        )''')

        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        if cursor.fetchone():
            flash('Username sudah wujud. Sila pilih yang lain.')
            return redirect(url_for('signup'))

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

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            admin INTEGER DEFAULT 0
        )''')

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

if __name__ == '__main__':
    app.run(debug=True)
