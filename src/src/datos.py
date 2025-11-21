# -------------------------
# BASE DE DATOS TEMPORAL
# -------------------------

usuarios = []      # Lista de diccionarios con datos del usuario
reservas = []      # Lista de reservas hechas

# Creación de sala de 11 columnas x 10 filas (121 sillas)
# "O" = disponible | "X" = ocupado

sala = [
    ['O'] * 11 for _ in range(11)
]

# Películas de ejemplo (el profe dará la definitiva)
funciones = [
    {"dia": "Sábado", "hora": "3:00 PM", "nombre": "Interestelar"},
    {"dia": "Sábado", "hora": "6:00 PM", "nombre": "Interstate 99"},
    {"dia": "Domingo", "hora": "2:00 PM", "nombre": "Cazafantasmas"},
]
