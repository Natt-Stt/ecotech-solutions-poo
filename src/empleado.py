from datetime import date


class Empleado:
    def __init__(
        self,
        id_empleado: int,
        nombre: str,
        direccion: str,
        nro_telefono: str,
        mail: str,
        fecha_inicio_contrato: date,
        salario: float
    ):
        self.__id = id_empleado
        self.nombre = nombre
        self.direccion = direccion
        self.nro_telefono = nro_telefono
        self.mail = mail
        self.fecha_inicio_contrato = fecha_inicio_contrato
        self.__salario = salario

    @property
    def id(self):
        return self.__id

    def _actualizar_salario(self, nuevo_salario: float):
     if nuevo_salario >= 0:
        self.__salario = nuevo_salario
     else:
        raise ValueError("El salario no puede ser negativo")