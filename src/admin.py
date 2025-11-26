from datos import funciones, reservas

def menu_admin():
    while True:
        print("\n--- MENÚ ADMINISTRATIVO ---")
        print("1. Ver todas las reservas")
        print("2. Ver funciones")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nReservas registradas:")
            for r in reservas:
                print(r)

        elif opcion == "2":
            print("\nFunciones disponibles:")
            for f in funciones:
                print(f)

        elif opcion == "3":
            break

        else:
            print("Opción inválida.")
