CREATE TABLE users (
id SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
    age INTEGER NOT NULL CHECK (age >= 0),
position VARCHAR(100) NOT NULL
);