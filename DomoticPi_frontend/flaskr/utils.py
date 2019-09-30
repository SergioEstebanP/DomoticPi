import json
import requests

def get_devices():
    names = []
    response = requests.get("http://localhost:5000/devices")
    jsonBody = json.loads(response.content)
    print(jsonBody)
    return jsonBody