from datetime import date
from empleado import Empleado
from administrador import Administrador
from departamento import Departamento
from proyecto import Proyecto
from usuario import Usuario

empleado_1 = Empleado(
    1,
    "Natalia",
    "Viña del Mar",
    "912345678",
    "natalia@ecotech.cl",
    date(2026, 3, 1),
    800000.0
)

print(empleado_1.nombre)
print(empleado_1.direccion)
print(empleado_1.mail)
print(empleado_1.fecha_inicio_contrato)

administrador_1 = Administrador(
    2,
    "Carlos",
    "Valparaíso",
    "987654321",
    "carlos@ecotech.cl",
    date(2026, 3, 1),
    900000
)

print(administrador_1.nombre)
print(administrador_1.mail)
print(administrador_1.fecha_inicio_contrato)

departamento_1 = Departamento(
    1,
    "Recursos Humanos",
    "Gestiona los procesos relacionados con los empleados"
)

print(departamento_1.nombre)
print(departamento_1.descripcion)
print(departamento_1.empleados)

departamento_1.agregar_empleado(empleado_1)
departamento_1.agregar_empleado(administrador_1)

print(departamento_1.empleados[0].nombre)
print(departamento_1.empleados[1].nombre)

try:
    administrador_1.editar_salario(empleado_1, -100000)
except ValueError as error:
    print("Error:", error)

try:
    departamento_1.agregar_empleado("Carlos")
except TypeError as error:
    print("Error:", error)

try:
    departamento_1.agregar_empleado(empleado_1)
except ValueError as error:
    print("Error:", error)

departamento_1.eliminar_empleado(empleado_1)

print(departamento_1.empleados)
print(departamento_1.empleados[0].nombre)

try:
    departamento_1.eliminar_empleado(empleado_1)
except ValueError as error:
    print("Error:", error)

print(empleado_1.id)
print(administrador_1.id)

departamento_1.agregar_empleado(empleado_1)
empleado_encontrado = departamento_1.buscar_empleado(1)

if empleado_encontrado is not None:
    print("Empleado encontrado:", empleado_encontrado.nombre)
else:
    print("Empleado no encontrado")

empleado_encontrado = departamento_1.buscar_empleado(99)

if empleado_encontrado is not None:
    print("Empleado encontrado:", empleado_encontrado.nombre)
else:
    print("Empleado no encontrado")

empleados_departamento = departamento_1.listar_empleados()

for empleado in empleados_departamento:
    print(empleado.id, empleado.nombre)

empleado_2 = Empleado(
    3,
    "Andrea",
    "Quilpué",
    "923456789",
    "andrea@ecotech.cl",
    date(2026, 4, 1),
    750000
)

administrador_1.agregar_empleado_departamento(
    departamento_1,
    empleado_2
)
for empleado in departamento_1.listar_empleados():
    print(empleado.id, empleado.nombre)

try:
    administrador_1.agregar_empleado_departamento(
        departamento_1,
        empleado_2
    )
except ValueError as error:
    print("Error:", error)

departamento_2 = Departamento(
    2,
    "Tecnología",
    "Gestiona los sistemas y recursos tecnológicos"
)
print(departamento_2.nombre)

administrador_1.reasignar_empleado(
    empleado_1,
    departamento_1,
    departamento_2
)
print("Recursos Humanos:")

for empleado in departamento_1.listar_empleados():
    print(empleado.id, empleado.nombre)

print("Tecnología:")

for empleado in departamento_2.listar_empleados():
    print(empleado.id, empleado.nombre)

proyecto_1 = Proyecto(
    1,
    "Plataforma Web EcoTech",
    "Desarrollo de una nueva plataforma web para EcoTech Solutions"
)
print(proyecto_1.nombre)
print(proyecto_1.descripcion)
print(proyecto_1.empleados)

proyecto_1.asignar_empleado(empleado_1)

print("Empleados del proyecto:")
for empleado in proyecto_1.empleados:
    print(empleado.id, empleado.nombre)

try:
    proyecto_1.asignar_empleado("Carlos")
except TypeError as error:
    print("Error:", error)

try:
    proyecto_1.asignar_empleado(empleado_1)
except ValueError as error:
    print("Error:", error)

proyecto_1.desasignar_empleado(empleado_1)

print("Empleados del proyecto después de desasignar:")
for empleado in proyecto_1.empleados:
    print(empleado.id, empleado.nombre)

print(proyecto_1.empleados)

try:
    proyecto_1.desasignar_empleado(empleado_1)
except ValueError as error:
    print("Error:", error)

proyecto_1.asignar_empleado(empleado_1)
empleado_encontrado = proyecto_1.buscar_empleado(1)

if empleado_encontrado is not None:
    print("Empleado encontrado:", empleado_encontrado.nombre)
else:
    print("Empleado no encontrado")

empleado_encontrado = proyecto_1.buscar_empleado(99)

if empleado_encontrado is not None:
    print("Empleado encontrado:", empleado_encontrado.nombre)
else:
    print("Empleado no encontrado")

print("Empleados del proyecto:")
for empleado in proyecto_1.listar_empleados():
    print(empleado.id, empleado.nombre)

from registro_tiempo import RegistroTiempo
registro_1 = RegistroTiempo(
    1,
    date(2026, 9, 10),
    4.0,
    empleado_1,
    proyecto_1
)

print(registro_1.fecha)
print(registro_1.horas)
print(registro_1.empleado.nombre)
print(registro_1.proyecto.nombre)

try:
    registro_invalido = RegistroTiempo(
        2,
        date(2026, 9, 10),
        -5.0,
        empleado_1,
        proyecto_1
    )
except ValueError as error:
    print("Error:", error)

try:
    registro_invalido = RegistroTiempo(
        2,
        date(2026, 9, 10),
        4.0,
        "Natalia",
        proyecto_1
    )
except TypeError as error:
    print("Error:", error)

try:
    registro_invalido = RegistroTiempo(
        3,
        date(2026, 9, 10),
        4.0,
        empleado_1,
        "Plataforma Web EcoTech"
    )
except TypeError as error:
    print("Error:", error)

print("¿Las horas son válidas?", registro_1.validar_horas())
usuario_1 = Usuario(
    1,
    "natalia",
    "EcoTech123",
    empleado_1
)
print(usuario_1.nombre_usuario)
print(usuario_1.empleado.nombre)

try:
    usuario_invalido = Usuario(
        2,
        "carlos",
        "EcoTech456",
        "Carlos"
    )
except TypeError as error:
    print("Error:", error)
