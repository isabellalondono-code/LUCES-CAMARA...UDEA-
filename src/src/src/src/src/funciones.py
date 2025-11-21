from datos import funciones

# ----------------------------------
# CONSULTAR FUNCIONES DEL FIN DE SEMANA
# ----------------------------------

def consultar_funciones():
    print("\n========== FUNCIONES DEL FIN DE SEMANA ==========")
    print("============= CINE, CÁMARAS Y UDEA ==============\n")

    if not funciones:
        print("No hay funciones registradas por el momento.")
        return

    # Mostrar funciones en orden
    for f in funciones:
        print(f"📅 {f['dia']}  |  🕒 {f['hora']}  |  🎬 {f['nombre']}")

    print("\nRecuerde que las reservas se realizan desde el menú principal.")
