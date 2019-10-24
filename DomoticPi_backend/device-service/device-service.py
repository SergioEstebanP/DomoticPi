import mysql.connector
from flask import Flask, jsonify, abort, request
from mysql.connector import Error
from peewee import *

app = Flask(__name__)
db = MySQLDatabase('dataService', user='database-service', password='database-service', host='database-service')

def get_devices():

@app.route('/devices', methods=['GET', 'POST'])
def index():
    if (request.method == 'GET'):
        query_result = get_devices()
        return jsonify(query_result)
    elif (request.method == 'POST'):
        return ("201 Created")
    else:
        abort(405, "Method not allowed not allowed")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

class Data_Service(Model): 
    class Meta: 
        database = db
        devices = 'device'
        devices_type = 'device_type'
        user = 'user'
        user_type = 'user_type'
        house = 'house'

class Device_Type (Data_Service):
    id = AutoField(unique = True)
    name = TextField()
    model = TextField()
    house = AutoField()

class Device (Data_Service):
    id = AutoField(unique = True)
    name = TextField()
    model = TextField()
    house = AutoField()

class User_Type (Data_Service):
    id = AutoField(unique = True)
    user_value = TextField()

class User (Data_Service):
    id = AutoField(unique = True)
    name = TextField()
    last_name_1 = TextField()
    last_name_2 = TextField()
    nick_name = TextField()

class House (Data_Service):
    id = AutoField(unique = True)
    city = TextField()
    address = TextField()
    owner = TextField()

