CREATE DATABASE devicesDB;
USE devicesDB;

CREATE TABLE device_type (
    id INT NOT NULL,
    device_value VARCHAR(50),
    CONSTRAINT device_type_pk PRIMARY KEY (id)
);

CREATE TABLE device (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL,
    model VARCHAR(255),
    CONSTRAINT device_pk PRIMARY KEY (id),
    CONSTRAINT device_type_fk FOREIGN KEY (type) REFERENCES device_type(id)
);

INSERT INTO device_type (id, device_value) values (0, "LIGTHS_CONTROL");
INSERT INTO device_type (id, device_value) values (1, "MOTION");
INSERT INTO device_type (id, device_value) values (2, "TEMPERATURE");
INSERT INTO device_type (id, device_value) values (3, "HUMIDITY");
INSERT INTO device_type (id, device_value) values (4, "WIFI");
INSERT INTO device_type (id, device_value) values (5, "REALY");
INSERT INTO device_type (id, device_value) values (6, "OTHER");

INSERT INTO device (name, type, model) values ("Wifi lights control Sergio", 4, "Wifi reciver");
INSERT INTO device (name, type, model) values ("Relay lights control Sergio", 5, "Realy reciver");
INSERT INTO device (name, type, model) values ("Motion sensor control Sergio", 2, "Motion sensor reciver");

CREATE USER 'device-service'@'%' IDENTIFIED WITH mysql_native_password BY 'device-service';
GRANT ALL PRIVILEGES ON *.* TO 'device-service'@'%';
FLUSH PRIVILEGES;