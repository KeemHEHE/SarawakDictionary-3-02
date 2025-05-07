DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS words;

CREATE TABLE IF NOT EXISTS users (
   id INTEGER PRIMARY KEY, 
   username TEXT, 
   password TEXT
);

CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT NOT NULL,
    definition TEXT NOT NULL,
    word_type TEXT,
    dialect TEXT,
    example_sentence TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);  

INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kitak', 'awak', 'kata ganti nama', 'Iban', 'Kitak pegi mana?', '2025-04-30T09:41:26.538152');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('andak', 'nanti', 'kata keterangan', 'Melanau', 'Andak dulu baru jalan.', '2025-04-30T09:41:26.538185');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('gatai', 'gatal', 'kata adjektif', 'Bidayuh', 'Tangan gatai jak.', '2025-04-30T09:41:26.538190');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('ngiga', 'mencari', 'kata kerja', 'Iban', 'Aku ngiga kerja baru.', '2025-04-30T09:41:26.538194');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bani', 'tidak mahu', 'kata kerja', 'Bidayuh', 'Dia bani makan.', '2025-04-30T09:41:26.538205');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('mun', 'kalau', 'kata hubung', 'Iban', 'Mun kitak datang awal.', '2025-04-30T09:41:26.538229');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kamek', 'saya', 'kata ganti nama', 'Iban', 'Kamek suka makan.', '2025-04-30T09:41:26.538232');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bebalin', 'bodoh', 'kata adjektif', 'Melanau', 'Jangan bebaling sangat.', '2025-04-30T09:41:26.538235');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyau', 'sudah', 'kata bantu', 'Iban', 'Kamek nyau makan.', '2025-04-30T09:41:26.538263');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('ngiga', 'mencari', 'kata kerja', 'Iban', 'Aku ngiga kerja baru.', '2025-04-30T09:41:26.538292');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)