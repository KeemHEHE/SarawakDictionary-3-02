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

@app.route('/delete', methods=['POST'])
def delete():
    word_id = request.form['id']
    conn = sqlite3.connect('sarawak_dictionary.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM words WHERE id = ?", (word_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

