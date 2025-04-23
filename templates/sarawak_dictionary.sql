CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT NOT NULL,
    definition TEXT NOT NULL,
    dialect TEXT
);

INSERT INTO words (word, definition, dialect) VALUES 
('nyamai', 'sedap', 'Iban'),
('kamek', 'saya', 'Sarawak Malay'),
('kitak', 'awak', 'Sarawak Malay');
('pandei', 'pandai / bijak', 'Sarawak Malay'),
('ngiga', 'mencari', 'Iban'),
('gerek', 'best / seronok', 'Sarawak Malay'),
('bisi', 'ada', 'Iban'),
('malasik', 'comel / manja', 'Bidayuh'),
('bujang', 'lelaki muda / belum kahwin', 'Sarawak Malay'),
('entauk', 'bagi / untuk', 'Iban'),
('kelala', 'lupa', 'Bidayuh'),
('mari', 'marah', 'Sarawak Malay'),
('maok', 'mahu / hendak', 'Sarawak Malay');
('menoa', 'kampung halaman / tempat asal', 'Iban'),
('nyin', 'tidur', 'Bidayuh'),
('ngasu', 'memburu', 'Iban'),
('tedong', 'ular', 'Sarawak Malay'),
('bagak', 'hebat / besar / bergaya', 'Sarawak Malay'),
('mensia', 'orang / manusia', 'Sarawak Malay'),
('entaban', 'naik / naik ke atas', 'Iban'),
('bekelit', 'berbohong / tipu', 'Sarawak Malay'),
('berimbai', 'berkibar (macam bendera)', 'Bidayuh'),
('kuduk', 'gatal-gatal / ruam', 'Sarawak Malay');
