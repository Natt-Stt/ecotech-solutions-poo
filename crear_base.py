import sqlite3

conexion = sqlite3.connect("ecotech.db")
cursor = conexion.cursor()


conexion.commit()
conexion.close()