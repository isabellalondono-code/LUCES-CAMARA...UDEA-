from datos import funciones

def consultar_funciones():
    print("\n--- Funciones Disponibles ---")
    for f in funciones:
        print(f"ID: {f['id']} | {f['pelicula']} | {f['hora']} | {f['sala']}")
