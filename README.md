# DATAFILE-SOLUTION
                                                                #INFORMACION

## INTEGRANTES

**- MARIA CAMILA CASTRO ESTRADA :** *"Hola, soy estudiante del programa Ingenieria Industrial virtual regiones de la sede Amalfi, trabajo como supernumeraria de la Registraduria Municipal de Amalfi, hago parte de una corporación sin animo de lucro llamada Mundo Al Revés, me gusta el arte y tengo 24 años."*
- Programa: Ingenieria Industrial Virtual Regiones.
- Habilidades: Entre mis habilidades destaco la recolección y organización de información, me interesa aprender métodos que ayuden a optimizar procesos y mejorar la manera en que se realizan las tareas.
- Fortalezas: Me considero una persona con buena disposición para el trabajo en equipo, soy buena para revisar, editar y reorganizar, me adapto bien a los cambios, procuro ser de ayuda, soy proactiva, considero que mis intereses académicos y personales me sirven para ampliar mi vision y ayudar en diversas situaciones.
  
  
**- LINA MARCELA DUQUE GIRALDO:** *"Tengo 28 años, estoy en el programa de ingeniería industrial virtual (sede Medellín) y trabajo en la alcaldía de Rionegro por carrera administrativa."*
- Programa: Ingenieria Industrial Virtual Medellin.
- Habilidades: Entre mis habilidades se destacan el análisis y resolución de problemas.  Además, cuento con pensamiento lógico y capacidad de aprendizaje, lo que me permite adaptarme al uso de herramientas tecnológicas necesarias para el desarrollo del software.
- Fortalezas: Me considero una persona proactiva, con iniciativa para asumir responsabilidades y aportar al desarrollo del proyecto. Además, me destaco por mi perseverancia para lograr los objetivos propuestos.
  


---

                                                                      # DISEÑO

## NOMBRE DEL PROYECTO

# DATAFILE-SOLUTION

![LOGO](https://github.com/user-attachments/assets/cd61d640-4f4c-4cfe-a765-f5bbbffa2427)
---
DATAFILE-SOLUTION © 2026 por MARIA CAMILA CASTRO ESTRADA, LINA MARCELA DUQUE GIRALDO está bajo licencia Creative Commons Attribution 4.0 International (CC-BY 4.0).
Se permite el uso, distribución y modificación del contenido en cualquier medio o formato, siempre que se otorgue el debido crédito a los autores del proyecto.

---

                                                                # REPORTE DE VISION
                                                                
## DESCRIPCION GENERAL

El proyecto “Datafile solution” consiste en el desarrollo de un sistema para la gestión de préstamos de objetos, diseñado para ayudar a Michael Jackson Gamboa a llevar un control organizado de los artículos que presta.

El software propuesto es un sistema de gestión de préstamos desarrollado en Python, diseñado para controlar de manera estructurada la información relacionada con usuarios, objetos y movimientos de préstamo y devolución. Su funcionamiento se realizará a través de una interfaz de consola amigable, que permita una interacción simple, ordenada y eficiente con el sistema.
Esta solución está pensada para contextos en los que sea necesario administrar recursos prestables de forma organizada, sustituyendo registros manuales por un entorno digital con mayor claridad operativa. El programa integrará funciones de registro, consulta, actualización y control de la información, permitiendo centralizar los datos dentro de una misma herramienta.

## BENEFICIOS

**Trazabilidad de cada préstamo**
Entre los principales beneficios del software se encuentra una organización eficiente de la información, el sistema permitirá conocer con precisión quién solicitó un objeto, en qué fecha lo recibió.

**Reducción de pérdidas por olvido o mala gestión**
Al mantener actualizada la información de préstamos y devoluciones, el software disminuye el riesgo de extravío de objetos, permitiendo la minimización de errores al recordar préstamos.

**Identificación de usuarios con mayor nivel de cumplimiento**
Esto aporta información útil para tomar decisiones sobre futuros préstamos.

**Detección de ítems con alta rotación**
El software permitirá identificar cuáles objetos son prestados con mayor frecuencia para reconocer qué recursos son más demandados y cuáles requieren mayor disponibilidad, mantenimiento o reposición.

**Apoyo en la toma de decisiones administrativas**
La información almacenada puede servir para decidir si conviene adquirir más unidades de ciertos objetos, restringir algunos préstamos, el propósito principal es organizar y optimizar los objetos que se prestan.

**Disminución del tiempo de búsqueda de información**
En lugar de revisar apuntes, archivos dispersos o registros manuales, el sistema permitirá consultar rápidamente el estado de un préstamo, esto mejora la eficiencia operativa y ahorra tiempo.

**Fortalecimiento de la cultura de responsabilidad**
El uso del sistema promueve en los usuarios una mayor conciencia sobre el cuidado de los objetos prestados y el cumplimiento de los tiempos de devolución, ya que cada operación queda registrada y asociada a un responsable.

**Base para futuras automatizaciones**
La creación de este software puede servir como punto de partida para en versiones futuras agregar alertas automáticas, reportes estadísticos, filtros, etc.

---

                                                               # ESPECIFICACION DE REQUISITOS
                                                               
## REQUISITOS FUNCIONALES

**Gestión de amigos**
•	El sistema debe permitir registrar amigos con información básica (nombre, teléfono, correo).
•	El sistema debe permitir consultar la lista de amigos registrados.
•	El sistema debe permitir actualizar y eliminar información de amigos.

**Gestión de inventario**
•	El sistema debe permitir registrar objetos con nombre y precio de adquisición.
•	El sistema debe indicar si un objeto está disponible o prestado.
•	El sistema debe permitir consultar el inventario de objetos.

**Gestión de préstamos**
•	El sistema debe permitir registrar un préstamo asociando un amigo, un objeto y la fecha.
•	El sistema debe impedir prestar objetos que no estén disponibles.
•	El sistema debe almacenar el historial de préstamos.

**Gestión de devoluciones**
•	El sistema debe permitir registrar la devolución de un objeto.
•	El sistema debe actualizar el estado del objeto a disponible.
•	El sistema debe registrar la fecha de devolución.

**Notificaciones y alertas**
•	El sistema debe generar un recordatorio automático cuando un préstamo supere los 20 días.
•	El sistema debe notificar al usuario sobre préstamos pendientes.

**Facturación**
•	El sistema debe generar una factura de venta cuando un préstamo supere los 30 días sin devolución.
•	La factura debe incluir el nombre del amigo, el objeto y el precio.

**Certificados**
•	El sistema debe generar un certificado de devolución cuando un objeto sea retornado.
•	El certificado debe incluir datos del amigo, objeto y fecha de devolución.


## REQUISITOS NO FUNCIONALES

**Usabilidad**
El sistema debe contar con una interfaz sencilla e intuitiva basada en menú para que el usuario pueda interactuar sin conocimientos técnicos avanzados.

**Rendimiento**
El sistema debe responder a las acciones del usuario de manera inmediata y el procesamiento de datos debe ser eficiente para listas pequeñas y medianas.

**Fiabilidad**
El sistema debe garantizar la correcta gestión de la información sin pérdida de datos durante su ejecución.

**Seguridad**
El sistema debe validar los datos ingresados por el usuario y debe evitar registros incompletos o incorrectos.

**Mantenibilidad**
El código debe estar organizado y documentado para facilitar futuras mejoras y permitir agregar nuevas funcionalidades sin afectar el funcionamiento actual.

---

                                                              # DIAGRAMA DE GANTT Y PRESUPUESTO
Nota aclaratoria: Los documentos sobre el diagrama y el presupuesto, están subidos al repositorio en version jpg, pdf y archivo excel, para una mejor visualizacion.                                                                                       
---

## 7. Plan de Versionado

| Versión | Fecha | Autor | Descripción |
|---------|-------|-------|-------------|
| v0.0.1 | Semana 14 | linaduque1 | Estructura base y menú principal. Se desarrolló la estructura de archivos requeridos para el proyecto y se implementó el menú principal. |
| v0.0.2 | Semana 15 | linaduque1 | Registro de usuarios e ítems. Se crean las funciones y validaciones para registrar usuarios e ítems. |
| v0.0.3 | Semana 15 | mariacastroe1 | Préstamos y admin creados. Se crean y validan las funciones para registrar préstamos y se crean los usuarios administradores. |
| v0.0.4 | Semana 16 | mariacastroe1 | Aplicación funcional sin reportes PDF. La aplicación guarda usuarios, ítems y préstamos en CSV y genera ventas automáticas para los préstamos de más de 30 días. |
| v0.0.5 | Semana 16 | linaduque1 | Versión final completa. Se agregan reportes PDF para facturas y certificados, persistencia completa con carga de CSV al inicio, fecha manual en préstamos y manual de usuario. |

### Historial de releases

- **[v0.0.5 — Versión final](https://github.com/mariacastroe1/DATAFILE-SOLUTION/releases/latest)** *(Latest)*
  Versión completa con PDF, persistencia de datos y manual de usuario.

- **[v0.0.4 — Aplicación funcional sin reportes PDF](https://github.com/mariacastroe1/DATAFILE-SOLUTION/releases/tag/v0.0.4)**
  La aplicación guarda usuarios, ítems y préstamos en CSV y genera ventas automáticas para préstamos de más de 30 días.

- **[v0.0.3 — Préstamos y admin creados](https://github.com/mariacastroe1/DATAFILE-SOLUTION/releases/tag/v0.0.3)**
  Se crean y validan las funciones para registrar préstamos y se crean los usuarios administradores.

- **[v0.0.2 — Registro de usuarios e ítems](https://github.com/mariacastroe1/DATAFILE-SOLUTION/releases/tag/v0.0.2)**
  Se crean las funciones y validaciones para registrar usuarios e ítems.

- **[v0.0.1 — Estructura base y menú principal](https://github.com/mariacastroe1/DATAFILE-SOLUTION/releases/tag/v0.0.1)**
  Se desarrolló la estructura de archivos requeridos para el proyecto y se implementó el menú principal.


### Observaciones 

Se colocó el plan versionado desde la semana 14 debido a que este se genera a partir del versionamiento, no se coloca desde el inicio debido al desconocimiento previo para guardar el versionamiento en Github, sin embargo se guarda registro previo en las actas de reunión.

---


### Guía de Instalación


### Requisitos

- Python 3.10 o superior
- Librería `reportlab` para generación de PDF

### Instalación en Windows

Abrir una terminal (cmd o PowerShell) en la carpeta del proyecto y ejecutar:

```
pip install reportlab
```

Si no funciona, probar con:

```
python -m pip install reportlab
```

### Instalación en Mac o Linux

```
pip3 install reportlab
```

### Ejecución

Ubicarse dentro de la carpeta `src/` y ejecutar:

```
cd src

.\venv\Scripts\Activate.ps1

python main.py
```

Al iniciar, el programa cargará automáticamente los datos guardados en los archivos CSV. Si es la primera vez que se ejecuta, las listas estarán vacías y se puede empezar a registrar desde cero.

---


## Manual de Usuario

El manual de usuario completo está disponible en la carpeta `doc/` del repositorio:

- [`doc/manual_data_file_solution.md`](doc/manual_data_file_solution.md)
- [`doc/manual_data_file_solution.docx`](doc/manual_data_file_solution.docx)

---

*Proyecto académico — Algoritmia y Programación — Universidad de Antioquia — 2026*
*Docente: John Heider Dávila*