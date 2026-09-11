import hashlib
from empleado import Empleado


class Usuario:
    def __init__(
        self,
        id_usuario: int,
        nombre_usuario: str,
        contrasena: str,
        empleado: Empleado
    ):
        self.__id = id_usuario
        self.nombre_usuario = nombre_usuario
        self.__contrasena = contrasena

        if isinstance(empleado, Empleado):
            self.empleado = empleado
        else:
            raise TypeError("El usuario debe estar asociado a un empleado")

    def _generar_hash(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()