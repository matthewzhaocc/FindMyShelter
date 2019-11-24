
CREATE DATABASE login;
USE login;
CREATE TABLE loginDatabase(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    usertype VARCHAR(255) NOT NULL,
    shelter VARCHAR(255) NOT NULL
)
CREATE TABLE companyUserDatabase(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    usertype VARCHAR(255) NOT NULL,
    details VARCHAR(255) NOT NULL
);

CREATE DATABASE shelter;
USE shelter;
CREATE TABLE shelterLocations(
    id INT AUTO_INCREMENT PRIMARY KEY,
    Organization VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    Capacity INT NOT NULL,
    open BOOLEAN NOT NULL
);