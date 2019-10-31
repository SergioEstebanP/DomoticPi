import mysql.connector
from flask import Flask, jsonify, abort, request, redirect, url_for
from mysql.connector import Error
# from peewee import *

app = Flask(__name__)
# db = MySQLDatabase('dataService', user='database-service', password='database-service', host='database-service')

def sql_query(query):
    try:
        connection  = mysql.connector.connect(
            host='database-service', 
            database='dataService', 
            user='database-service', 
            password='database-service'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            connection.close()
            return result
    except Error as error:
        print(error)

def from_type_to_number(type):
    if (type == "LIGHTS_CONTROL"):
        return 0
    elif (type == "MOTION"):
        return 1
    elif (type == "TEMPERATURE"):
        return 2
    elif (type == "HUMIDITY"):
        return 3
    elif (type == "WIFI"):
        return 4
    elif (type == "RELAY"):
        return 5
    else:
        return 6

def create_new_device (name, type, city, model):
    type = from_type_to_number(type)
    return sql_query("insert into device (name, type, model, house) values({}, {}, {}, {})".format(name, type, model, city))

def get_devices():
    return sql_query("select * from device")
        
def get_devices_types():
    return sql_query("select * from device_type")

@app.route('/devices', methods=['GET', 'POST'])
def devices():
    if (request.method == 'GET'):
        query_result = get_devices()
        return jsonify(query_result)
    elif (request.method == 'POST'):
        name = request.args['device_name']
        type = request.args['device_type']
        city = request.args['device_city']
        model = request.args['device_model']
        create_new_device(name, type, city, model)
        print("{} {} {} {}".format(name, model, city, type), flush=True)
        return jsonify(name, type, city, model)
    else:
        abort(405, "Method not allowed not allowed")

@app.route('/devices/types', methods=['GET'])
def devices_types():
    if (request.method == 'GET'):
        query_result = get_devices_types()
        return jsonify(query_result)
    else:
        abort(405, "Method not allowed not allowed")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
