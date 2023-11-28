DROP TABLE IF EXISTS users;

CREATE TABLE users ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  password TEXT NOT NULL
);
CREATE TABLE sqlite_sequence(name,seq);
