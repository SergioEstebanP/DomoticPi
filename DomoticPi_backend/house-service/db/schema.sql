CREATE DATABASE housesDB;
USE housesDB;

CREATE TABLE house (
    id INT NOT NULL AUTO_INCREMENT,
    city VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    owner VARCHAR(50),
    CONSTRAINT house_pk PRIMARY KEY (id)
);

INSERT INTO house (city, address, owner) values ("Valladolid", "Calle Manuel Azaña, 39", "Sergio Esteban");
INSERT INTO house (city, address, owner) values ("Zaragoza", "Andador Gutierrez Mellado, 11", "Antonio Esteban");

CREATE USER 'house-service'@'%' IDENTIFIED WITH mysql_native_password BY 'house-service';
GRANT ALL PRIVILEGES ON *.* TO 'house-service'@'%';
FLUSH PRIVILEGES;