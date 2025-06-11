DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS words;

CREATE TABLE IF NOT EXISTS users (
   id INTEGER PRIMARY KEY, 
   username TEXT, 
   password TEXT,
   admin INTEGER NOT NULL
);

CREATE TABLE words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT NOT NULL UNIQUE,
    definition TEXT NOT NULL,
    dialect TEXT NOT NULL,
    approved INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    word_id INTEGER NOT NULL,
    FOREIGN KEY (id) REFERENCES words(id)
);

INSERT INTO users (username, password, admin) VALUES 
('boss', 'boss', 1),
('user', 'user', 0);

INSERT INTO words (word, definition, dialect, approved) VALUES 
('aruk', 'nasi goreng', 'Melanau', 1),
('bagak', 'hebat / besar / bergaya', 'Sarawak Malay', 1),
('bedau', 'belum', 'Melanau', 1),
('bek', 'jangan', 'Iban', 1),
('bekelit', 'berbohong / tipu', 'Sarawak Malay', 1),
('belama', 'lama / berlama-lama', 'Melanau', 1),
('berimbai', 'berkibar (macam bendera)', 'Bidayuh', 1),
('bisi', 'ada', 'Iban', 1),
('bujang', 'lelaki muda / belum kahwin', 'Sarawak Malay', 1),
('bujur', 'betul', 'Iban', 1),
('entaban', 'naik / naik ke atas', 'Iban', 1),
('entauk', 'bagi / untuk', 'Iban', 1),
('gerek', 'best / seronok', 'Sarawak Malay', 1),
('jan', 'jangan', 'Melanau', 1),
('kacak', 'cakap', 'Melanau', 1),
('kamek', 'saya', 'Sarawak Malay', 1),
('kelala', 'lupa', 'Bidayuh', 1),
('kitak', 'awak', 'Sarawak Malay', 1),
('kuduk', 'gatal-gatal / ruam', 'Sarawak Malay', 1),
('kupi', 'kopi', 'Iban', 1),
('madah', 'beritahu', 'Melanau', 1),
('malasik', 'comel / manja', 'Bidayuh', 1),
('maok', 'mahu / hendak', 'Sarawak Malay', 1),
('makan', 'makan', 'Bidayuh', 1),
('mari', 'marah', 'Sarawak Malay', 1),
('mensia', 'orang / manusia', 'Sarawak Malay', 1),
('minum', 'minum', 'Bidayuh', 1),
('mun', 'kalau', 'Iban', 1),
('nadai', 'tiada', 'Bidayuh', 1),
('ngan', 'dengan', 'Bidayuh', 1),
('ngansam', 'simpan', 'Melanau', 1),
('ngantos', 'tunggu / menunggu', 'Bidayuh', 1),
('ngasu', 'memburu', 'Iban', 1),
('ngeri', 'menakutkan', 'Sarawak Malay', 1),
('ngiga', 'mencari', 'Iban', 1),
('ngilu', 'sakit bila gigit', 'Bidayuh', 1),
('nyamai', 'sedap / enak', 'Bidayuh', 1),
('nyepit', 'cubit', 'Iban', 1),
('nyin', 'tidur', 'Bidayuh', 1),
('pandei', 'pandai / bijak', 'Sarawak Malay', 1),
('pauk', 'kena / dapat', 'Sarawak Malay', 1),
('sauk', 'ambil', 'Bidayuh', 1),
('sik', 'tidak', 'Sarawak Malay', 1),
('tambuk', 'baling', 'Melanau', 1),
('tegak', 'berdiri', 'Sarawak Malay', 1),
('tedong', 'ular', 'Sarawak Malay', 1),
('tangga', 'lihat / tengok', 'Bidayuh', 1),
('tinduk', 'tidur', 'Iban', 1),
('tok', 'ini', 'Iban', 1),
('tunggu', 'menunggu', 'Bidayuh', 1),
('ya', 'itu', 'Sarawak Malay', 1);
