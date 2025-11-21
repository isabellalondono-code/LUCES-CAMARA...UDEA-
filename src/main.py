from usuarios import registrar_usuario
from reservas import registrar_reserva, cancelar_reserva, mostrar_sala
from funciones import consultar_funciones
from admin import menu_admin

# -------------------------------
# MENÚ PRINCIPAL DEL CINE, CÁMARAS Y UDEA
# -------------------------------

def menu_principal():
    while True:
        print("\n========== CINE, CÁMARAS Y UDEA ==========\n")
        print("1. Registrar Usuario")
        print("2. Registrar Reserva")
        print("3. Cancelar Reserva")
        print("4. Consultar Funciones Fin de Semana")
        print("5. Administrador")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            registrar_reserva()

        elif opcion == "3":
            cancelar_reserva()

        elif opcion == "4":
            consultar_funciones()

        elif opcion == "5":
            menu_admin()

        elif opcion == "6":
            print("\nGracias por usar Cine, Cámaras y UdeA. ¡Hasta luego!")
            break

        else:
            print("\n❌ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu_principal()

