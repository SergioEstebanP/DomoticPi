## Useful Commands

Some useful commands to deploy the services:
- **Build Dockerfile**: `docker build -t device-service .`
- **Create docker local network**: `docker create network -d bridge network_name`
- **Run Service container**: `docker run -p -d 5000:5000 --name device-service --net=devices-nw device-service`
- **Run MySQL container**: `docker run -p 3306:3306 --name device-service-db -e MYSQL_ROOT_PASSWORD=device-service -d --net=services-nw device-service-db`
- **Start Services**: `docker-compose up`
- **Stop Services**: `docker-compose down`
- **Enter in running container**: `docker exec -it container_name bash`

---

## To do list: 
- Doc all the services
- Move db credentials to private file and add it to .gitignore
- Move credentials, directions and ip to external file
- Add requirement file for pip 
- Select a better frontend framework
- See if MySQL connector for node is updated and support MySQL 8.0 version

---

## Useful information
 
Por forwarding for **services**:

| Service          | Port outside container  |  Port Forwarded |
| ---------------- |:-----------------------:|:---------------:|
| device-service   | 6001                    | 5000            |
| house-service    | 6002                    | 5000            |
| user-service     | 6003                    | 5000            |

Port forwarding for services **databases**:

| Service            | Port outside container  |  Port Forwarded |
| ------------------ |:-----------------------:|:---------------:|
| device-service-db  | 7001                    | 3306            |
| house-service-db   | 7002                    | 3306            |
| user-service-db    | 7003                    | 3306            |