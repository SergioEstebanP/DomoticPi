CREATE DATABASE dataService;
USE dataService;

CREATE TABLE house (
    id INT NOT NULL,
    city VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    owner VARCHAR(255) NOT NULL,
    CONSTRAINT house_pk PRIMARY KEY (id)
);

CREATE TABLE user_type (
    id INT NOT NULL,
    user_value VARCHAR(50),
    CONSTRAINT user_type_pk PRIMARY KEY (id)
);

CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    lastName1 VARCHAR(255) NOT NULL,
    lastName2 VARCHAR(255) NOT NULL,
    type INT NOT NULL,
    house INT NOT NULL, 
    CONSTRAINT user_pk PRIMARY KEY (id),
    CONSTRAINT user_type_fk FOREIGN KEY (type) REFERENCES user_type(id),
    CONSTRAINT user_house_fk FOREIGN KEY (house) REFERENCES house(id)
);

CREATE TABLE device_type (
    id INT NOT NULL,
    device_value VARCHAR(50),
    CONSTRAINT device_type_pk PRIMARY KEY (id)
);

CREATE TABLE device (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    type INT NOT NULL,
    model VARCHAR(255),
    house INT NOT NULL, 
    CONSTRAINT device_pk PRIMARY KEY (id),
    CONSTRAINT device_type_fk FOREIGN KEY (type) REFERENCES device_type(id),
    CONSTRAINT device_house_fk FOREIGN KEY (house) REFERENCES house(id)
);

INSERT INTO house (id, city, address, owner) values (0, "Valladolid", "Calle Manuel Azaña, 39", "Antonio Esteban");           
INSERT INTO house (id, city, address, owner) values (1, "Zaragoza", "Andador Gutierrez Mellado, 11", "Isabel Pellejero");    
INSERT INTO house (id, city, address, owner) values (2, "Madrid", "Calle de los Olmos, 3", "Sergio Esteban");               
INSERT INTO house (id, city, address, owner) values (3, "Ibdes", "Calle del Barranco", "Maria Luisa");               

INSERT INTO user_type (id, user_value) values (0, "Administrador");          
INSERT INTO user_type (id, user_value) values (1, "Usuario sin permisos");   
INSERT INTO user_type (id, user_value) values (2, "Usuario con permisos");   

INSERT INTO user (name, lastName1, lastName2, type, house) values ("Sergio", "Esteban", "Pellejero", 0, 0); 
INSERT INTO user (name, lastName1, lastName2, type, house) values ("Miriam", "Esteban", "Pellejero", 1, 1); 
INSERT INTO user (name, lastName1, lastName2, type, house) values ("Isabel", "Pellejero", "Gonzalez", 1, 1);
INSERT INTO user (name, lastName1, lastName2, type, house) values ("Antonio", "Esteban", "Arguedas", 2, 2); 

INSERT INTO device_type (id, device_value) values (0, "LIGTHS_CONTROL");
INSERT INTO device_type (id, device_value) values (1, "MOTION");
INSERT INTO device_type (id, device_value) values (2, "TEMPERATURE");
INSERT INTO device_type (id, device_value) values (3, "HUMIDITY");
INSERT INTO device_type (id, device_value) values (4, "WIFI");
INSERT INTO device_type (id, device_value) values (5, "REALY");
INSERT INTO device_type (id, device_value) values (6, "OTHER");

INSERT INTO device (name, type, model, house) values ("Wifi lights control Sergio", 4, "Wifi reciver", 0);
INSERT INTO device (name, type, model, house) values ("Relay lights control Sergio", 5, "Realy reciver", 0);
INSERT INTO device (name, type, model, house) values ("Motion sensor control Sergio", 2, "Motion sensor reciver", 0);

CREATE USER 'database-service'@'%' IDENTIFIED WITH mysql_native_password BY 'database-service';
GRANT ALL PRIVILEGES ON *.* TO 'database-service'@'%';
FLUSH PRIVILEGES;