# mysql_connection.py

import mysql.connector

def get_mysql_connection():
    config = {
        "host": "mysql_host",
        "user": "read_only_user",
        "password": "read_only_password",
        "database": "openedx"
    }
    return mysql.connector.connect(**config)