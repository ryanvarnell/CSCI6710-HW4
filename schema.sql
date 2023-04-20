CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT,
    image TEXT,
    bio TEXT
);

CREATE TABLE item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    name TEXT,
    link TEXT,
    image TEXT NOT NULL
)

CREATE TABLE style (
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    description TEXT,
    head TEXT,
    shirt TEXT,
    overshirt TEXT,
    jacket TEXT,
    pants TEXT,
    shoes TEXT,
    socks TEXT,
    FOREIGN KEY (creator_id) REFERENCES user (id)
)
