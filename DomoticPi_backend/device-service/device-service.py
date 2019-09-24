import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
            host='172.17.0.2',
            database='devicesDB',
            user='device-service',
            password='device-service')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        sql_query = "select * from device"
        cursor = connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        print("{}".format(result))

except Error as e:
    print(e)
finally:
    if (connection.is_connected()):
        connection.close()
        print("Mysql Connection CLosed")