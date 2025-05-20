CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT NOT NULL,
    definition TEXT NOT NULL,
    dialect TEXT,
    approved INTEGER
);

INSERT INTO words (word, definition, dialect, approved) VALUES 
('nyamai', 'sedap', 'Iban', 1),
('kamek', 'saya', 'Sarawak Malay', 1),
('kitak', 'awak', 'Sarawak Malay', 1);
('pandei', 'pandai / bijak', 'Sarawak Malay', 1),
('ngiga', 'mencari', 'Iban', 1),
('gerek', 'best / seronok', 'Sarawak Malay', 1),
('bisi', 'ada', 'Iban', 1),
('malasik', 'comel / manja', 'Bidayuh', 1),
('bujang', 'lelaki muda / belum kahwin', 'Sarawak Malay', 1),
('entauk', 'bagi / untuk', 'Iban', 1),
('kelala', 'lupa', 'Bidayuh', 1),
('mari', 'marah', 'Sarawak Malay'),
('maok', 'mahu / hendak', 'Sarawak Malay', 1);
('menoa', 'kampung halaman / tempat asal', 'Iban', 1),
('nyin', 'tidur', 'Bidayuh', 1),
('ngasu', 'memburu', 'Iban', 1),
('tedong', 'ular', 'Sarawak Malay', 1,
('bagak', 'hebat / besar / bergaya', 'Sarawak Malay', 1),
('mensia', 'orang / manusia', 'Sarawak Malay', 1),
('entaban', 'naik / naik ke atas', 'Iban', 1),
('bekelit', 'berbohong / tipu', 'Sarawak Malay', 1),
('berimbai', 'berkibar (macam bendera)', 'Bidayuh', 1),
('kuduk', 'gatal-gatal / ruam', 'Sarawak Malay', 1);
