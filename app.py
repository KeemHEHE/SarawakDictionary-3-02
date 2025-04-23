from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'sarawak_dict.db'

@app.route('/')
def homepage():
    return render_template("main.html")

# --- Initialize Database (run only once) ---
def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE dictionary (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sarawak TEXT NOT NULL,
                bm TEXT NOT NULL,
                english TEXT,
                category TEXT
            )
        ''')
        conn.commit()
        conn.close()

# --- Helper to connect to DB ---
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# --- View All Entries ---
@app.route('/dictionary', methods=['GET'])
def view_dictionary():
    db = get_db()
    cursor = db.execute('SELECT * FROM dictionary')
    entries = [dict(row) for row in cursor.fetchall()]
    return jsonify(entries)

# --- Add New Entry ---
@app.route('/add', methods=['POST'])
def add_word():
    data = request.get_json()
    sarawak = data.get('sarawak')
    bm = data.get('bm')
    english = data.get('english')
    category = data.get('category')

    if not sarawak or not bm:
        return jsonify({'error': 'Missing Sarawak or BM translation'}), 400

    db = get_db()
    db.execute(
        'INSERT INTO dictionary (sarawak, bm, english, category) VALUES (?, ?, ?, ?)',
        (sarawak, bm, english, category)
    )
    db.commit()
    return jsonify({'message': 'Word added successfully'})

# --- Edit Existing Entry ---
@app.route('/edit/<int:id>', methods=['PUT'])
def edit_word(id):
    data = request.get_json()
    sarawak = data.get('sarawak')
    bm = data.get('bm')
    english = data.get('english')
    category = data.get('category')

    db = get_db()
    db.execute(
        'UPDATE dictionary SET sarawak=?, bm=?, english=?, category=? WHERE id=?',
        (sarawak, bm, english, category, id)
    )
    db.commit()
    return jsonify({'message': 'Word updated successfully'})

# --- Delete Entry ---
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_word(id):
    db = get_db()
    db.execute('DELETE FROM dictionary WHERE id=?', (id,))
    db.commit()
    return jsonify({'message': 'Word deleted successfully'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
