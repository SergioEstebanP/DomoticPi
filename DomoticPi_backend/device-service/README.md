To create the container with the service:
```
docker build -t device-service .
```

To tune the containter:
```
docker run -p 3000:3000 --name device-service -d device-service
```