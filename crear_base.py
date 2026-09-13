import sqlite3

conexion = sqlite3.connect("ecotech.db")

# Activa claves foráneas
conexion.execute("PRAGMA foreign_keys = ON")

cursor = conexion.cursor()

# Creación de tablas

# Tabla departamento
cursor.execute("""
CREATE TABLE IF NOT EXISTS departamento (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE,
    descripcion TEXT NOT NULL
)
""")


# Tabla empleado
cursor.execute("""
CREATE TABLE IF NOT EXISTS empleado (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    direccion TEXT NOT NULL,
    nro_telefono TEXT NOT NULL,
    mail TEXT NOT NULL UNIQUE,
    fecha_inicio_contrato TEXT NOT NULL,
    salario REAL NOT NULL,
    id_departamento INTEGER,
    FOREIGN KEY (id_departamento)
        REFERENCES departamento(id)
)
""")


cursor.execute("""
SELECT name FROM sqlite_master
WHERE type='table'
""")

print(cursor.fetchall())
conexion.commit()
conexion.close()