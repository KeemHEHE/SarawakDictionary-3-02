
import sqlite3

# Sambung ke database
conn = sqlite3.connect('sarawak_dictionary.db')
cursor = conn.cursor()

# Padam semua word yang duplicate, simpan hanya yang pertama (ikut ID terkecil)
cursor.execute("""
DELETE FROM words
WHERE id NOT IN (
    SELECT MIN(id)
    FROM words
    GROUP BY word
);
""")
conn.commit()
conn.close()

print("✅ Semua perkataan duplicate berjaya dipadam. Hanya tinggal satu salinan setiap perkataan.")
