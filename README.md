# DomoticPi

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

In this repository you can find the whole project and infraestructure for DomoticPi. A private project to make your house domotic in a low cost way. The main idea is to have a raspi in every house as a central server. The raspi is managed from a remote server by the company. The raspi will be able to manage the ligths and other devices selected by the user. In this repository you'll find all the code in order to make this small project works. 

### Table of Contents
---

1. [DomoticPi](#domoticpi) 
2. [Table of Contents](#table-of-contents)
3. [Tools used in the project](#table-of-contents)
4. [Useful Commands](#useful-commands)
5. [Useful Information](#useful-information)
   1. [Services Port Forwarding](#services-port-forwarding)
   2. [Databases Port Forwarding](#databases-port-forwarding)
   3. [Services Architecture](#services-architecture)
   4. [Infrastructure Architecture](#infrastructure-architecture)
   5. [Entity Relation Diagram](#entity-relation-diagram)
6. [To do list](#to-do-list)

### Tools used in the project
---

Main tools used in the project are: 
- **Docker**: there is a full service infrastructure to orchestrate the environments. Each service is into a container, and each db service is also in its own container.
  - **Docker-compose**: the above infrastructure is easily orchestrated with docker-compose command. This way for the deploys made it available for windows or even linux platforms. The main idea is deploy the whole system in Linux based computers. 
  - **Docker hub**: above containers are based on 2 images, which can be found in docker-hub. 
- **Python**: main developing language is python. Backend and frontend are written in python. Original idea was use NodeJS for the backend and Python with a simple flask application for the frontend. But MySQL was updated to 8.X version and MySQL connectr for node wasn't updated and there was several incompatibilities. In some far future, backend services could be in NodeJS. 
  - **Flask**: flask application as a simple way to server HTTP pages and create REST API servers. In a few lines you can deploy webpages and connect services to the databases. 
- **MySQL**: relational database to serve the information. use MongoDB as a future enhacement becase the data allow it and it's a simpleway to mangae updates in schema and data management. 
- **Github**: github as a simple SCV and project management software. 
- **VSCode**: VSCode as a simple editor. 
- **Jenkins**: future improvement for CI/CD automation. Still not implemented. 


### Useful Commands
---

Some useful commands to deploy the services:
- **Build Dockerfile**: `docker build -t device-service .`
- **Create docker local network**: `docker create network -d bridge network_name`
- **Run Service container**: `docker run -p -d 5000:5000 --name device-service --net=devices-nw device-service`
- **Run MySQL container**: `docker run -p 3306:3306 --name device-service-db -e MYSQL_ROOT_PASSWORD=device-service -d --net=services-nw device-service-db`
- **Start Services**: `docker-compose up`
- **Stop Services**: `docker-compose down`
- **Start services container**: `docker run -it sergioestebanp/domoticpi:services-1.0`
- **Enter in running container**: `docker exec -it container_name bash`
- **Install python packages in containers**: `pip3 install packageName`
- **Create container image from existing**: `docker commit sha256 sergioestebanp/domoticpi:tagName`
- **Upload image container to docker-hub**: `docker push sergioestebanp/domoticpi:tagNameContainer`

### Useful information
---

#### Services Port forwarding

| Service          | Port outside container  |  Port Forwarded |
| ---------------- |:-----------------------:|:---------------:|
| device-service   | 6001                    | 5000            |
| house-service    | 6002                    | 5000            |
| user-service     | 6003                    | 5000            |

#### Databases Port forwarding

| Service            | Port outside container  |  Port Forwarded |
| ------------------ |:-----------------------:|:---------------:|
| database-service   | 7000                    | 3306            |

#### Services Architecture
There are two approaches to achieve the infrastructure we want here:
1. Using a pure microservices architecture. With one services accesing its own db. And communicating them with an event handler and with an intermediate layer to have the proper consistency in the database. Using this architecture we avoid the issue with lots of hits using the databse and keeping consistency depends on external middleware. We can see this architecture and solution in the following image: 
![alt Services_architecture_middleware](documentation/components_diagra_services_consistency_layer.png)

2. Other solution, more classic: use only one database for all services and all the services accessing to it. We decide to use this architecture due to the lack of high hits to the API and also to the Database. This database is supossed to be designed only once and modifications are rare. only if customer wants to add new devices. We can see the architecture mentioned abode in the following picture:
![alt Services_architecture_classical](documentation/components_diagra_services_one_db.png)

#### Infrastructure Architecture
![alt Infrastructure_diagram](documentation/components_diagram.png)

#### Entity Relation Diagram
Depending on the solution we choose as main infrasctructure, we are going to have a different set up for the databases. The models are the following:
1. Solution with middleware: 
![alt er_diagram](documentation/er_diagram.png)

2. Solution without:
![alt er_diagram](documentation/er_diagram_modified.png)

### To do list: 
---
- Doc all the services
- Move db credentials to private file and add it to .gitignore
- Move credentials, directions and ip to external file
- Add requirement file for pip 
- Select a better frontend framework
- See if MySQL connector for node is updated and support MySQL 8.0 version
