## Useful Commands

Some useful commands to deploy the services:
- **Build Dockerfile**: `docker build -t device-service .`
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