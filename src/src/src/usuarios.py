from datos import usuarios

# -------------------------------------
# VALIDACIONES DE ENTRADA DEL USUARIO
# -------------------------------------

def validar_nombre(texto):
    """Valida que el nombre o apellido tenga solo letras y mínimo 3 caracteres."""
    if len(texto) < 3:
        return False
    if not texto.isalpha():
        return False
    return True


def validar_documento(doc):
    """Valida que el documento tenga solo números y entre 3 y 15 dígitos."""
    return doc.isdigit() and 3 <= len(doc) <= 15


# -------------------------------------
# REGISTRO DE USUARIOS
# -------------------------------------

def registrar_usuario():
    print("\n=== REGISTRO DE USUARIO ===")

    # NOMBRE
    nombre = input("Ingrese el nombre: ")
    while not validar_nombre(nombre):
        print("❌ Nombre inválido. Debe tener al menos 3 letras y no contener números.")
        nombre = input("Ingrese el nombre: ")

    # APELLIDO
    apellido = input("Ingrese el apellido: ")
    while not validar_nombre(apellido):
        print("❌ Apellido inválido. Debe tener al menos 3 letras y no contener números.")
        apellido = input("Ingrese el apellido: ")

    # DOCUMENTO
    documento = input("Ingrese el documento: ")
    while not validar_documento(documento):
        print("❌ El documento debe ser numérico y contener entre 3 y 15 dígitos.")
        documento = input("Ingrese el documento: ")

    # TIPO DE VÍNCULO
    print("\nTipos de usuario:")
    print("1. Estudiante ($7.500)")
    print("2. Docente ($10.000)")
    print("3. Administrativo ($8.500)")
    print("4. Oficial Interno ($7.000)")
    print("5. Público Externo ($15.000)")

    tipos = ["Estudiante", "Docente", "Administrativo", "Oficial Interno", "Público Externo"]
    precios = [7500, 10000, 8500, 7000, 15000]

    tipo_op = input("Seleccione el tipo (1-5): ")
    whil
