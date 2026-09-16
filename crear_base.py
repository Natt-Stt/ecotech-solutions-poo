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


# Tabla proyecto
cursor.execute("""
CREATE TABLE IF NOT EXISTS proyecto (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE,
    descripcion TEXT NOT NULL
)
""")


# Tabla empleado_proyecto
cursor.execute("""
CREATE TABLE IF NOT EXISTS empleado_proyecto (
    id_empleado INTEGER NOT NULL,
    id_proyecto INTEGER NOT NULL,
    PRIMARY KEY (id_empleado, id_proyecto),
    FOREIGN KEY (id_empleado)
        REFERENCES empleado(id),
    FOREIGN KEY (id_proyecto)
        REFERENCES proyecto(id)
)
""")


# Tabla registro_tiempo
cursor.execute("""
CREATE TABLE IF NOT EXISTS registro_tiempo (
    id INTEGER PRIMARY KEY,
    fecha TEXT NOT NULL,
    horas REAL NOT NULL CHECK (horas > 0),
    id_empleado INTEGER NOT NULL,
    id_proyecto INTEGER NOT NULL,
    FOREIGN KEY (id_empleado)
        REFERENCES empleado(id),
    FOREIGN KEY (id_proyecto)
        REFERENCES proyecto(id)
)
""")


# Tabla usuario
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY,
    nombre_usuario TEXT NOT NULL UNIQUE,
    contrasena_hash TEXT NOT NULL,
    id_empleado INTEGER NOT NULL UNIQUE,
    FOREIGN KEY (id_empleado)
        REFERENCES empleado(id)
)
""")

conexion.commit()
conexion.close()


# Agregando columnas faltantes
cursor.execute("""
CREATE TABLE IF NOT EXISTS departamento (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE,
    descripcion TEXT NOT NULL,
    gerente TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS proyecto (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE,
    descripcion TEXT NOT NULL,
    fecha_inicio TEXT
)
""")