import json
import requests

def get_dog_names():
    names = []
    response = requests.get("http://localhost:3000/dogs")
    jsonBody = json.loads(response.content)
    for group in jsonBody:
        for key in group:
            names.append(group[key]['name'])
    return names