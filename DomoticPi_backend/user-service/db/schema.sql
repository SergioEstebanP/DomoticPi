CREATE DATABASE userDB;
USE userDB;

CREATE TABLE user_type (
    id INT NOT NULL,
    user_value VARCHAR(50),
    CONSTRAINT user_type_pk PRIMARY KEY (id)
);

CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    surname_1 VARCHAR(50),
    surname_2 VARCHAR(50),
    nick VARCHAR(25),
    type INTEGER,
    CONSTRAINT user_pk PRIMARY KEY (id)
);

INSERT INTO user_type (id, user_value) values (0, "client");
INSERT INTO user_type (id, user_value) values (1, "manager");

INSERT INTO user (name, surname_1, surname_2, nick, type) values ("Sergio", "Esteban", "Pellejero", "SergioEstebanP", 1);
INSERT INTO user (name, surname_1, surname_2, nick, type) values ("Antonio", "Esteban", "Arguedas", "AntonioEstebanA", 0);
INSERT INTO user (name, surname_1, surname_2, nick, type) values ("Miriam", "Esteban", "Pellejero", "MiriamEstebanA", 0);

CREATE USER 'user-service'@'%' IDENTIFIED WITH mysql_native_password BY 'user-service';
GRANT ALL PRIVILEGES ON *.* TO 'user-service'@'%';
FLUSH PRIVILEGES;