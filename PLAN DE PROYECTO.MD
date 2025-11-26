# 🎬 Plan de Proyecto –   

## 1. Introducción  
 LUCES-CÁMARA, UDEA es un sistema desarrollado en Python desde consola, diseñado para gestionar de forma eficiente un espacio cinematográfico dentro de la Universidad de Antioquia. Este proyecto busca ofrecer a la comunidad universitaria (estudiantes, docentes, administrativos, oficiales internos y público externo) una experiencia organizada y accesible para reservar asientos, consultar funciones, generar facturas y visualizar reportes administrativos. 

## 2. Justificación  
El desarrollo del proyecto “Cine, Cámaras y UdeA” surge de la necesidad de aplicar los conceptos fundamentales vistos en el curso de Algoritmia y Programación mediante la construcción de un sistema funcional, modular y completamente ejecutable. Crear un software que gestione usuarios, reservas y funciones de cine permite integrar de manera práctica temas como estructuras de datos, modularización, validación de información y manejo de flujos lógicos dentro de un programa real.

Además, este proyecto nos permitió simular un caso cercano a situaciones del mundo laboral, donde es necesario organizar el código de forma ordenada, trabajar con diferentes módulos, garantizar la claridad del sistema, y documentar el proceso de manera profesional. Elegimos este enfoque porque representa un escenario cotidiano y entendible para cualquier usuario: un cine, con su sistema básico de reservas y administración.

La implementación en Python y la organización del repositorio en GitHub se justifican porque ambas herramientas son ampliamente utilizadas en la industria del software. Python facilita el aprendizaje de estructuras lógicas, lectura del código y modularidad. GitHub, por su parte, nos permitió gestionar versiones, mantener ordenado el proyecto, y comprender cómo funciona un entorno de desarrollo más cercano a lo profesional, aun cuando al inicio fue un reto para nosotros.

En conclusión, este proyecto se justifica tanto desde el punto de vista académico como práctico: consolida las bases de la programación, promueve el trabajo en equipo, fortalece habilidades técnicas esenciales y ofrece una solución funcional a un problema realista, demostrando el aprendizaje adquirido a lo largo del curso.

## 3. Objetivos  
### Objetivo general  
Diseñar y desarrollar un programa de consola que permita gestionar las operaciones básicas de un cine universitario, incluyendo registro de usuarios, reservas, cancelaciones, facturación y reportes administrativos, garantizando una interacción amigable y clara para el usuario.  

### Objetivos específicos  
- Diseñar un programa  que funcione desde consola y permita gestionar un cine universitario de forma amigable para el usuario.
-	Poder registrar usuarios con validaciones estrictas en nombre, apellido, documento y tipo de vínculo (estudiante, docente, etc.).
-	Gestionar reservas de asientos para funciones de cine, mostrando visualmente la disponibilidad y ocupación de sillas.
-	Cancelar reservas activas, validando que el usuario tenga una reserva vigente y actualizando el estado del asiento.
-	Consultar funciones del fin de semana, mostrando cartelera, horarios y disponibilidad de sillas por película.
-	Imprime facturas y confirma compras de tiquetes, incluyendo el valor según el tipo de usuario.
-	Exportar datos a archivos CSV, como respaldo de información administrativa y operativa del cine.
-	Desarrollar un módulo de administración con informes como total de reservas, ingresos, usuarios frecuentes, etc.
-	Organizar el proyecto en GitHub, incluyendo carpetas específicas (src, doc) y documentación en Markdown.


 

## 4. Alcance  
- **Incluye:**  
- Sala de cine fisica en el campus universitario con capacidad para 121 espectadores
- Proyección de exposiciones y proyectos presentados por las facultades
- Presentación de otros eventos programados por la universidad.
 

- **No incluye:**  
 - Actividades fuera de nuestro enfoque cinemático

## 🎯5. Metas 

Las metas del proyecto **Cine, Cámaras y UdeA** se diseñaron para lograr un sistema funcional, organizado y útil tanto para el usuario común como para la administración. Estas metas guiaron el desarrollo técnico, la estructura del repositorio y la implementación del código.

---

##  **1. Meta general**

Desarrollar un sistema interactivo en consola que permita gestionar un cine universitario mediante operaciones como registro de usuarios, reservas, cancelaciones, consulta de funciones y acceso administrativo, aplicando los fundamentos de programación aprendidos durante el curso.

---

##  **2. Metas específicas**

### ✔️ **2.1 Crear un sistema modular**
Implementar el proyecto utilizando diferentes módulos (`main.py`, `usuarios.py`, `reservas.py`, `funciones.py`, `admin.py`, `datos.py`) para garantizar orden, claridad y facilidad de mantenimiento.

---

### ✔️ **2.2 Registrar usuarios correctamente**
Desarrollar un módulo capaz de validar nombres, apellidos, documentos y tipos de usuario, asegurando que la información almacenada sea correcta y consistente.

---

### ✔️ **2.3 Gestionar reservas y cancelaciones**
Permitir al usuario seleccionar asientos dentro de la matriz del cine, validar disponibilidad, registrar reservas, cancelarlas y actualizar la sala en tiempo real.

---

### ✔️ **2.4 Consultar la programación del fin de semana**
Mostrar de manera clara y organizada las películas disponibles, simulando la cartelera de un cine real.

---

### ✔️ **2.5 Crear un panel administrativo**
Implementar funciones que permitan visualizar estadísticas como:
- Número total de reservas  
- Cantidad de usuarios  
- Total recaudado 💰  
- Usuarios con más y menos reservas  
- Listado general de usuarios  

Esto permite simular el trabajo administrativo de un cine real.

---

### ✔️ **2.6 Organizar el repositorio en GitHub**
Estructurar el proyecto con carpetas claras:
- `/src` → código fuente  
- `/doc` → documentos del proyecto  
- Archivos de requisitos, visión, planeación y manual de usuario  

Garantizando buenas prácticas de documentación y entrega.

---

### ✔️ **2.7 Elaborar documentación clara**
Desarrollar manuales, visión, justificación, plan de proyecto, metas, versionado y README para que cualquier persona pueda entender cómo usar o modificar el sistema.

---

##  **2.8 Trabajar colaborativamente**
Fomentar el trabajo en equipo mediante reuniones, asignación de responsabilidades y uso básico de GitHub para manejar versiones del proyecto.

---

##  **2.9 Presentar un producto funcional y sustentable**
Entregar un sistema que pueda ser ejecutado sin errores, con menús claros, navegación sencilla, y que cumpla con todos los requerimientos planteados por el docente.

---


## 6. Beneficiarios  
- **Directos:** estudiantes, docentes y personal administrativo de la Universidad de Antioquia.  
- **Indirectos:** público externo invitado en actividades especiales.  

## 7. Presupuesto y Herramientas 
- **Presupuesto:** Equipo de trabajo de 4 estudiantes, de los cuales cada uno invertira un total de 70  horas en un periodo de 2 Meses , las cuales seran dedicadas a la practica y ejecución del proyecto. Para tener un total de 280 horas las cuales seran reconocidas como tiempo de formación y tienen un valor equivalente de 2 SMLV por integrante (no són en dinero real) 

  **Herramientas tecnologicas:** Para la ejecucion de ested proyecto y con la finalidad de ser un programa agradable para el usuario se han utilizado las siguientes herramientas; Gogle Colab,Python 3, Markdown, Git y Github, licencia MIT/ Creative Commons

## 📊 **Presupuesto del Proyecto**

El presente presupuesto contempla el tiempo de trabajo, dedicación académica y herramientas tecnológicas utilizadas durante el desarrollo del sistema **Cine, Cámaras y UdeA**.  
Este presupuesto NO representa dinero real, sino una valorización académica equivalente, según los lineamientos del curso.

---

### 🧑‍🤝‍🧑 **Equipo de Trabajo**

| Integrante                         | Rol / Participación |
|------------------------------------|----------------------|
| **Isabella Londoño**               | Desarrollo – Documentación |
| **Julián Alberto Gómez Agudelo**   | Análisis – Apoyo técnico |
| **Michael Hincapié Alzate**        | Programación – Pruebas |
| **Anderson Arboleda Duque**        | Coordinación – Gestión |

---

### ⏳ **Tiempo de Dedicación**

Cada integrante invirtió:

- **70 horas de trabajo**
- Distribuidas en un periodo de **2 meses**
- Para un total acumulado de:

**70 horas × 4 integrantes = 280 horas invertidas**

Este tiempo corresponde a actividades como:

- Diseño del sistema  
- Escritura de código  
- Pruebas del programa  
- Revisión grupal  
- Documentación  
- Subida del proyecto a GitHub  

---

### 💰 **Valoración Académica del Trabajo**

Aunque NO es dinero real, se estima un valor académico equivalente a:

| Integrante | Horas trabajadas | Valor simbólico (equivalente) |
|-----------|------------------|--------------------------------|
| Isabella  | 70 h             | **2 SMLV** |
| Julián    | 70 h             | **2 SMLV** |
| Michael   | 70 h             | **2 SMLV** |
| Anderson  | 70 h             | **2 SMLV** |

> 🔹 *Esta valorización se usa únicamente con fines educativos, como reconocimiento del esfuerzo realizado en el desarrollo del proyecto.*

---

### 🖥️ **Herramientas Tecnológicas Utilizadas**

| Herramienta            | Uso Principal |
|------------------------|---------------|
| **Google Colab**       | Desarrollo del código en Python |
| **Python 3**           | Lenguaje de programación principal |
| **Markdown**           | Documentación técnica del proyecto |
| **Git**                | Control de versiones |
| **GitHub**             | Gestión del repositorio y entregas |
| **MIT / Creative Commons** | Licencias abiertas utilizadas para el despliegue y versiones |

---

### 📌 **Resumen del Presupuesto**

| Concepto                     | Cantidad          |
|------------------------------|--------------------|
| Integrantes                  | **4**              |
| Horas totales trabajadas     | **280 horas**      |
| Valor simbólico por integrante | **2 SMLV**       |
| Total SMLV simbólicos        | **8 SMLV**         |
| Herramientas utilizadas      | **5 herramientas tecnológicas** |

---

### ✔️ **Conclusión del Presupuesto**

El proyecto fue desarrollado bajo una estructura colaborativa, con una inversión total de **280 horas** de trabajo académico, apoyado por herramientas gratuitas y de código abierto.  
La valoración del proyecto en SMLV es únicamente representativa y se utiliza para efectos formativos dentro de la asignatura.


## 8. Evaluación y seguimiento  
Indicadores de éxito:  
- Número de proyecciones realizadas y asistencia promedio.  
- Cantidad de producciones estudiantiles exhibidas.  
- Empleos y prácticas generadas para estudiantes.  
- Nivel de satisfacción de los asistentes y comunidad universitaria.  

## 9. Conclusión  
LUCES-CÁMARA, UDEA  se convertira en un modelo funcional de gestión cultural universitaria, que pueda ser escalado o adaptado a otros espacios institucionales, sera un programa con una experiencia muy agradable para el usuario en el momento se realizar sus compras y reservas, ademas va a ser una gran oportunidad para los jovenes ir conviviendo con el mundo tecnologico, tambien servira como un apoyo para aquellos estudiantes que quieran realizar sus practicas universitarias.
