"""
EcoTech Solutions - Sistema de gestión (POO Segura)
====================================================
  1) Inicio de sesión (login) validado contra la clase Usuario.
  2) Menú de Administrador (si el empleado autenticado es Administrador).
  3) Menú de Empleado regular (funciones básicas).
"""

import hashlib
from datetime import date


# =========================================================
# 1. EMPLEADO
# =========================================================
class Empleado:
    _contador_id = 1

    def __init__(self, nombre, direccion, nro_telefono, mail,
                 fecha_inicio_contrato, salario):
        self.__id = Empleado._contador_id
        Empleado._contador_id += 1

        self.nombre = nombre
        self.direccion = direccion
        self.nro_telefono = nro_telefono
        self.mail = mail
        self.fecha_inicio_contrato = fecha_inicio_contrato

        if salario < 0:
            raise ValueError("El salario no puede ser negativo.")
        self.__salario = salario

        self.usuario = None  # se asocia luego mediante _asignar_usuario()

    @property
    def id(self):
        return self.__id

    @property
    def salario(self):
        return self.__salario

    def _actualizar_salario(self, nuevo_salario):
        """Valida y actualiza el salario del empleado."""
        if not isinstance(nuevo_salario, (int, float)):
            raise TypeError("El salario debe ser numérico.")
        if nuevo_salario < 0:
            raise ValueError("El salario no puede ser negativo.")
        self.__salario = nuevo_salario

    def _asignar_usuario(self, usuario):
        """Asocia una cuenta Usuario, evitando una segunda asociación."""
        if not isinstance(usuario, Usuario):
            raise TypeError("Se esperaba una instancia de Usuario.")
        if self.usuario is not None:
            raise ValueError(f"El empleado {self.nombre} ya tiene una cuenta asociada.")
        self.usuario = usuario

    def __str__(self):
        return f"[{self.id}] {self.nombre} - {self.mail}"


# =========================================================
# 2. ADMINISTRADOR (hereda de Empleado)
# =========================================================
class Administrador(Empleado):
    def editar_salario(self, empleado, nuevo_salario):
        """Delega la validación/actualización en el propio Empleado."""
        empleado._actualizar_salario(nuevo_salario)
        print(f"Salario de {empleado.nombre} actualizado a {nuevo_salario}.")

    def agregar_empleado_departamento(self, departamento, empleado):
        """Delega en Departamento.agregar_empleado (bajo acoplamiento)."""
        departamento.agregar_empleado(empleado)
        print(f"{empleado.nombre} agregado al departamento {departamento.nombre}.")

    def reasignar_empleado(self, empleado, departamento_actual, nuevo_departamento):
        departamento_actual.eliminar_empleado(empleado)
        nuevo_departamento.agregar_empleado(empleado)
        print(f"{empleado.nombre} reasignado de {departamento_actual.nombre} "
              f"a {nuevo_departamento.nombre}.")


# =========================================================
# 3. DEPARTAMENTO
# =========================================================
class Departamento:
    _contador_id = 1

    def __init__(self, nombre, descripcion=""):
        self.__id = Departamento._contador_id
        Departamento._contador_id += 1
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleados = []

    @property
    def id(self):
        return self.__id

    def agregar_empleado(self, empleado):
        if not isinstance(empleado, Empleado):
            raise TypeError("Solo se pueden agregar instancias de Empleado.")
        if empleado in self.empleados:
            raise ValueError(f"{empleado.nombre} ya pertenece a este departamento.")
        self.empleados.append(empleado)

    def eliminar_empleado(self, empleado):
        if empleado not in self.empleados:
            raise ValueError(f"{empleado.nombre} no pertenece a este departamento.")
        self.empleados.remove(empleado)

    def buscar_empleado(self, id_empleado):
        for emp in self.empleados:
            if emp.id == id_empleado:
                return emp
        return None

    def listar_empleados(self):
        return list(self.empleados)

    def __str__(self):
        return f"[{self.id}] {self.nombre}"


# =========================================================
# 4. PROYECTO
# =========================================================
class Proyecto:
    _contador_id = 1

    def __init__(self, nombre, descripcion=""):
        self.__id = Proyecto._contador_id
        Proyecto._contador_id += 1
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleados = []

    @property
    def id(self):
        return self.__id

    def asignar_empleado(self, empleado):
        if not isinstance(empleado, Empleado):
            raise TypeError("Solo se pueden asignar instancias de Empleado.")
        if empleado in self.empleados:
            raise ValueError(f"{empleado.nombre} ya está asignado a este proyecto.")
        self.empleados.append(empleado)

    def desasignar_empleado(self, empleado):
        if empleado not in self.empleados:
            raise ValueError(f"{empleado.nombre} no está asignado a este proyecto.")
        self.empleados.remove(empleado)

    def buscar_empleado(self, id_empleado):
        for emp in self.empleados:
            if emp.id == id_empleado:
                return emp
        return None

    def listar_empleados(self):
        return list(self.empleados)

    def __str__(self):
        return f"[{self.id}] {self.nombre}"


# =========================================================
# 5. REGISTROTIEMPO
# =========================================================
class RegistroTiempo:
    _contador_id = 1

    def __init__(self, fecha, horas, empleado, proyecto):
        self.__id = RegistroTiempo._contador_id
        RegistroTiempo._contador_id += 1

        if not isinstance(empleado, Empleado):
            raise TypeError("empleado debe ser una instancia de Empleado.")
        if not isinstance(proyecto, Proyecto):
            raise TypeError("proyecto debe ser una instancia de Proyecto.")
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")

        self.fecha = fecha
        self.horas = horas
        self.empleado = empleado
        self.proyecto = proyecto

    @property
    def id(self):
        return self.__id

    def validar_horas(self):
        return self.horas > 0

    def __str__(self):
        return (f"[{self.id}] {self.fecha} - {self.horas}h - "
                f"{self.empleado.nombre} / {self.proyecto.nombre}")


# =========================================================
# 6. USUARIO
# =========================================================
class Usuario:
    _contador_id = 1

    def __init__(self, nombre_usuario, contrasena, empleado):
        self.__id = Usuario._contador_id
        Usuario._contador_id += 1

        if not isinstance(empleado, Empleado):
            raise TypeError("empleado debe ser una instancia de Empleado.")

        self.nombre_usuario = nombre_usuario
        self.__contrasena = self._generar_hash(contrasena)
        self.empleado = empleado

        # Asocia esta cuenta al empleado (falla si ya tiene una)
        empleado._asignar_usuario(self)

    @property
    def id(self):
        return self.__id

    def _generar_hash(self, contrasena):
        return hashlib.sha256(contrasena.encode("utf-8")).hexdigest()

    def verificar_contrasena(self, contrasena):
        return self.__contrasena == self._generar_hash(contrasena)

    def cambiar_contrasena(self, nueva_contrasena):
        if not nueva_contrasena:
            raise ValueError("La contraseña no puede estar vacía.")
        self.__contrasena = self._generar_hash(nueva_contrasena)

    def __str__(self):
        return f"[{self.id}] {self.nombre_usuario} ({self.empleado.nombre})"


# =========================================================
# 7. INFORME
# =========================================================
class Informe:
    _contador_id = 1

    def __init__(self, titulo):
        self.__id = Informe._contador_id
        Informe._contador_id += 1
        self.titulo = titulo
        self.registros = []

    @property
    def id(self):
        return self.__id

    def agregar_registro(self, registro):
        if not isinstance(registro, RegistroTiempo):
            raise TypeError("Solo se pueden agregar instancias de RegistroTiempo.")
        self.registros.append(registro)

    def calcular_total_horas(self):
        return sum(r.horas for r in self.registros)

    def calcular_horas_empleado(self, empleado):
        return sum(r.horas for r in self.registros if r.empleado == empleado)

    def calcular_horas_proyecto(self, proyecto):
        return sum(r.horas for r in self.registros if r.proyecto == proyecto)

    def generar_resumen(self):
        lineas = [f"--- Informe: {self.titulo} ---"]
        lineas.append(f"Total de registros: {len(self.registros)}")
        lineas.append(f"Total de horas: {self.calcular_total_horas()}")
        for r in self.registros:
            lineas.append(f"  {r}")
        return "\n".join(lineas)


# =========================================================
# DATOS DE DEMOSTRACIÓN (seed data en memoria)
# =========================================================
def cargar_datos_demo():
    depto_dev = Departamento("Desarrollo", "Área de desarrollo de software")
    depto_ops = Departamento("Operaciones", "Área de operaciones sostenibles")

    proyecto_a = Proyecto("Panel Solar Comunitario", "Instalación de paneles en zonas rurales")
    proyecto_b = Proyecto("App de Reciclaje", "Aplicación móvil de gestión de reciclaje")

    emp_admin = Administrador(
        nombre="Natalia Trejo",
        direccion="Av. Siempre Viva 123",
        nro_telefono="+56911111111",
        mail="natalia.trejo@ecotech.cl",
        fecha_inicio_contrato=date(2023, 1, 15),
        salario=1500000,
    )

    emp_regular = Empleado(
        nombre="Juan Pérez",
        direccion="Calle Falsa 456",
        nro_telefono="+56922222222",
        mail="juan.perez@ecotech.cl",
        fecha_inicio_contrato=date(2024, 3, 1),
        salario=900000,
    )

    depto_dev.agregar_empleado(emp_admin)
    depto_ops.agregar_empleado(emp_regular)

    proyecto_a.asignar_empleado(emp_regular)
    proyecto_b.asignar_empleado(emp_admin)

    usuario_admin = Usuario("admin", "admin123", emp_admin)
    usuario_regular = Usuario("jperez", "clave123", emp_regular)

    informe_general = Informe("Informe General de Horas")

    estado = {
        "departamentos": [depto_dev, depto_ops],
        "proyectos": [proyecto_a, proyecto_b],
        "empleados": [emp_admin, emp_regular],
        "usuarios": [usuario_admin, usuario_regular],
        "registros": [],
        "informe": informe_general,
    }
    return estado


# =========================================================
# UTILIDADES DE INTERFAZ
# =========================================================
def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor ingresa un número entero válido.")


def pedir_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor ingresa un número válido.")


def seleccionar_de_lista(lista, nombre_entidad):
    if not lista:
        print(f"No hay {nombre_entidad} registrados.")
        return None
    for item in lista:
        print(f"  {item}")
    id_sel = pedir_entero(f"Ingresa el ID de {nombre_entidad}: ")
    for item in lista:
        if item.id == id_sel:
            return item
    print("No se encontró un elemento con ese ID.")
    return None


# =========================================================
# LOGIN
# =========================================================
def login(estado):
    print("\n=== INICIO DE SESIÓN ===")
    nombre_usuario = input("Usuario: ").strip()
    contrasena = input("Contraseña: ").strip()

    for usuario in estado["usuarios"]:
        if usuario.nombre_usuario == nombre_usuario:
            if usuario.verificar_contrasena(contrasena):
                print(f"\nBienvenido/a, {usuario.empleado.nombre}.")
                return usuario
            else:
                print("Contraseña incorrecta.")
                return None
    print("Usuario no encontrado.")
    return None


# =========================================================
# MENÚ ADMINISTRADOR
# =========================================================
def menu_administrador(estado, admin: Administrador):
    while True:
        print("\n=== MENÚ ADMINISTRADOR ===")
        print("1) Editar salario de un empleado")
        print("2) Agregar empleado a un departamento")
        print("3) Reasignar empleado entre departamentos")
        print("4) Crear departamento")
        print("5) Crear proyecto")
        print("6) Asignar empleado a proyecto")
        print("7) Registrar horas trabajadas")
        print("8) Generar resumen de informe")
        print("9) Listar empleados")
        print("0) Cerrar sesión")

        opcion = input("Selecciona una opción: ").strip()

        try:
            if opcion == "1":
                print("\nEmpleados disponibles:")
                empleado = seleccionar_de_lista(estado["empleados"], "empleado")
                if empleado:
                    nuevo_salario = pedir_flotante("Nuevo salario: ")
                    admin.editar_salario(empleado, nuevo_salario)

            elif opcion == "2":
                print("\nDepartamentos disponibles:")
                depto = seleccionar_de_lista(estado["departamentos"], "departamento")
                if depto:
                    print("\nEmpleados disponibles:")
                    empleado = seleccionar_de_lista(estado["empleados"], "empleado")
                    if empleado:
                        admin.agregar_empleado_departamento(depto, empleado)

            elif opcion == "3":
                print("\nEmpleados disponibles:")
                empleado = seleccionar_de_lista(estado["empleados"], "empleado")
                if empleado:
                    print("\nDepartamento actual:")
                    depto_actual = seleccionar_de_lista(estado["departamentos"], "departamento")
                    print("\nNuevo departamento:")
                    depto_nuevo = seleccionar_de_lista(estado["departamentos"], "departamento")
                    if depto_actual and depto_nuevo:
                        admin.reasignar_empleado(empleado, depto_actual, depto_nuevo)

            elif opcion == "4":
                nombre = input("Nombre del nuevo departamento: ").strip()
                descripcion = input("Descripción: ").strip()
                nuevo_depto = Departamento(nombre, descripcion)
                estado["departamentos"].append(nuevo_depto)
                print(f"Departamento creado: {nuevo_depto}")

            elif opcion == "5":
                nombre = input("Nombre del nuevo proyecto: ").strip()
                descripcion = input("Descripción: ").strip()
                nuevo_proyecto = Proyecto(nombre, descripcion)
                estado["proyectos"].append(nuevo_proyecto)
                print(f"Proyecto creado: {nuevo_proyecto}")

            elif opcion == "6":
                print("\nProyectos disponibles:")
                proyecto = seleccionar_de_lista(estado["proyectos"], "proyecto")
                if proyecto:
                    print("\nEmpleados disponibles:")
                    empleado = seleccionar_de_lista(estado["empleados"], "empleado")
                    if empleado:
                        proyecto.asignar_empleado(empleado)
                        print(f"{empleado.nombre} asignado a {proyecto.nombre}.")

            elif opcion == "7":
                print("\nEmpleados disponibles:")
                empleado = seleccionar_de_lista(estado["empleados"], "empleado")
                print("\nProyectos disponibles:")
                proyecto = seleccionar_de_lista(estado["proyectos"], "proyecto")
                if empleado and proyecto:
                    fecha_str = input("Fecha (AAAA-MM-DD): ").strip()
                    anio, mes, dia = map(int, fecha_str.split("-"))
                    fecha = date(anio, mes, dia)
                    horas = pedir_flotante("Horas trabajadas: ")
                    registro = RegistroTiempo(fecha, horas, empleado, proyecto)
                    estado["registros"].append(registro)
                    estado["informe"].agregar_registro(registro)
                    print(f"Registro creado: {registro}")

            elif opcion == "8":
                print("\n" + estado["informe"].generar_resumen())

            elif opcion == "9":
                print("\nEmpleados registrados:")
                for emp in estado["empleados"]:
                    tipo = "Administrador" if isinstance(emp, Administrador) else "Empleado"
                    print(f"  {emp} - {tipo} - Salario: {emp.salario}")

            elif opcion == "0":
                print("Cerrando sesión...")
                break

            else:
                print("Opción inválida.")

        except (ValueError, TypeError) as e:
            print(f"Error: {e}")


# =========================================================
# MENÚ EMPLEADO REGULAR
# =========================================================
def menu_empleado(estado, empleado: Empleado):
    while True:
        print("\n=== MENÚ EMPLEADO ===")
        print("1) Ver mis datos")
        print("2) Registrar horas trabajadas")
        print("3) Ver mis horas totales")
        print("4) Cambiar mi contraseña")
        print("0) Cerrar sesión")

        opcion = input("Selecciona una opción: ").strip()

        try:
            if opcion == "1":
                print(f"\nNombre: {empleado.nombre}")
                print(f"Dirección: {empleado.direccion}")
                print(f"Teléfono: {empleado.nro_telefono}")
                print(f"Correo: {empleado.mail}")
                print(f"Fecha inicio contrato: {empleado.fecha_inicio_contrato}")

            elif opcion == "2":
                print("\nProyectos disponibles:")
                proyecto = seleccionar_de_lista(estado["proyectos"], "proyecto")
                if proyecto:
                    fecha_str = input("Fecha (AAAA-MM-DD): ").strip()
                    anio, mes, dia = map(int, fecha_str.split("-"))
                    fecha = date(anio, mes, dia)
                    horas = pedir_flotante("Horas trabajadas: ")
                    registro = RegistroTiempo(fecha, horas, empleado, proyecto)
                    estado["registros"].append(registro)
                    estado["informe"].agregar_registro(registro)
                    print(f"Registro creado: {registro}")

            elif opcion == "3":
                total = estado["informe"].calcular_horas_empleado(empleado)
                print(f"\nTotal de horas registradas: {total}")

            elif opcion == "4":
                nueva = input("Nueva contraseña: ").strip()
                empleado.usuario.cambiar_contrasena(nueva)
                print("Contraseña actualizada correctamente.")

            elif opcion == "0":
                print("Cerrando sesión...")
                break

            else:
                print("Opción inválida.")

        except (ValueError, TypeError) as e:
            print(f"Error: {e}")


# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================
def main():
    estado = cargar_datos_demo()

    print("==========================================")
    print(" EcoTech Solutions - Sistema de Gestión")
    print("==========================================")
    print("(Datos de prueba precargados)")
    print("  Admin  -> usuario: admin   / contraseña: admin123")
    print("  Empleado -> usuario: jperez / contraseña: clave123")

    while True:
        usuario = login(estado)
        if usuario is None:
            reintentar = input("\n¿Intentar de nuevo? (s/n): ").strip().lower()
            if reintentar != "s":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            continue

        empleado_autenticado = usuario.empleado

        if isinstance(empleado_autenticado, Administrador):
            menu_administrador(estado, empleado_autenticado)
        else:
            menu_empleado(estado, empleado_autenticado)

        continuar = input("\n¿Deseas iniciar sesión con otra cuenta? (s/n): ").strip().lower()
        if continuar != "s":
            print("Saliendo del sistema. ¡Hasta luego!")
            break


if __name__ == "__main__":
    main()