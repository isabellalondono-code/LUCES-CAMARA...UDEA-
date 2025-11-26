from datos import funciones, reservas

def mostrar_sala(asientos):
    print("\n--- Estado Actual de la Sala ---")
    for fila in asientos:
        print(" ".join(fila))

def registrar_reserva():
    print("\n--- Registrar Reserva ---")
    id_funcion = int(input("Ingrese ID de la función: "))

    funcion = next((f for f in funciones if f["id"] == id_funcion), None)

    if not funcion:
        print("Función no encontrada.")
        return

    mostrar_sala(funcion["asientos"])

    fila = int(input("Seleccione fila (0-4): "))
    columna = int(input("Seleccione asiento (0-7): "))

    if funcion["asientos"][fila][columna] == "X":
        print("El asiento ya está ocupado.")
        return

    funcion["asientos"][fila][columna] = "X"

    reserva = {
        "funcion": id_funcion,
        "fila": fila,
        "columna": columna
    }

    reservas.append(reserva)
    print("Reserva registrada exitosamente.")

def cancelar_reserva():
    print("\n--- Cancelar Reserva ---")
    id_funcion = int(input("ID función: "))
    fila = int(input("Fila: "))
    columna = int(input("Columna: "))

    for r in reservas:
        if r["funcion"] == id_funcion and r["fila"] == fila and r["columna"] == columna:
            reservas.remove(r)

            funcion = next(f for f in funciones if f["id"] == id_funcion)
            funcion["asientos"][fila][columna] = "O"

            print("Reserva cancelada.")
            return

    print("Reserva no encontrada.")
