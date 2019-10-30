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
        return redirect(url_for("devices"))
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

# class Data_Service(Model): 
#     class Meta: 
#         database = db
#         devices = 'device'
#         devices_type = 'device_type'
#         user = 'user'
#         user_type = 'user_type'
#         house = 'house'

# class Device_Type (Data_Service):
#     id = AutoField(unique = True)
#     name = TextField()
#     model = TextField()
#     house = AutoField()

# class Device (Data_Service):
#     id = AutoField(unique = True)
#     name = TextField()
#     model = TextField()
#     house = AutoField()

# class User_Type (Data_Service):
#     id = AutoField(unique = True)
#     user_value = TextField()

# class User (Data_Service):
#     id = AutoField(unique = True)
#     name = TextField()
#     last_name_1 = TextField()
#     last_name_2 = TextField()
#     nick_name = TextField()

# class House (Data_Service):
#     id = AutoField(unique = True)
#     city = TextField()
#     address = TextField()
#     owner = TextField()

