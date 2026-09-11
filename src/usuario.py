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
        self.empleado = empleado