import sqlite3
import os

# Ruta absoluta al archivo .db, para que funcione sin importar
# desde qué carpeta ejecutes el programa
RUTA_DB = os.path.join(os.path.dirname(__file__), "..", "ecotech.db")


def conectar():
    conexion = sqlite3.connect(RUTA_DB)
    conexion.execute("PRAGMA foreign_keys = ON")
    conexion.row_factory = sqlite3.Row
    return conexion


def crear_empleado(nombre, direccion, nro_telefono, mail, fecha_inicio_contrato, salario, id_departamento=None):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            """
            INSERT INTO empleado (nombre, direccion, nro_telefono, mail, fecha_inicio_contrato, salario, id_departamento)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (nombre, direccion, nro_telefono, mail, fecha_inicio_contrato, salario, id_departamento)
        )
        conexion.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error al crear empleado: {e}")
        return None
    finally:
        conexion.close()



def listar_empleados():
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM empleado")
        filas = cursor.fetchall()
        return [dict(fila) for fila in filas]
    except sqlite3.Error as e:
        print(f"Error al listar empleados: {e}")
        return []
    finally:
        conexion.close()


def crear_departamento(nombre, descripcion, gerente=None):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO departamento (nombre, descripcion, gerente) VALUES (?, ?, ?)",
            (nombre, descripcion, gerente)
        )
        conexion.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error al crear departamento: {e}")
        return None
    finally:
        conexion.close()


def listar_departamentos():
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM departamento")
        return [dict(fila) for fila in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Error al listar departamentos: {e}")
        return []
    finally:
        conexion.close()


def crear_proyecto(nombre, descripcion, fecha_inicio=None):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO proyecto (nombre, descripcion, fecha_inicio) VALUES (?, ?, ?)",
            (nombre, descripcion, fecha_inicio)
        )
        conexion.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error al crear proyecto: {e}")
        return None
    finally:
        conexion.close()


def listar_proyectos():
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM proyecto")
        return [dict(fila) for fila in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Error al listar proyectos: {e}")
        return []
    finally:
        conexion.close()


import hashlib


def crear_registro_tiempo(fecha, horas, id_empleado, id_proyecto):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO registro_tiempo (fecha, horas, id_empleado, id_proyecto) VALUES (?, ?, ?, ?)",
            (fecha, horas, id_empleado, id_proyecto)
        )
        conexion.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error al crear registro de tiempo: {e}")
        return None
    finally:
        conexion.close()


def listar_registros_tiempo():
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM registro_tiempo")
        return [dict(fila) for fila in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Error al listar registros de tiempo: {e}")
        return []
    finally:
        conexion.close()


def crear_usuario(nombre_usuario, contrasena, id_empleado):
    contrasena_hash = hashlib.sha256(contrasena.encode()).hexdigest()
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO usuario (nombre_usuario, contrasena_hash, id_empleado) VALUES (?, ?, ?)",
            (nombre_usuario, contrasena_hash, id_empleado)
        )
        conexion.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error al crear usuario: {e}")
        return None
    finally:
        conexion.close()


def verificar_usuario(nombre_usuario, contrasena):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM usuario WHERE nombre_usuario = ?",
            (nombre_usuario,)
        )
        fila = cursor.fetchone()
        if fila is None:
            return False  # el usuario no existe
        contrasena_hash = hashlib.sha256(contrasena.encode()).hexdigest()
        return fila["contrasena_hash"] == contrasena_hash
    except sqlite3.Error as e:
        print(f"Error al verificar usuario: {e}")
        return False
    finally:
        conexion.close()