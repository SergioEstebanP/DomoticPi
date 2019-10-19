from flask import Flask, render_template, request, json

import os

app = Flask(__name__)

devices_url = 'http://localhost:6001/devices'
houses_url = 'http://localhost:6002/houses'
users_url = 'http://localhost:6003/users'

def get_devices():
    response = request.get(devices_url)
    return json.loads(response.content)

def get_houses():
    response = request.get(houses_url)
    return json.loads(response.content)

def get_users():
    response = request.get(users_url)
    return json.loads(response.content)

@app.route('/devices')
def devices():
    data_devices = get_devices()
    return render_template('devices_view.html', data_devices=data_devices)

@app.route('/houses')
def houses():
    data_houses = get_houses()
    return render_template('houses_view.html', data_houses=data_houses)

@app.route('/users')
def users():
    data_users = get_users()
    return render_template('users_view.html', data_users=data_users)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3001')