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

class DevicesDatabase(Model): 
    class Meta: 
        database = db

class Device (DevicesDatabase):
    id = AutoField(unique = True)
    name = TextField()
    model = TextField()
    house = AutoField()

class DeviceType (DevicesDatabase):
    id = AutoField(unique = True)
    name = TextField()
    model = TextField()
    house = AutoField()

class 
