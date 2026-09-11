from empleado import Empleado

class Proyecto:
    def __init__(
        self,
        id_proyecto: int,
        nombre: str,
        descripcion: str
    ):
        self.__id = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleados = []


    def asignar_empleado(self, empleado):
        if isinstance(empleado, Empleado):
            if empleado not in self.empleados:
                self.empleados.append(empleado)
            else:
                raise ValueError("El empleado ya está asignado al proyecto")
        else:
            raise TypeError("Solo se pueden asignar empleados")
        

    def desasignar_empleado(self, empleado):
        if empleado in self.empleados:
            self.empleados.remove(empleado)
        else:
            raise ValueError("El empleado no está asignado al proyecto")
        

    def buscar_empleado(self, id_empleado: int):
        for empleado in self.empleados:
            if empleado.id == id_empleado:
                return empleado

        return None

    def listar_empleados(self):
        return self.empleados