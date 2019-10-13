import mysql.connector
from flask import Flask, jsonify, abort, request
from mysql.connector import Error

app = Flask(__name__)

def get_devices():
    try:
        connection = mysql.connector.connect(
            host='device-service-db', 
            database='devicesDB', 
            user='device-service', 
            password='device-service'
        )
        if connection.is_connected():
            sql_query = "select * from device"
            cursor = connection.cursor()
            cursor.execute(sql_query)
            result = cursor.fetchall()
            connection.close()
            return result
    except Error as error:
        print(error)

@app.route('/devices', methods=['GET', 'POST'])
def index():
    if (request.method == 'GET'):
        print("hola")
        query_result = get_devices()
        return jsonify(query_result)
    elif (request.method == 'POST'):
        return ("201 Created")
    else:
        abort(405, "Method not allowed not allowed")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')