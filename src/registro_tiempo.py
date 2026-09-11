from datetime import date
from empleado import Empleado
from proyecto import Proyecto


class RegistroTiempo:
    def __init__(
        self,
        id_registro: int,
        fecha: date,
        horas: float,
        empleado: Empleado,
        proyecto: Proyecto
    ):
        self.__id = id_registro
        self.fecha = fecha

        if horas > 0:
            self.horas = horas
        else:
            raise ValueError("Las horas deben ser mayores que cero")

        if isinstance(empleado, Empleado):
            self.empleado = empleado
        else:
            raise TypeError("El empleado debe ser un objeto Empleado")

        if isinstance(proyecto, Proyecto):
            self.proyecto = proyecto
        else:
            raise TypeError("El proyecto debe ser un objeto Proyecto")

    def validar_horas(self):
        if self.horas > 0:
            return True
        else:
            return False
