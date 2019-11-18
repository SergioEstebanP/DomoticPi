import mysql.connector
from flask import Flask, jsonify, abort, request
from mysql.connector import Error

app = Flask(__name__)
app.config.from_object('config')

GET = 'GET'
POST = 'POST'

LOCALHOST = '0.0.0.0'

def get_users():
    try:
        connection = mysql.connector.connect(
            host='database-service', 
            database='dataService', 
            user='database-service', 
            password='database-service'
        )
        print("connected to DB")
        if connection.is_connected():
            sql_query = "select * from user"
            cursor = connection.cursor()
            cursor.execute(sql_query)
            result = cursor.fetchall()
            connection.close()
            print(result)
            return result
    except Error as error:
        print(error)

@app.route('/users', methods=[GET, POST])
def index():
    if (request.method == GET):
        print("enter in GET users")
        query_result = get_users()
        print("after execute sql query")
        return jsonify(query_result)
    elif (request.method == POST):
        return ("201 Created")
    else:
        abort(405, "Method not allowed not allowed")

if __name__ == '__main__':
    app.run(debug=True, host=LOCALHOST, port=app.config["PORT"])
