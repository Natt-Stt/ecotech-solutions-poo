from registro_tiempo import RegistroTiempo


class Informe:
    def __init__(
        self,
        id_informe: int,
        titulo: str
    ):
        self.__id = id_informe
        self.titulo = titulo
        self.registros = []

    def agregar_registro(self, registro):
        if isinstance(registro, RegistroTiempo):
           if registro not in self.registros:
            self.registros.append(registro)
           else:
                raise ValueError("El registro ya está incluido en el informe")
        else:
            raise TypeError("Solo se pueden agregar registros de tiempo")


    def generar_resumen(self):
        resumen = []

        for registro in self.registros:
            resumen.append(
                f"Empleado: {registro.empleado.nombre} | "
                f"Proyecto: {registro.proyecto.nombre} | "
                f"Fecha: {registro.fecha} | "
                f"Horas: {registro.horas}"
            )

        return resumen


    def calcular_total_horas(self):
        total_horas = 0

        for registro in self.registros:
            total_horas += registro.horas

        return total_horas


    
    def calcular_horas_empleado(self, empleado):
        total_horas = 0

        for registro in self.registros:
            if registro.empleado == empleado:
               total_horas += registro.horas

        return total_horas


    def calcular_horas_proyecto(self, proyecto):
        total_horas = 0

        for registro in self.registros:
            if registro.proyecto == proyecto:
               total_horas += registro.horas

        return total_horas