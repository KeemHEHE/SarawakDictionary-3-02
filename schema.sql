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

CREATE TABLE IF NOT EXISTS favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    word_id INTEGER NOT NULL,
    FOREIGN KEY (id) REFERENCES words(id)
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
VALUES ('kitak', 'awak', 'kata ganti nama', 'Iban', 'Kitak pegi mana?', '2025-04-30T09:41:26.538198');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kitak', 'awak', 'kata ganti nama', 'Iban', 'Kitak pegi mana?', '2025-04-30T09:41:26.538202');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bani', 'tidak mahu', 'kata kerja', 'Bidayuh', 'Dia bani makan.', '2025-04-30T09:41:26.538205');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('andak', 'nanti', 'kata keterangan', 'Melanau', 'Andak dulu baru jalan.', '2025-04-30T09:41:26.538213');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bani', 'tidak mahu', 'kata kerja', 'Bidayuh', 'Dia bani makan.', '2025-04-30T09:41:26.538218');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('andak', 'nanti', 'kata keterangan', 'Melanau', 'Andak dulu baru jalan.', '2025-04-30T09:41:26.538222');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bani', 'tidak mahu', 'kata kerja', 'Bidayuh', 'Dia bani makan.', '2025-04-30T09:41:26.538225');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('mun', 'kalau', 'kata hubung', 'Iban', 'Mun kitak datang awal.', '2025-04-30T09:41:26.538229');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kamek', 'saya', 'kata ganti nama', 'Iban', 'Kamek suka makan.', '2025-04-30T09:41:26.538232');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bebalin', 'bodoh', 'kata adjektif', 'Melanau', 'Jangan bebaling sangat.', '2025-04-30T09:41:26.538235');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kamek', 'saya', 'kata ganti nama', 'Iban', 'Kamek suka makan.', '2025-04-30T09:41:26.538238');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bani', 'tidak mahu', 'kata kerja', 'Bidayuh', 'Dia bani makan.', '2025-04-30T09:41:26.538241');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('gatai', 'gatal', 'kata adjektif', 'Bidayuh', 'Tangan gatai jak.', '2025-04-30T09:41:26.538244');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('ngiga', 'mencari', 'kata kerja', 'Iban', 'Aku ngiga kerja baru.', '2025-04-30T09:41:26.538247');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('ngiga', 'mencari', 'kata kerja', 'Iban', 'Aku ngiga kerja baru.', '2025-04-30T09:41:26.538251');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kitak', 'awak', 'kata ganti nama', 'Iban', 'Kitak pegi mana?', '2025-04-30T09:41:26.538254');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('mun', 'kalau', 'kata hubung', 'Iban', 'Mun kitak datang awal.', '2025-04-30T09:41:26.538257');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bebalin', 'bodoh', 'kata adjektif', 'Melanau', 'Jangan bebaling sangat.', '2025-04-30T09:41:26.538260');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyau', 'sudah', 'kata bantu', 'Iban', 'Kamek nyau makan.', '2025-04-30T09:41:26.538263');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bani', 'tidak mahu', 'kata kerja', 'Bidayuh', 'Dia bani makan.', '2025-04-30T09:41:26.538266');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('mun', 'kalau', 'kata hubung', 'Iban', 'Mun kitak datang awal.', '2025-04-30T09:41:26.538269');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kitak', 'awak', 'kata ganti nama', 'Iban', 'Kitak pegi mana?', '2025-04-30T09:41:26.538273');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kamek', 'saya', 'kata ganti nama', 'Iban', 'Kamek suka makan.', '2025-04-30T09:41:26.538276');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kamek', 'saya', 'kata ganti nama', 'Iban', 'Kamek suka makan.', '2025-04-30T09:41:26.538279');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kamek', 'saya', 'kata ganti nama', 'Iban', 'Kamek suka makan.', '2025-04-30T09:41:26.538283');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bani', 'tidak mahu', 'kata kerja', 'Bidayuh', 'Dia bani makan.', '2025-04-30T09:41:26.538286');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('mun', 'kalau', 'kata hubung', 'Iban', 'Mun kitak datang awal.', '2025-04-30T09:41:26.538289');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('ngiga', 'mencari', 'kata kerja', 'Iban', 'Aku ngiga kerja baru.', '2025-04-30T09:41:26.538292');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('gatai', 'gatal', 'kata adjektif', 'Bidayuh', 'Tangan gatai jak.', '2025-04-30T09:41:26.538295');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('gatai', 'gatal', 'kata adjektif', 'Bidayuh', 'Tangan gatai jak.', '2025-04-30T09:41:26.538299');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kamek', 'saya', 'kata ganti nama', 'Iban', 'Kamek suka makan.', '2025-04-30T09:41:26.538302');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kamek', 'saya', 'kata ganti nama', 'Iban', 'Kamek suka makan.', '2025-04-30T09:41:26.538305');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('mun', 'kalau', 'kata hubung', 'Iban', 'Mun kitak datang awal.', '2025-04-30T09:41:26.538307');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kamek', 'saya', 'kata ganti nama', 'Iban', 'Kamek suka makan.', '2025-04-30T09:41:26.538311');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kamek', 'saya', 'kata ganti nama', 'Iban', 'Kamek suka makan.', '2025-04-30T09:41:26.538314');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('andak', 'nanti', 'kata keterangan', 'Melanau', 'Andak dulu baru jalan.', '2025-04-30T09:41:26.538317');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyau', 'sudah', 'kata bantu', 'Iban', 'Kamek nyau makan.', '2025-04-30T09:41:26.538320');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('ngiga', 'mencari', 'kata kerja', 'Iban', 'Aku ngiga kerja baru.', '2025-04-30T09:41:26.538323');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('andak', 'nanti', 'kata keterangan', 'Melanau', 'Andak dulu baru jalan.', '2025-04-30T09:41:26.538326');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kitak', 'awak', 'kata ganti nama', 'Iban', 'Kitak pegi mana?', '2025-04-30T09:41:26.538329');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('gatai', 'gatal', 'kata adjektif', 'Bidayuh', 'Tangan gatai jak.', '2025-04-30T09:41:26.538332');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kamek', 'saya', 'kata ganti nama', 'Iban', 'Kamek suka makan.', '2025-04-30T09:41:26.538343');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kitak', 'awak', 'kata ganti nama', 'Iban', 'Kitak pegi mana?', '2025-04-30T09:41:26.538346');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('mun', 'kalau', 'kata hubung', 'Iban', 'Mun kitak datang awal.', '2025-04-30T09:41:26.538349');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('gatai', 'gatal', 'kata adjektif', 'Bidayuh', 'Tangan gatai jak.', '2025-04-30T09:41:26.538352');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyau', 'sudah', 'kata bantu', 'Iban', 'Kamek nyau makan.', '2025-04-30T09:41:26.538355');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bebalin', 'bodoh', 'kata adjektif', 'Melanau', 'Jangan bebaling sangat.', '2025-04-30T09:41:26.538358');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bani', 'tidak mahu', 'kata kerja', 'Bidayuh', 'Dia bani makan.', '2025-04-30T09:41:26.538362');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bebalin', 'bodoh', 'kata adjektif', 'Melanau', 'Jangan bebaling sangat.', '2025-04-30T09:41:26.538365');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyau', 'sudah', 'kata bantu', 'Iban', 'Kamek nyau makan.', '2025-04-30T09:41:26.538368');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bebalin', 'bodoh', 'kata adjektif', 'Melanau', 'Jangan bebaling sangat.', '2025-04-30T09:41:26.538371');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('andak', 'nanti', 'kata keterangan', 'Melanau', 'Andak dulu baru jalan.', '2025-04-30T09:41:26.538374');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('ngiga', 'mencari', 'kata kerja', 'Iban', 'Aku ngiga kerja baru.', '2025-04-30T09:41:26.538377');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('andak', 'nanti', 'kata keterangan', 'Melanau', 'Andak dulu baru jalan.', '2025-04-30T09:41:26.538380');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('andak', 'nanti', 'kata keterangan', 'Melanau', 'Andak dulu baru jalan.', '2025-04-30T09:41:26.538383');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kitak', 'awak', 'kata ganti nama', 'Iban', 'Kitak pegi mana?', '2025-04-30T09:41:26.538387');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyau', 'sudah', 'kata bantu', 'Iban', 'Kamek nyau makan.', '2025-04-30T09:41:26.538390');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bebalin', 'bodoh', 'kata adjektif', 'Melanau', 'Jangan bebaling sangat.', '2025-04-30T09:41:26.538393');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bani', 'tidak mahu', 'kata kerja', 'Bidayuh', 'Dia bani makan.', '2025-04-30T09:41:26.538396');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyamai', 'sedap', 'kata adjektif', 'Iban', 'Makanan tok nyamai gilak.', '2025-04-30T09:41:26.538406');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyamai', 'sedap', 'kata adjektif', 'Iban', 'Makanan tok nyamai gilak.', '2025-04-30T09:41:26.538409');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('gatai', 'gatal', 'kata adjektif', 'Bidayuh', 'Tangan gatai jak.', '2025-04-30T09:41:26.538412');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bebalin', 'bodoh', 'kata adjektif', 'Melanau', 'Jangan bebaling sangat.', '2025-04-30T09:41:26.538415');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyamai', 'sedap', 'kata adjektif', 'Iban', 'Makanan tok nyamai gilak.', '2025-04-30T09:41:26.538418');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('andak', 'nanti', 'kata keterangan', 'Melanau', 'Andak dulu baru jalan.', '2025-04-30T09:41:26.538422');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('gatai', 'gatal', 'kata adjektif', 'Bidayuh', 'Tangan gatai jak.', '2025-04-30T09:41:26.538425');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('mun', 'kalau', 'kata hubung', 'Iban', 'Mun kitak datang awal.', '2025-04-30T09:41:26.538427');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('gatai', 'gatal', 'kata adjektif', 'Bidayuh', 'Tangan gatai jak.', '2025-04-30T09:41:26.538430');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyamai', 'sedap', 'kata adjektif', 'Iban', 'Makanan tok nyamai gilak.', '2025-04-30T09:41:26.538433');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyamai', 'sedap', 'kata adjektif', 'Iban', 'Makanan tok nyamai gilak.', '2025-04-30T09:41:26.538436');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('ngiga', 'mencari', 'kata kerja', 'Iban', 'Aku ngiga kerja baru.', '2025-04-30T09:41:26.538439');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('gatai', 'gatal', 'kata adjektif', 'Bidayuh', 'Tangan gatai jak.', '2025-04-30T09:41:26.538442');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyau', 'sudah', 'kata bantu', 'Iban', 'Kamek nyau makan.', '2025-04-30T09:41:26.538446');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bebalin', 'bodoh', 'kata adjektif', 'Melanau', 'Jangan bebaling sangat.', '2025-04-30T09:41:26.538449');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyamai', 'sedap', 'kata adjektif', 'Iban', 'Makanan tok nyamai gilak.', '2025-04-30T09:41:26.538452');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('ngiga', 'mencari', 'kata kerja', 'Iban', 'Aku ngiga kerja baru.', '2025-04-30T09:41:26.538455');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bani', 'tidak mahu', 'kata kerja', 'Bidayuh', 'Dia bani makan.', '2025-04-30T09:41:26.538458');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('gatai', 'gatal', 'kata adjektif', 'Bidayuh', 'Tangan gatai jak.', '2025-04-30T09:41:26.538461');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyau', 'sudah', 'kata bantu', 'Iban', 'Kamek nyau makan.', '2025-04-30T09:41:26.538464');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyamai', 'sedap', 'kata adjektif', 'Iban', 'Makanan tok nyamai gilak.', '2025-04-30T09:41:26.538467');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bani', 'tidak mahu', 'kata kerja', 'Bidayuh', 'Dia bani makan.', '2025-04-30T09:41:26.538470');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('andak', 'nanti', 'kata keterangan', 'Melanau', 'Andak dulu baru jalan.', '2025-04-30T09:41:26.538473');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kamek', 'saya', 'kata ganti nama', 'Iban', 'Kamek suka makan.', '2025-04-30T09:41:26.538476');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('mun', 'kalau', 'kata hubung', 'Iban', 'Mun kitak datang awal.', '2025-04-30T09:41:26.538479');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyamai', 'sedap', 'kata adjektif', 'Iban', 'Makanan tok nyamai gilak.', '2025-04-30T09:41:26.538482');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyau', 'sudah', 'kata bantu', 'Iban', 'Kamek nyau makan.', '2025-04-30T09:41:26.538485');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('nyamai', 'sedap', 'kata adjektif', 'Iban', 'Makanan tok nyamai gilak.', '2025-04-30T09:41:26.538488');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('gatai', 'gatal', 'kata adjektif', 'Bidayuh', 'Tangan gatai jak.', '2025-04-30T09:41:26.538491');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kamek', 'saya', 'kata ganti nama', 'Iban', 'Kamek suka makan.', '2025-04-30T09:41:26.538494');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kamek', 'saya', 'kata ganti nama', 'Iban', 'Kamek suka makan.', '2025-04-30T09:41:26.538498');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('mun', 'kalau', 'kata hubung', 'Iban', 'Mun kitak datang awal.', '2025-04-30T09:41:26.538501');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('mun', 'kalau', 'kata hubung', 'Iban', 'Mun kitak datang awal.', '2025-04-30T09:41:26.538504');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('kamek', 'saya', 'kata ganti nama', 'Iban', 'Kamek suka makan.', '2025-04-30T09:41:26.538507');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bebalin', 'bodoh', 'kata adjektif', 'Melanau', 'Jangan bebaling sangat.', '2025-04-30T09:41:26.538510');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('bani', 'tidak mahu', 'kata kerja', 'Bidayuh', 'Dia bani makan.', '2025-04-30T09:41:26.538514');
INSERT INTO words (word, definition, word_type, dialect, example_sentence, created_at)
VALUES ('mun', 'kalau', 'kata hubung', 'Iban', 'Mun kitak datang awal.', '2025-04-30T09:41:26.538517');
