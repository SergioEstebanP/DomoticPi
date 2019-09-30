To create the container with the database:
```
docker build -t device-service-db .
```

To tune the containter:
```
docker run -p 3306:3306 --name device-service-db -e MYSQL_ROOT_PASSWORD=device-service -d --net=services-nw device-service-db
```