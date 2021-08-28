DROP DATABASE IF EXISTS capstone_1;

CREATE DATABASE capstone_1;

\c capstone_1

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    user_name TEXT NOT NULL,
    user_password TEXT NOT NULL,
    user_email TEXT NOT NULL
);

CREATE TABLE drinks (
    drink_id SERIAL PRIMARY KEY,
    drink_name TEXT NOT NULL
);

CREATE TABLE drink_name (
    drink_name_id SERIAL PRIMARY KEY,
    ingredient_id INT REFERENCES ingredients ON DELETE CASCADE
);

CREATE TABLE notes (
    note_id SERIAL PRIMARY KEY,
    notes TEXT NOT NULL
);

CREATE TABLE ingredients (
    ingredient_id SERIAL PRIMARY KEY,
    ingredient_name TEXT NOT NULL
);

CREATE TABLE favorites (
    favorite_id SERIAL PRIMARY KEY,
    drink_id INT REFERENCES drinks ON DELETE CASCADE,
    user_id INT REFERENCES users ON DELETE CASCADE,
    note_id INT REFERENCES notes ON DELETE CASCADE 
);