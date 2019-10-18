import json
import requests

devices_url = 'http://localhost:6001/devices'
houses_url = 'http://localhost:6002/houses'

def get_devices():
    response = requests.get(devices_url)
    return json.loads(response.content)

def get_houses():
    response = requests.get(houses_url)
    return json.loads(response.content)