 import csv
from datetime import datetime
import pytz

# -----------------------------
# Datos iniciales del sistema
# -----------------------------

TARIFAS = {
    "Estudiantes": 7500,
    "Docentes": 10000,
    "Administrativos": 8500,
    "Oficiales internos": 7000,
    "Publico externo": 15000,
}

TIPOS_VINCULO_VALIDOS = list(TARIFAS.keys())

# Cartelera del fin de semana
CARTELERA = [
    {"id": 1, "dia": "Viernes", "hora": "2pm", "pelicula": "Zootopia 2"},
    {"id": 1, "dia": "Viernes", "hora": "4pm", "pelicula": "Zootopia 2"},
    {"id": 1, "dia": "Viernes", "hora": "6pm", "pelicula": "Zootopia 2"},
    {"id": 2, "dia": "Sabado", "hora": "2pm", "pelicula": "Los ilusionistas 3"},
    {"id": 2, "dia": "Sabado", "hora": "4pm", "pelicula": "Los ilusionistas 3"},
    {"id": 2, "dia": "Sabado", "hora": "6pm", "pelicula": "Los ilusionistas 3"},
    {"id": 3, "dia": "Domingo", "hora": "2pm", "pelicula": "Depredador"},
    {"id": 3, "dia": "Domingo", "hora": "4pm", "pelicula": "Depredador"},
    {"id": 3, "dia": "Domingo", "hora": "6pm", "pelicula": "Depredador"},
]

# Usuarios y reservas en memoria
USUARIOS = {}  # key: documento, value: dict con datos del usuario
# Estado de asientos por función (cada función tiene su propio mapa 11x11)
# Clave será un índice de la lista CARTELERA (0..len-1)
ASIENTOS = {}
RESERVAS = []  # cada reserva: {documento, idx_funcion, asiento, valor, fecha}

# Inicializa asientos (11 filas A-K, 11 columnas 1-11, "O" libre, "X" ocupado)
def crear_mapa_asientos():
    filas = [chr(ord('A') + i) for i in range(11)]  # A..K
    columnas = list(range(1, 12))  # 1..11
    return {f"{f}{c}": "O" for f in filas for c in columnas}

for idx in range(len(CARTELERA)):
    ASIENTOS[idx] = crear_mapa_asientos()

# -----------------------------
# Utilidades y validaciones
# -----------------------------

def validar_nombre(texto, etiqueta="Nombre"):
    errores = []
    if not isinstance(texto, str) or not texto.strip():
        errores.append(f"{etiqueta}: no puede estar vacío.")
    else:
        t = texto.strip()
        if len(t) < 3:
            errores.append(f"{etiqueta}: debe tener al menos 3 letras.")
        if any(ch.isdigit() for ch in t):
            errores.append(f"{etiqueta}: no debe contener números.")
    return errores

def validar_documento(doc):
    errores = []
    if not isinstance(doc, str) or not doc.strip():
        errores.append("Documento: no puede estar vacío.")
    else:
        d = doc.strip()
        if not d.isdigit():
            errores.append("Documento: solo debe contener números.")
        if not (3 <= len(d) <= 15):
            errores.append("Documento: longitud debe estar entre 3 y 15 dígitos.")
    return errores

def validar_vinculo(v):
    errores = []
    if v not in TIPOS_VINCULO_VALIDOS:
        errores.append(f"Tipo de vínculo inválido. Opciones: {', '.join(TIPOS_VINCULO_VALIDOS)}.")
    return errores

def print_errores(errores):
    # Muestra todos los errores de forma clara y secuencial
    print("\n[Errores encontrados]")
    for i, e in enumerate(errores, 1):
        print(f"  {i}. {e}")
    print()

def exportar_csv_usuarios(ruta="usuarios.csv"):
    campos = ["documento", "nombre", "apellido", "vinculo"]
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for doc, u in USUARIOS.items():
            w.writerow({
                "documento": doc,
                "nombre": u["nombre"],
                "apellido": u["apellido"],
                "vinculo": u["vinculo"],

            })

def exportar_csv_reservas(ruta="reservas.csv"):
    campos = ["documento", "pelicula", "dia", "hora", "asiento", "valor", "fecha"]
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for r in RESERVAS:
            func = CARTELERA[r["idx_funcion"]]
            w.writerow({
                "documento": r["documento"],
                "pelicula": func["pelicula"],
                "dia": func["dia"],
                "hora": func["hora"],
                "asiento": r["asiento"],
                "valor": r["valor"],
                "fecha": r["fecha"],
            })

def imprimir_mapa_asientos(idx_funcion):
    # Imprime un mapa similar al del enunciado, marcando "O" libres y "X" ocupados
    print("\nCINEMA UDEA (O Disponible) (X Ocupado)")
    mapa = ASIENTOS[idx_funcion]
    filas = [chr(ord('A') + i) for i in range(11)]
    columnas = list(range(1, 12))  # 1..11
    header = "  " + " ".join([f"{c:>3}" for c in columnas])
    print(header)
    for f in filas:
        fila_str = f"{f} " + " ".join([f"{mapa[f+str(c)]:>3}" for c in columnas])
        print(fila_str)
    print()

def seleccionar_funcion():
    # Lista funciones con índice y retorna el índice elegido
    print("\n[Funciones del fin de semana]")
    for i, fun in enumerate(CARTELERA):
        disp = sum(1 for estado in ASIENTOS[i].values() if estado == "O")
        print(f"  {i}. {fun['dia']} {fun['hora']} - {fun['pelicula']} | Disponibles: {disp}")
    while True:
        val = input("Ingrese el número de la función: ").strip()
        if val.isdigit():
            i = int(val)
            if 0 <= i < len(CARTELERA):
                return i
        print("Entrada inválida. Intente de nuevo.")

def solicitar_asiento(idx_funcion):
    imprimir_mapa_asientos(idx_funcion)
    while True:
        asiento = input("Seleccione asiento (ejemplo A1, B10, K11): ").strip().upper()
        if len(asiento) >= 2 and asiento[0].isalpha():
            fila = asiento[0]
            col = asiento[1:]
            if fila in [chr(ord('A') + i) for i in range(11)] and col.isdigit():
                col = int(col)
                if 1 <= col <= 11:
                    clave = f"{fila}{col}"
                    estado = ASIENTOS[idx_funcion][clave]
                    if estado == "O":
                        return clave
                    else:
                        print("Ese asiento está ocupado (X). Elige otro.")
                        continue
        print("Formato de asiento inválido. Usa letra A-K y número 1-11 (ejemplo: C7).")

def confirmar_compra(documento, idx_funcion, asiento):
    vinculo = USUARIOS[documento]["vinculo"]
    valor = TARIFAS[vinculo]
    
    # Obtener la hora actual en la zona horaria de Colombia
    zona_horaria_colombia = pytz.timezone('America/Bogota')
    fecha_hora_colombia = datetime.now(zona_horaria_colombia)
    fecha = fecha_hora_colombia.strftime("%Y-%m-%d %H:%M:%S")

    func = CARTELERA[idx_funcion]

    # Cambiar estado asiento
    ASIENTOS[idx_funcion][asiento] = "X"
    RESERVAS.append({
        "documento": documento,
        "idx_funcion": idx_funcion,
        "asiento": asiento,
        "valor": valor,
        "fecha": fecha,
    })

    # Factura simple
    print("\n[Factura de compra]")
    print(f"  Usuario: {documento} ({USUARIOS[documento]['nombre']} {USUARIOS[documento]['apellido']})")
    print(f"  Película: {func['pelicula']}")
    print(f"  Función: {func['dia']} {func['hora']}")
    print(f"  Asiento: {asiento}")
    print(f"  Vínculo: {vinculo}")
    print(f"  Valor: ${valor}")
    print(f"  Fecha: {fecha}\n")

def cancelar_reserva(documento):
    reservas_usuario = [r for r in RESERVAS if r["documento"] == documento]
    if not reservas_usuario:
        print("\nNo tienes reservas activas. ¿Deseas hacer una reserva? Volviendo al menú...\n")
        return

    # Listar reservas del usuario
    print("\n[Tus reservas]")
    for i, r in enumerate(reservas_usuario):
        func = CARTELERA[r["idx_funcion"]]
        print(f"  {i}. {func['pelicula']} | {func['dia']} {func['hora']} | Asiento: {r['asiento']} | ${r['valor']}")

    while True:
        val = input("Ingresa el número de la reserva a cancelar: ").strip()
        if val.isdigit():
            i = int(val)
            if 0 <= i < len(reservas_usuario):
                reserva = reservas_usuario[i]
                # Liberar asiento
                ASIENTOS[reserva["idx_funcion"]][reserva["asiento"]] = "O"
                # Remover de RESERVAS (por índice global)
                idx_global = RESERVAS.index(reserva)
                RESERVAS.pop(idx_global)
                print("\nReserva cancelada. El asiento volvió a estar disponible (O).\n")
                return
        print("Entrada inválida. Intenta de nuevo.")

def registrar_usuario():
    print("\n[Registro de Usuario] Paso a paso")
    nombre = input("1) Ingresa tu nombre: ").strip()
    apellido = input("2) Ingresa tu apellido: ").strip()
    documento = input("3) Ingresa tu documento (solo números, 3-15 dígitos): ").strip()

    print("\nTipos de vínculo disponibles:")
    for i, v in enumerate(TIPOS_VINCULO_VALIDOS, 1):
        print(f"  {i}. {v} - ${TARIFAS[v]}")

    tipo_op = input(f"4) Selecciona el tipo de vínculo por número (1-{len(TIPOS_VINCULO_VALIDOS)}): ").strip()

    errores = []
    errores += validar_nombre(nombre, "Nombre")
    errores += validar_nombre(apellido, "Apellido")
    errores += validar_documento(documento)

    # Validar la entrada numerica para el tipo de vinculo
    if not tipo_op.isdigit() or not (1 <= int(tipo_op) <= len(TIPOS_VINCULO_VALIDOS)):
        errores.append(f"Selección de vínculo inválida. Debe ser un número entre 1 y {len(TIPOS_VINCULO_VALIDOS)}.")

    if errores:
        print_errores(errores)
        print("Vuelve a intentarlo siguiendo las indicaciones. No se guardó el registro.\n")
        return

    # Convertir la entrada numerica a la cadena real del tipo de vinculo
    tipo_sel = TIPOS_VINCULO_VALIDOS[int(tipo_op) - 1]

    if documento in USUARIOS:
        print("\nYa existe un usuario con ese documento. Usa otro documento o inicia sesión.\n")
        return

    USUARIOS[documento] = {
        "nombre": nombre.strip(),
        "apellido": apellido.strip(),
        "vinculo": tipo_sel,
    }
    print("\nUsuario registrado correctamente.\n")
    exportar_csv_usuarios()

def registrar_reserva():
    print("\n[Registrar Reserva] Paso a paso")
    documento = input("Primero, ingresa tu documento para validar que estás registrado: ").strip()
    doc_err = validar_documento(documento)
    if doc_err:
        print_errores(doc_err)
        return
    if documento not in USUARIOS:
        print("\nNo estás registrado. Regístrate antes de reservar.\n")
        return

    idx_funcion = seleccionar_funcion()
    asiento = solicitar_asiento(idx_funcion)
    confirmar_compra(documento, idx_funcion, asiento)
    exportar_csv_reservas()

def consultar_funciones():
    print("\n[CARTELERA DE CINE UdeA]")
    print(f"Total de funciones programadas: {len(CARTELERA)}")

    # Group functions by movie title
    funciones_por_pelicula = {}
    for i, fun in enumerate(CARTELERA):
        pelicula = fun["pelicula"]
        if pelicula not in funciones_por_pelicula:
            funciones_por_pelicula[pelicula] = []
        funciones_por_pelicula[pelicula].append({"index": i, "data": fun})

    print(f"Películas en cartelera: {len(funciones_por_pelicula)}")
    print("\n[HORARIOS Y DISPONIBILIDAD]")

    for pelicula, funciones in sorted(funciones_por_pelicula.items()):
        print(f"\n--- Película: {pelicula} ---")
        for f_info in funciones:
            i = f_info["index"]
            fun = f_info["data"]
            disp = sum(1 for estado in ASIENTOS[i].values() if estado == "O")
            print(f"  [{i}] {fun['dia']} {fun['hora']} | Asientos disponibles: {disp}")
    print()

def admin_login():
    # Usuarios y contraseñas de administrador
    admins = {"admin": "admin123", "po_udea": "cinema2025"}
    print("\n[Ingreso Administrador]")
    user = input("Usuario: ").strip()
    pwd = input("Contraseña: ").strip()
    if user in admins and admins[user] == pwd:
        admin_menu()
    else:
        print("\nCredenciales inválidas.\n")

def admin_menu():
    while True:
        print("\n[Menú administrador]")
        print("  1. Total de reservas registradas")
        print("  2. Total de tiquetes vendidos")
        print("  3. Total pago realizado")
        print("  4. Promedio por venta diario del cine ")
        print("  5. Lista de usuarios")
        print("  6. Usuario con mayor y menor cantidad de reservas")
        print("  7. Exportar CSV (usuarios y reservas)")
        print("  0. Volver")
        op = input("Elige una opción: ").strip()

        if op == "1":
            print(f"\nTotal de reservas registradas: {len(RESERVAS)}\n")
        elif op == "2":
            print(f"\nTotal de tiquetes vendidos: {len(RESERVAS)}\n")
        elif op == "3":
            total_pago = sum(r["valor"] for r in RESERVAS)
            print(f"\nTotal pago realizado: ${total_pago}\n")
        elif op == "4":
            # Promedio por día (agrupamos por fecha YYYY-MM-DD)
            por_dia = {}
            for r in RESERVAS:
                dia = r["fecha"].split(" ")[0]
                por_dia.setdefault(dia, []).append(r)
            if por_dia:
                proms = [sum(rr["valor"] for rr in lst) / len(lst) for lst in por_dia.values()]
                promedio_global = sum(proms) / len(proms)
                print(f"\nPromedio por venta diario del cine: ${promedio_global:.2f}\n")
            else:
                print("\nNo hay reservas para calcular promedio.\n")
        elif op == "5":
            if not USUARIOS:
                print("\nNo hay usuarios registrados.\n")
            else:
                print("\n[Usuarios]")
                for doc, u in USUARIOS.items():
                    print(f"  {doc} - {u['nombre']} {u['apellido']} ({u['vinculo']})")
                print()
        elif op == "6":
            if not RESERVAS:
                print("\nNo hay reservas registradas.\n")
            else:
                conteo = {}
                for r in RESERVAS:
                    conteo[r["documento"]] = conteo.get(r["documento"], 0) + 1
                # max y min
                doc_max = max(conteo, key=conteo.get)
                doc_min = min(conteo, key=conteo.get)
                u_max = USUARIOS.get(doc_max, {"nombre": "?", "apellido": "?"})
                u_min = USUARIOS.get(doc_min, {"nombre": "?", "apellido": "?"})
                print(f"\nMayor reservas: {doc_max} - {u_max['nombre']} {u_max['apellido']} ({conteo[doc_max]})\n")
                print(f"Menor reservas: {doc_min} - {u_min['nombre']} {u_min['apellido']} ({conteo[doc_min]})\n")
        elif op == "7":
            exportar_csv_usuarios()
            exportar_csv_reservas()
            print("\nCSV exportados (usuarios.csv y reservas.csv).\n")
        elif op == "0":
            return
        else:
            print("Opción inválida.")

# -----------------------------
# Menú principal
# -----------------------------

def menu_principal():
    print("\nCINEMA UDEA")
    print("Bienvenido al Cinema UdeA Luces, Camara y UdeA")
    while True:
        print("\n1. Registrar Usuario")
        print("2. Registrar Reserva")
        print("3. Cancelar Reserva")
        print("4. Consultar Funciones Fin de Semana")
        print("5. Administrador")
        print("6. Salir")
        op = input("\nSelecciona una opción: ").strip()

        if op == "1":
            registrar_usuario()
        elif op == "2":
            registrar_reserva()
        elif op == "3":
            documento = input("Ingresa tu documento para cancelar: ").strip()
            doc_err = validar_documento(documento)
            if doc_err:
                print_errores(doc_err)
            elif documento not in USUARIOS:
                print("\nNo estás registrado. Regístrate antes de cancelar.\n")
            else:
                cancelar_reserva(documento)
        elif op == "4":
            consultar_funciones()
        elif op == "5":
            admin_login()
        elif op == "6":
            print("\nGracias por usar Cinema UdeA. Hasta pronto.\n")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
