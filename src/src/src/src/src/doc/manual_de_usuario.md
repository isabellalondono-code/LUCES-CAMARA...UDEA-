MANUAL DE USUARIO  “Cine, Cámaras y UdeA"

1. Introducción

El presente manual de usuario tiene como objetivo explicar de manera clara y sencilla el funcionamiento del programa de consola Cine, Cámaras y UdeA, desarrollado como proyecto final del curso Algoritmia y Programación.

El sistema permite:

Registrar usuarios

Realizar reservas de asientos

Cancelar reservas

Consultar funciones del fin de semana

Acceder al panel administrativo con reportes

Visualizar el estado de la sala de cine

Este manual está dirigido a cualquier persona que desee usar el programa sin conocimiento previo en programación.

2. Requisitos del Sistema

Para ejecutar el programa, se requieren los siguientes elementos:

Sistema operativo Windows, macOS o Linux

Python 3.8 o superior

Archivos del proyecto descargados desde GitHub

Consola o terminal para ejecutar el programa

3. Cómo ejecutar el programa

Descargar el repositorio desde GitHub

Botón verde Code → Download ZIP

Descomprimir la carpeta

Abrir una terminal o consola en la carpeta src
Ejemplo (Windows):

cd Downloads/LUCES-CAMARA-UDEA-main/src


Ejecutar el archivo principal:

python main.py


Al hacerlo, aparecerá el menú del cine.

4. Menú Principal

Al iniciar el programa verás:

========== CINE, CÁMARAS Y UDEA ==========
1. Registrar Usuario
2. Registrar Reserva
3. Cancelar Reserva
4. Consultar Funciones Fin de Semana
5. Administrador
6. Salir


Puedes ingresar a cualquier opción escribiendo el número correspondiente.
 5. Registrar Usuario

Esta opción permite registrar un usuario nuevo.
El sistema solicitará:

Nombre (solo letras, mínimo 3)

Apellido (solo letras, mínimo 3)

Documento (solo números entre 3 y 15 dígitos)

Tipo de usuario:

Estudiante

Docente

Administrativo

Oficial Interno

Público Externo

Cada tipo tiene un precio diferente del tiquete.

Si los datos son correctos, el sistema mostrará:

✔ Usuario registrado exitosamente.

6. Registrar Reserva

Para reservar un asiento:

Ingresa el documento del usuario

El sistema validará que el usuario esté registrado

Se mostrará la sala:

CINE, CÁMARAS Y UDEA  (O = Disponible / X = Ocupado)

   A  B  C  D  E  F  G  H  I  J  K
A  O  O  O  O  O  O  O  O  O  O  O
B  O  O  O  O  O  O  O  O  O  O  O
...


Seleccionas un asiento (Ejemplo: A5)

Si el asiento está disponible, se marcará como ocupado (X)

El sistema mostrará:

✔ Reserva realizada con éxito.
Asiento reservado: A5
Total a pagar: $7500

 7. Cancelar Reserva

Permite cancelar una reserva activa.

Ingresa el documento del usuario

El sistema mostrará sus reservas activas

Selecciona cuál deseas cancelar

El asiento será liberado (volverá a “O”)

Mensaje final:

✔ Reserva cancelada exitosamente.
 8. Consultar Funciones del Fin de Semana

Muestra la programación:

📅 Sábado | 🕒 3:00 PM | 🎬 Interestelar
📅 Sábado | 🕒 6:00 PM | 🎬 Interstate 99
📅 Domingo | 🕒 2:00 PM | 🎬 Cazafantasmas


Las funciones reales serán proporcionadas por el docente.

 9. Panel Administrativo

Accede con:

Usuario: admin

Contraseña: 1234

El menú incluye:

Total de reservas

Total de tiquetes vendidos

Total recaudado

Promedio por día

Lista de usuarios

Usuario con más reservas

Usuario con menos reservas

Ejemplo de salida:

💰 Total recaudado: $32000

 10. Finalizar el Programa

En el menú principal, selecciona:

6. Salir


Mensaje final:

Gracias por usar Cine, Cámaras y UdeA. ¡Hasta luego!

🎉 11. Contacto del Equipo

Proyecto desarrollado por:
Julian 

Isabella Londoño
Michael Hincapié
Anderson Arboleda

Facultad de Ingeniería – Universidad de Antioquia
Curso: Algoritmia y Programación 2025-2
