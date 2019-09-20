CREATE DATABASE devicesDB;
USE devicesDB;

CREATE TABLE device (
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    house VARCHAR(255),
    room VARCHAR(255),
    type VARCHAR(255)
);

INSERT INTO TABLE (device) values ("General lights", "Valladolid", "Room 1", "LIGHT");
INSERT INTO TABLE (device) values ("Motion sensor", "Valladolid", "Hall", "SENSOR");

CREATE USER 'deviceservice'@'localhost' IDENTIFIED WITH mysql_native_password BY 'deviceservice';
GRANT ALL PRIVILEGES ON *.* TO 'deviceservice'@'localhost';
FLUSH PRIVILEGES;