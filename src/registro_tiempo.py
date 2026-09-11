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

        self.empleado = empleado
        self.proyecto = proyecto