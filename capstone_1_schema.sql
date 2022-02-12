DROP DATABASE IF EXISTS capstone_1;

CREATE DATABASE capstone_1;

\c capstone_1

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    user_password TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE drinks (
    drink_id SERIAL PRIMARY KEY,
    drink_ingredients_id INT   NOT NULL,
    drink_image TEXT,
    drink_instructions TEXT

);

CREATE TABLE drink_ingridients (
    drink_ingredient_id SERIAL PRIMARY KEY,
    drink_ingredient_1 TEXT,
    drink_ingredient_2 TEXT,
    drink_ingredient_3 TEXT,
    drink_ingredient_4 TEXT,
    drink_ingredient_5 TEXT,
    quantity_of_ingredient_1 FLOAT,
    quantity_of_ingredient_2 FLOAT,
    quantity_of_ingredient_3 FLOAT,
    quantity_of_ingredient_4 FLOAT,
    quantity_of_ingredient_5 FLOAT,
    measurement_type_ingredient_1 TEXT,
    measurement_type_ingredient_2 TEXT,
    measurement_type_ingredient_3 TEXT,
    measurement_type_ingredient_4 TEXT,
    measurement_type_ingredient_5 TEXT
    
);


CREATE TABLE favorites (
    favorite_id SERIAL PRIMARY KEY,
    drink_id INT REFERENCES drinks ON DELETE CASCADE,
    user_id INT REFERENCES users ON DELETE CASCADE,
    comment TEXT,
    created_at TIMESTAMP   NOT NULL
);

