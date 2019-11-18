from flask import Flask, render_template, redirect, url_for, request, abort

import requests
import json
import os

app = Flask(__name__)

DEVICES_URL = 'http://device-service:5000/devices'
DEVICES_TYPES_URL = 'http://device-service:5000/devices/types'

GET = 'GET'
POST = 'POST'

# DEVICES 
def get_devices():
    response = requests.get(DEVICES_URL)
    return json.loads(response.content)

def get_devices_type():
    response = requests.get(DEVICES_TYPES_URL)
    return json.loads(response.content)

def create_new_device(device_name, device_type, device_city, device_model):
    query_parameters = {'device_name': device_name, 'device_type': device_type, 'device_city': device_city, 'device_model': device_model}
    response = requests.post(DEVICES_URL, params = query_parameters)
    # print(response.json(), flush=True)
    return json.loads(response.content)

@app.route('/devices', methods = [GET, POST])
def devices():
    if (request.method == GET):
        data_devices = get_devices()
        data_houses = get_houses()
        data_devices_type = get_devices_type()
        return render_template('devices_view.html', data_devices=data_devices, data_houses=data_houses, data_devices_type=data_devices_type)
    elif (request.method == POST):
        device_name = request.form.get("device_name")
        device_type = request.form.get("device_type")
        device_city = request.form.get("device_city")
        device_model = request.form.get("device_model")
        create_new_device(device_name, device_type, device_city, device_model)
        return redirect(url_for("devices")) 
    else:
        abort(405, "Method Not Allowed")
    

# HOUSES 
def get_houses():
    response = requests.get('http://house-service:5000/houses')
    return json.loads(response.content)

@app.route('/houses')
def houses():
    data_houses = get_houses()
    return render_template('houses_view.html', data_houses=data_houses)

# USERS 
def get_users():
    response = requests.get('http://user-service:5000/users')
    return json.loads(response.content)

@app.route('/users')
def users():
    data_users = get_users()
    return render_template('users_view.html', data_users=data_users)

# MAIN APPLICATION RUNNER
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3001')
