## Simple mciroservice to get pets

### 1. Requirements

To run this microservice you only need to have [Docker|https://www.docker.com/] installed in your machine. To deploy the microservice you have to run the following commands:

### 2. Deployment
```
git clone https://github.com/SergioEstebanP/dummy-rest-api.git
cd dummy-rest-api
docker build dummy-rest-api .
docker run -p 3000:3000 --name dummy-rest-api dummy-rest-api
```

To see if the microservice is running fine you have to type in google the following URL [http://localhost:3000/dogs|http://localhost:3000/dogs]. And the output should be a JSON like this:
```
[
    {
        "group_0": {
            "name": "pipo",
            "age": 4
        }
    },
    {
        "group_1": {
            "name": "tobi",
            "age": 5
        }
    }
]
```

### 3. Description

This is just a simple server developed in nodeJS using the express framework. The only HTTP method allowed is GET opeation against /dogs endpoint. And the output is the commented above. 