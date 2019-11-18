import mysql.connector
from mysql.connector import Error

def sql_query(query):
    try:
        connection  = mysql.connector.connect(
            host='172.17.0.2', 
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
