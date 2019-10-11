import mysql.connector
from flask import Flask, jsonify, abort
from mysql.connector import Error

app = Flask(__name__)

@app.route('/devices', methods=['GET', 'POST'])
def index():
    try:
        connection = mysql.connector.connect(
                host='device-service-db',
                database='devicesDB',
                user='device-service',
                password='device-service')
        if connection.is_connected():
            if (flask.request.method == 'GET'):
                sql_query = "select * from device"
                cursor = connection.cursor()
                cursor.execute(sql_query)
                result = cursor.fetchall()
                return jsonify(result)
            elif (flask.request.method == 'POST'):
                sql_query = "select * from device"
            else:
                abort(405, "Method not allowed not allowed")

    except Error as e:
        print(e)
    finally:
        if (connection.is_connected()):
            connection.close()
            print("Mysql Connection CLosed")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')