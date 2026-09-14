def mostrar_menu():
    print("\n========================================")
    print("          ECOTECH SOLUTIONS")
    print("========================================")
    print("1. Registrar empleado")
    print("2. Registrar proyecto")
    print("3. Asignar empleado a proyecto")
    print("4. Registrar horas")
    print("5. Consultar empleados")
    print("6. Generar informe")
    print("0. Salir")
    print("========================================")


def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Opción: Registrar empleado")

        elif opcion == "2":
            print("Opción: Registrar proyecto")

        elif opcion == "3":
            print("Opción: Asignar empleado a proyecto")

        elif opcion == "4":
            print("Opción: Registrar horas")

        elif opcion == "5":
            print("Opción: Consultar empleados")

        elif opcion == "6":
            print("Opción: Generar informe")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()