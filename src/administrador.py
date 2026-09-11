from empleado import Empleado


class Administrador(Empleado):

    def editar_salario(self, empleado: Empleado, nuevo_salario: float):
        empleado._actualizar_salario(nuevo_salario)

    def agregar_empleado_departamento(self, departamento, empleado: Empleado):
        departamento.agregar_empleado(empleado)

    def reasignar_empleado(self, empleado: Empleado, departamento_actual, nuevo_departamento):
        departamento_actual.eliminar_empleado(empleado)
        nuevo_departamento.agregar_empleado(empleado)