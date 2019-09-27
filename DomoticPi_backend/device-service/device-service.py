import mysql.connector
from flask import Flask, jsonify
from mysql.connector import Error

app = Flask(__name__)

@app.route('/devices')
def index():
    try:
        connection = mysql.connector.connect(
                host='172.17.0.2'
                database='devicesDB',
                user='device-service',
                password='device-service')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            sql_query = "select * from device"
            cursor = connection.cursor()
            cursor.execute(sql_query)
            result = cursor.fetchall()
            print(result)
            return jsonify(result)

    except Error as e:
        print(e)
    finally:
        if (connection.is_connected()):
            connection.close()
            print("Mysql Connection CLosed")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')