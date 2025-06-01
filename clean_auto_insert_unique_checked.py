
import sqlite3

# Sambung ke database
conn = sqlite3.connect('sarawak_dictionary.db')
cursor = conn.cursor()

# Senarai perkataan nak dimasukkan
words = [
    ("nyin", "kamu semua", "Melanau"),
    ("mun", "kalau", "Iban"),
    ("kamek", "saya / aku", "Iban"),
    ("ya", "itu", "Sarawak Malay"),
    ("tambuk", "baling", "Melanau"),
    ("nadai", "tiada", "Bidayuh"),
    ("sauk", "ambil", "Bidayuh"),
    ("nyamai", "sedap / enak", "Bidayuh"),
    ("tok", "ini", "Iban"),
    ("makan", "makan", "Bidayuh"),
    ("bisi", "ada", "Melanau"),
    ("belama", "lama / berlama-lama", "Melanau"),
    ("ngeri", "menakutkan", "Sarawak Malay"),
    ("madah", "beritahu", "Melanau"),
    ("tegak", "berdiri", "Sarawak Malay"),
    ("ngiga", "mencari", "Sarawak Malay"),
    ("pandei", "pandai/bijak", "Bidayuh"),
    ("gerek", "best / seronok", "Melanau"),
    ("kelala", "lupa", "Bidayuh"),
    ("pauk", "kena / dapat", "Sarawak Malay"),
    ("kupi", "kopi", "Iban"),
    ("tangga", "lihat / tengok", "Bidayuh"),
    ("kacak", "cakap", "Melanau"),
    ("nyepit", "cubit", "Iban"),
    ("bek", "jangan", "Iban"),
    ("aruk", "nasi goreng", "Melanau"),
    ("sik", "tidak", "Sarawak Malay"),
    ("ngansam", "simpan", "Melanau"),
    ("kitak", "awak", "Bidayuh"),
    ("tinduk", "tidur", "Iban"),
    ("ngilu", "sakit bila gigit", "Bidayuh"),
    ("bujur", "betul", "Iban"),
    ("tunggu", "menunggu", "Bidayuh"),
    ("ngan", "dengan", "Bidayuh"),
    ("ngantos", "tunggu / menunggu", "Bidayuh"),
    ("jan", "jangan", "Melanau"),
    ("bedau", "belum", "Melanau"),
    ("minum", "minum", "Bidayuh"),
]
# Loop dan masukkan ke dalam database dengan semakan
for word, definition, dialect in words:
    cursor.execute("SELECT COUNT(*) FROM words WHERE word = ?", (word,))
    exists = cursor.fetchone()[0]

    if not exists:
        cursor.execute("INSERT INTO words (word, definition, dialect, approved) VALUES (?, ?, ?, 1)", 
                       (word, definition, dialect))

conn.commit()
conn.close()

print("✅ Semua perkataan unik berjaya dimasukkan ke dalam database tanpa ulang.")
