-- CREATE DATABASE IF NOT EXISTS auth_db;

-- CREATE USER 'egs'@'localhost' IDENTIFIED BY 'egs';

-- GRANT INSERT, UPDATE, SELECT on auth_db.* TO 'egs'@'localhost' 

USE auth_db;

CREATE TABLE users (
    username VARCHAR(50) PRIMARY KEY,
    email VARCHAR(60) UNIQUE NOT NULL,
    password VARCHAR(150) NOT NULL
);