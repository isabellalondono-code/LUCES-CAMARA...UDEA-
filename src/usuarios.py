usuarios = []

def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    nombre = input("Nombre: ")
    correo = input("Correo: ")

    usuario = {
        "nombre": nombre,
        "correo": correo
    }

    usuarios.append(usuario)
    print("Usuario registrado con éxito.")
