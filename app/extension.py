import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Ankul@123',
            database='maurya'
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_write_query(query):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        print('query', query)
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
        return
    except Error as e:
        print(f"The error '{e}' occurred")
        
        
def execute_read_query(query):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        print('query', query)
        cursor.execute(query)
        result = cursor.fetchall()
        print("Query executed successfully")
        return result
    except Error as e:
        print(f"The error '{e}' occurred")        
        
        
