from empleado import Empleado


class Departamento:
    def __init__(
        self,
        id_departamento: int,
        nombre: str,
        descripcion: str
    ):
        self.__id = id_departamento
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleados = []

    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado):
            if empleado not in self.empleados:
                self.empleados.append(empleado)
            else:
                raise ValueError("El empleado ya pertenece al departamento")
        else:
            raise TypeError("Solo se pueden agregar empleados")

    def eliminar_empleado(self, empleado):
        if empleado in self.empleados:
         self.empleados.remove(empleado)
        else:
            raise ValueError("El empleado no pertenece al departamento")

    def buscar_empleado(self, id_empleado: int):
        for empleado in self.empleados:
           if empleado.id == id_empleado:
              return empleado

        return None

    def listar_empleados(self):
        return self.empleados