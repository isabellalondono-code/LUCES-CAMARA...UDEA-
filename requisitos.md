---

## Especificación de Requisitos “LUCES-CAMARA...UDEA”

Este documento describe los requisitos funcionales y no funcionales del sistema de gestión del Cine Universitario, desarrollado como proyecto académico para el curso de Algoritmia y Programación.
El sistema busca ofrecer una simulación de la gestión de un cine universitario mediante una interfaz de consola en Python, empleando conceptos básicos de programación estructurada y orientada a objetos.

---

## Objetivo general

Diseñar y desarrollar un programa de consola que permita gestionar las operaciones básicas de un cine universitario, incluyendo registro de usuarios, reservas, cancelaciones, facturación y reportes administrativos, garantizando una interacción amigable y clara para el usuario.

---

## Requisitos Funcionales (RF)

Los requisitos funcionales definen las acciones específicas que el sistema debe ejecutar para cumplir con los objetivos del proyecto.

| Código | Requisito | Propósito pedagógico |
|--------|-----------|-----------------------|
| RF1 | Registrar usuarios | El sistema debe permitir registrar usuarios ingresando nombre, apellido, documento y tipo de vínculo (estudiante, docente, administrativo, oficial interno o público externo). |
| RF2 | Validar datos de usuario | El sistema debe verificar que el nombre y apellido tengan mínimo tres letras y no incluyan números; el documento solo debe contener entre 3 y 15 dígitos numéricos. |
| RF3 | Mostrar menú principal	| El sistema debe desplegar un menú de opciones que permita al usuario navegar entre registrar, reservar, cancelar o consultar funciones. |
| RF4 | Consultar cartelera	| El usuario podrá visualizar la lista de películas disponibles para el próximo fin de semana, con información de día, hora y sillas disponibles. |
| RF5 | Registrar reserva	| Solo los usuarios registrados podrán realizar reservas. El sistema mostrará el mapa de asientos y permitirá seleccionar uno. |
| RF6 | Generar factura	| Después de la reserva, el sistema debe mostrar la confirmación del tiquete con los datos del usuario, película, tipo de vínculo y valor total. |
| RF7 | Cancelar reserva | Los usuarios podrán cancelar una reserva activa. El sistema validará la existencia de la reserva antes de permitir su cancelación. |
| RF8 | Control de asientos	| Cada vez que un usuario reserve o cancele, el sistema debe actualizar el estado del asiento en el mapa de ocupación. |
| RF9 | Acceso de administrador	| Debe existir un módulo protegido con usuario y contraseña para acceder a reportes administrativos. |
| RF10 | Reportes administrativos	| El módulo de administrador debe permitir visualizar el total de reservas, total de ingresos, promedio diario, lista de usuarios y el usuario con más y menos reservas.|
| RF11 | Finalizar sesión |	Al salir del sistema, se debe mostrar un mensaje de cierre y retornar al menú principal o finalizar la ejecución. |

---

## Requisitos No Funcionales (RNF)

Los requisitos no funcionales definen criterios de calidad, rendimiento y usabilidad que complementan el comportamiento del sistema.

| Código | Requisito | Aplicación en Colab |
|--------|-----------|---------------------|
| RNF1 | Usabilidad | La interfaz en consola debe ser clara, con mensajes descriptivos y opciones numeradas para facilitar la interacción. |
| RNF2 | Rendimiento | El tiempo de respuesta de las operaciones no debe superar los 2 segundos. |
| RNF3 | Seguridad básica |	Los datos ingresados no deben almacenarse de forma permanente ni incluir información sensible. |
| RNF4 | Portabilidad	| El programa debe ser ejecutable en cualquier entorno con Python (Google Colab, terminal o IDE). |
| RNF5 | Mantenibilidad |	El código debe estar modularizado y documentado con comentarios breves que expliquen la función de cada bloque. |
| RNF6 | Reusabilidad |	El código debe ser adaptable para futuras versiones o mejoras (por ejemplo, reserva múltiple o interfaz gráfica). |
| RNF7 | Claridad pedagógica | El programa debe ser entendible para estudiantes que inician en programación, evitando complejidad innecesaria. |
| RNF8 | Compatibilidad |	El programa debe funcionar correctamente en Google Colab, cumpliendo con los requerimientos del curso. |
| RNF9 | Accesibilidad | Debe utilizar un lenguaje simple, mensajes informativos y evitar tecnicismos. |
| RNF10 | Control de errores | El sistema debe validar entradas y mostrar mensajes adecuados cuando se detecten errores de ingreso o ejecución. |

---

## Observaciones finales

- El desarrollo se realizará en Python, con ejecución en Google Colab o consola local.

- Se prioriza la claridad, modularidad y comprensión sobre la complejidad técnica.

- La especificación podrá actualizarse según el avance del proyecto y los requerimientos del docente.
