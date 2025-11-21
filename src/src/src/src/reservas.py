from datos import sala, usuarios, reservas

# ----------------------------------
# FUNCIÓN PARA MOSTRAR LA SALA
# ----------------------------------

def mostrar_sala():
    print("\nCINE, CÁMARAS Y UDEA  (O = Disponible / X = Ocupado)\n")

    columnas = "   " + "  ".join([chr(65 + i) for i in range(len(sala[0]))])
    print(columnas)

    for i, fila in enumerate(sala):
        fila_str = f"{chr(65 + i)}  " + "  ".join(fila)
        print(fila_str)


# ----------------------------------
# BUSCAR USUARIO POR DOCUMENTO
# ----------------------------------

def buscar_usuario(documento):
    for u in usuarios:
        if u["documento"] == documento:
            return u
    return None


# ----------------------------------
# REGISTRAR RESERVA
# ----------------------------------

def registrar_reserva():
    print("\n=== REGISTRAR RESERVA ===")

    documento = input("Ingrese el documento del usuario: ")

    usuario = buscar_usuario(documento)
    if usuario is None:
        print("❌ El usuario no está registrado. Primero debe registrarse.")
        return

    mostrar_sala()

    asiento = input("\nSeleccione el asiento (Ej: A5): ").upper()

    if len(asiento) < 2:
        print("❌ Formato inválido. Debe ser como A5.")
        return

    fila_letra = asiento[0]
    col_num = asiento[1:]

    if not col_num.isdigit():
        print("❌ El número de silla debe ser numérico.")
        return

    fila = ord(fila_letra) - 65
    col = int(col_num)

    if fila < 0 or fila >= len(sala) or col < 0 or col >= len(sala[0]):
        print("❌ El asiento no existe.")
        return

    if sala[fila][col] == "X":
        print("❌ El asiento ya está ocupado.")
        return

    sala[fila][col] = "X"

    reservas.append({
        "usuario": usuario,
        "fila": fila_letra,
        "columna": col,
        "precio": usuario["precio"]
    })

    print("\n✔ Reserva realizada con éxito.")
    print(f"Asiento reservado: {fila_letra}{col}")
    print(f"Total a pagar: ${usuario['precio']}\n")


# ----------------------------------
# CANCELAR RESERVA
# ----------------------------------

def cancelar_reserva():
    print("\n=== CANCELAR RESERVA ===")

    documento = input("Ingrese el documento del usuario: ")

    usuario = buscar_usuario(documento)
    if usuario is None:
        print("❌ No existe un usuario con ese documento.")
        return

    reservas_usuario = [r for r in reservas if r["usuario"]["documento"] == documento]

    if not reservas_usuario:
        print("❌ El usuario no tiene reservas activas.")
        return

    print("\nReservas activas del usuario:")
    for i, r in enumerate(reservas_usuario):
        print(f"{i+1}. Asiento {r['fila']}{r['columna']} - ${r['precio']}")

    opcion = input("\nSeleccione la reserva a cancelar: ")

    if not opcion.isdigit() or not (1 <= int(opcion) <= len(reservas_usuario)):
        print("❌ Opción inválida.")
        return

    reserva = reservas_usuario[int(opcion) - 1]

    fila = ord(reserva["fila"]) - 65
    columna = reserva["columna"]
    sala[fila][columna] = "O"

    reservas.remove(reserva)

    print("\n✔ Reserva cancelada exitosamente.")
    print(f"Asiento liberado: {reserva['fila']}{reserva['columna']}")
