To create the container with the service:
```
docker build -t device-service .
```

To tune the containter:
```
docker run -p -d 5000:5000 --name device-service --net=devices-nw device-service
```