#get_connections.py
from tkinter import Tk, Button,Label,Scrollbar,Listbox,StringVar,Entry,W,E,N,S,END
from tkinter import ttk
from tkinter import messagebox
from db_config import dbConfig
import mysql.connector as pyo
import psycopg2
import sqlite3
#from db_config import configDB
# Otros módulos de bases de datos que puedas necesitar

#con = pyo.connect(**dbConfig)
#print(con)

#cursor = con.cursor()


class MultiDatabaseConnector:
    def __init__(self, db_type, **kwargs):

        self.db_type = db_type.lower()
        self.connection = None

        if self.db_type == 'mysql':
        	self.connection = pyo.connect(**kwargs)
        


    def execute_query(self, query, parameters=None):
    	if self.connection is None:
    		raise Exception("No se ha establecido una conexión a la base de datos.")

    	with self.connection.cursor() as cursor:
    		cursor.execute(query, parameters)
    		self.connection.commit()

    def fetch_data(self, query, parameters=None):
        if self.connection is None:
            raise Exception("No se ha establecido una conexión a la base de datos.")

        with self.connection.cursor() as cursor:
            cursor.execute(query, parameters)
            return cursor.fetchall()

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

# Ejemplo de uso
if __name__ == '__main__':

    mysql_config = {
    	'user': 'root',
    	'password': '',
    	'host': '127.0.0.1',
    	'database': 'tk_registros',
    	'port':3307
    	}



    mysql_connector = MultiDatabaseConnector('mysql', **mysql_config)


    try:
        #postgres_connector.execute_query("INSERT INTO users (name, age) VALUES (%s, %s)", ('Alice', 30))
        #sqlite_connector.execute_query("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 28))

        cat_tipos = mysql_connector.fetch_data("SELECT * FROM cattipo")

        print("Tipos in MySQL:", cat_tipos)

    finally:
        
        mysql_connector.close_connection()
