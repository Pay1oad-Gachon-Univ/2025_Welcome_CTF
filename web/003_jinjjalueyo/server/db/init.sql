CREATE DATABASE IF NOT EXISTS ctfdb;
USE ctfdb;

CREATE TABLE suggestions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    content TEXT,
    viewed TINYINT DEFAULT 0
);
