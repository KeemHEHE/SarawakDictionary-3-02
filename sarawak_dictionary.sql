CREATE TABLE words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sarawak_word TEXT NOT NULL,
    meaning TEXT NOT NULL,
    word_type TEXT,
    dialect TEXT,
    example_sentence TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO words (sarawak_word, meaning, word_type, dialect, example_sentence)
VALUES
('ngiga', 'mencari', 'kata kerja', 'Iban', 'Aku ngiga kerja baru.'),
('bani', 'tidak mahu', 'kata kerja', 'Bidayuh', 'Dia bani makan.'),
('bebalin', 'bodoh', 'kata adjektif', 'Melanau', 'Jangan bebaling sangat.');
