CREATE TABLE IF NOT EXISTS 'pets' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS 'people' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    pet_id INTEGER NOT NULL,
    FOREIGN KEY (pet_id) REFERENCES pets(id)
);

INSERT into pets (name, type) 
VALUES 
('Fido', 'dog'),
('Whiskers', 'cat'),
('Tweety', 'bird'),
('Nemo', 'fish'),
('Buddy', 'dog'),   
('Mittens', 'cat'),
('Goldie', 'fish'),
('Shadow', 'dog'),
('Luna', 'cat'),
('Coco', 'bird');