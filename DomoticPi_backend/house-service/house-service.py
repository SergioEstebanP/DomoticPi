import mysql.connector
from flask import Flask, jsonify, abort, request
from mysql.connector import Error

GET = 'GET'
POST = 'POST'

LOCALHOST = '0.0.0.0'

app = Flask(__name__)
app.config.from_object('config')

def get_houses():
    try:
        connection = mysql.connector.connect(
            # host='database-service'
            host='127.0.0.1', 
            database='dataService', 
            user='database-service', 
            password='database-service'
        )
        if connection.is_connected():
            sql_query = "select * from house"
            cursor = connection.cursor()
            cursor.execute(sql_query)
            result = cursor.fetchall()
            connection.close()
            return result
    except Error as error:
        print(error)

@app.route('/houses', methods=[GET, POST])
def index():
    if (request.method == GET):
        query_result = get_houses()
        return jsonify(query_result)
    elif (request.method == POST):
        return ("201 Created")
    else:
        abort(405, "Method not allowed not allowed")

if __name__ == '__main__':
    app.run(debug=True, host=LOCALHOST, port=app.config["PORT"])
