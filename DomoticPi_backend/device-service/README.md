To create the container with the service:
```
docker build -t device-service .
```

To tune the containter:
```
docker run -p 5000:5000 --name device-service device-service
```