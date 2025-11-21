from datos import usuarios, reservas

# --------------------------------------
# MENÚ DE ADMINISTRACIÓN
# --------------------------------------

def menu_admin():
    print("\n=== ACCESO A ADMINISTRACIÓN DEL CINE, CÁMARAS Y UDEA ===")

    # Usuario y contraseña predefinidos
    usuario_admin = "admin"
    password_admin = "1234"

    usuario = input("Ingrese usuario administrador: ")
    contraseña = input("Ingrese contraseña: ")

    if usuario != usuario_admin or contraseña != password_admin:
        print("❌ Acceso denegado. Usuario o contraseña incorrectos.")
        return

    while True:
        print("\n======= PANEL ADMINISTRATIVO =======")
        print("1. Total de reservas registradas")
        print("2. Total de tiquetes vendidos")
        print("3. Total pago realizado (recaudo)")
        print("4. Promedio por venta diario del cine")
        print("5. Lista de usuarios")
        print("6. Usuario con mayor cantidad de reservas")
        print("7. Usuario con menor cantidad de reservas")
        print("8. Salir del panel")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            total_reservas()

        elif opcion == "2":
            total_tiquetes()

        elif opcion == "3":
            total_recaudo()

        elif opcion == "4":
            promedio_diario()

        elif opcion == "5":
            listar_usuarios()

        elif opcion == "6":
            mayor_reservas()

        elif opcion == "7":
            menor_reservas()

        elif opcion == "8":
            print("\nSaliendo del administrador...")
            break

        else:
            print("❌ Opción inválida.")


# --------------------------------------
# REPORTES
# --------------------------------------

def total_reservas():
    print(f"\n📌 Total de reservas registradas: {len(reservas)}")


def total_tiquetes():
    print(f"\n🎟️ Total de tiquetes vendidos: {len(reservas)}")


def total_recaudo():
    total = sum(r["precio"] for r in reservas)
    print(f"\n💰 Total recaudado: ${total}")


def promedio_diario():
    if len(reservas) == 0:
        print("\nNo hay datos suficientes para calcular el promedio.")
        return

    # Consideramos solo sábado y domingo: 2 días
    promedio = sum(r["precio"] for r in reservas) / 2
    print(f"\n📊 Promedio por día del fin de semana: ${promedio:.2f}")


def listar_usuarios():
    if not usuarios:
        print("\nNo hay usuarios registrados.")
        return

    print("\n=== LISTA DE USUARIOS REGISTRADOS ===")
    for u in usuarios:
        print(f"- {u['nombre']} {u['apellido']} ({u['tipo']})  Doc: {u['documento']}")


def mayor_reservas():
    if not reservas:
        print("\nNo hay reservas registradas.")
        return

    contador = {}  # documento : número de reservas

    for r in reservas:
        doc = r["usuario"]["documento"]
        contador[doc] = contador.get(doc, 0) + 1

    # Usuario con mayor reservas
    doc_mayor = max(contador, key=contador.get)
    cant = contador[doc_mayor]

    usuario = next(u for u in usuarios if u["documento"] == doc_mayor)

    print(f"\n🏆 Usuario con más reservas: {usuario['nombre']} {usuario['apellido']} ({cant} reservas)")


def menor_reservas():
    if not reservas:
        print("\nNo hay reservas registradas.")
        return

    contador = {}

    for r in reservas:
        doc = r["usuario"]["documento"]
        contador[doc] = contador.get(doc, 0) + 1

    doc_menor = min(contador, key=contador.get)
    cant = contador[doc_menor]

    usuario = next(u for u in usuarios if u["documento"] == doc_menor)

    print(f"\n📉 Usuario con menos reservas: {usuario['nombre']} {usuario['apellido']} ({cant} reservas)")
