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
        self.__contrasena = self._generar_hash(contrasena)

        if isinstance(empleado, Empleado):
            self.empleado = empleado
        else:
            raise TypeError("El usuario debe estar asociado a un empleado")

    def _generar_hash(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def verificar_contrasena(self, contrasena):
        hash_ingresado = self._generar_hash(contrasena)
        return hash_ingresado == self.__contrasena