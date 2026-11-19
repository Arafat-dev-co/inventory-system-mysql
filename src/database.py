import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv() 

def get_connection():
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        ) 

        if conn.is_connected():
            return conn

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_table(conn):
    cursor = conn.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        quantity INT NOT NULL
    )
    """

    cursor.execute(query)
    conn.commit()
    print(f"Products table created successfully (or already exist)")


