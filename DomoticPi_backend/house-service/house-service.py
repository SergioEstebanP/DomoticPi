import mysql.connector
from flask import Flask, jsonify, abort, request
from mysql.connector import Error

app = Flask(__name__)

@app.route('/houses', methods=['GET', 'POST'])
def index():
    try:
        connection = mysql.connector.connect(
                host='house-service-db',
                database='housesDB',
                user='house-service',
                password='device-service')
        if connection.is_connected():
            if (request.method == 'GET'):
                sql_query = "select * from house"
                cursor = connection.cursor()
                cursor.execute(sql_query)
                result = cursor.fetchall()
                return jsonify(result)
            elif (request.method == 'POST'):
                sql_query = "select * from house"
                return "operation success"
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