To create the container with the database:
```
docker build -t device-service-db .
```

To tune the containter:
```
docker run -p 33060:3306 --name device-service-db -e MYSQL_ROOT_PASSWORD=device-service -d device-service-db
```