import sqlite3

conn = sqlite3.connect('sarawak_dictionary.db')
cursor = conn.cursor()

with open('sarawak_dictionary.sql', 'r', encoding='utf-8') as file:
    sql_script = file.read()

cursor.executescript(sql_script)

conn.commit()
conn.close()
print("✅ Database berjaya dibuat dan data dimasukkan!")




