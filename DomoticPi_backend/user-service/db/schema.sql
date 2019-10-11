CREATE DATABASE devicesDB;
USE devicesDB;

CREATE TABLE device (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    house VARCHAR(255),
    room VARCHAR(255),
    type VARCHAR(255),
    CONSTRAINT device_pk PRIMARY KEY (id)
);

INSERT INTO device (name, house, room, type) values ("General lights", "Valladolid", "Room 1", "LIGHT");
INSERT INTO device (name, house, room, type) values ("Motion sensor", "Valladolid", "Hall", "SENSOR");

CREATE USER 'device-service'@'%' IDENTIFIED WITH mysql_native_password BY 'device-service';
GRANT ALL PRIVILEGES ON *.* TO 'device-service'@'%';
FLUSH PRIVILEGES;