# MANUAL DE USUARIO

## Sistema Data File Solution
### Gestion Eficiente de Activos

**Algoritmia y Programacion**
Universidad de Antioquia — 2026

---

## 1. Introduccion

Data File Solution es un programa desarrollado en Python que permite gestionar prestamos de articulos entre personas de manera organizada.

El sistema permite registrar usuarios, registrar articulos, administrar prestamos y devoluciones, controlar articulos vencidos, generar facturas por incumplimiento y consultar reportes desde el panel de administracion.

Toda la informacion se guarda automaticamente en archivos CSV y documentos de texto que el programa crea en la carpeta del proyecto.

---

## 2. Requisitos del Sistema

Para ejecutar el programa se necesita:

- Python 3.10 o superior
- La libreria reportlab instalada (para generar PDF)
- Sistema operativo Windows, Linux o macOS
- Permiso de lectura y escritura en la carpeta del proyecto

Para instalar reportlab abra una terminal y ejecute:

```
pip install reportlab
```

---

## 3. Como Ejecutar el Programa

Abra una terminal, ubiquese en la carpeta donde estan los archivos del proyecto y ejecute:

```
python main.py
```

Al iniciar, el programa cargara automaticamente los datos guardados en los archivos CSV. Si es la primera vez que se ejecuta, las listas estaran vacias y podra empezar a registrar datos desde cero.

---

## 4. Menu Principal

Una vez iniciado el programa aparece el menu principal con las siguientes opciones:

| Opcion | Descripcion |
|--------|-------------|
| 1. Registrar Usuario | Agrega un nuevo usuario al sistema |
| 2. Registrar Prestamo | Registra un prestamo a un usuario existente |
| 3. Registrar Devolucion | Registra la devolucion de un articulo prestado |
| 4. Items con mas de 30 dias | Muestra articulos vencidos y genera ventas |
| 5. Consultar articulos prestados | Lista todos los prestamos activos ordenados por dias |
| 6. Administrador | Acceso al panel administrativo con contrasena |
| 0. Salir | Cierra el programa |

---

## 5. Registro de Usuarios

Esta opcion permite agregar nuevos usuarios al sistema. El programa solicitara los siguientes datos:

- Nombre
- Apellido
- Numero de documento
- Correo electronico
- Dias de prestamo permitidos

### Validaciones

**Nombre y apellido:** deben tener minimo 3 letras y no pueden contener numeros.

**Documento:** solo se permiten numeros, debe tener entre 3 y 15 digitos y no puede estar repetido en el sistema.

**Correo electronico:** debe contener el simbolo @ y terminar en .com. Por ejemplo: nombre@gmail.com

**Dias de prestamo:** solo se aceptan los valores 5, 10, 15 o 30 dias. Cualquier otro valor sera rechazado.

Si algun dato es incorrecto el programa mostrara un mensaje de error y volvera a pedir ese mismo campo sin perder los datos anteriores.

Al completar el registro el usuario queda guardado en: `data/usuarios.csv`

---

## 6. Registro de Items

Esta opcion permite registrar articulos que podran ser prestados. Solo el administrador puede registrar items desde el panel de administracion.

### Datos solicitados

- Nombre del articulo (minimo 3 caracteres)
- Categoria
- Precio de compra
- Estado del articulo (valoracion de funcionamiento y apariencia)

### Categorias disponibles

1. Videojuegos
2. Libros
3. Musica y video
4. Herramientas
5. Dinero
6. Miscelaneo

### Estado del articulo (logica difusa)

El sistema calcula el estado del articulo combinando dos valores del 1 al 10: calidad de funcionamiento (peso del 70%) y estado estetico o fisico (peso del 30%).

| Puntaje calculado | Estado asignado |
|-------------------|-----------------|
| 9 o mas | Excelente (Como nuevo) |
| 7 a 8.9 | Bueno (Desgaste minimo) |
| 5 a 6.9 | Regular (Funcional con detalles) |
| Menos de 5 | Malo (Requiere mantenimiento) |

### ID automatico

Cada articulo recibe un identificador unico generado automaticamente. El ID usa el prefijo de la categoria seguido de 4 caracteres aleatorios.

Ejemplos: `VID-A3K9`, `LIB-X7B2`, `HER-QP12`, `MUS-J8N1`

Al completar el registro el articulo queda guardado en: `data/items.csv`

---

## 7. Registro de Prestamos

Esta opcion permite prestar un articulo disponible a un usuario registrado.

### Pasos

1. El programa pide el documento del usuario.
2. Si el usuario existe muestra el inventario de articulos disponibles.
3. Se ingresa el ID del articulo a prestar.
4. Se elige si usar la fecha de hoy o ingresar una fecha manualmente.
5. El prestamo queda registrado y el articulo pasa a no disponible.

### Fecha manual

El programa permite ingresar una fecha de inicio diferente a la de hoy. Esto es util para simular prestamos antiguos y probar la opcion de ventas por mora sin tener que esperar 30 dias reales. La fecha debe tener el formato `YYYY-MM-DD`, por ejemplo: `2026-01-15`

Si el usuario no existe el programa lo informa y pregunta si desea intentar con otro documento.

El prestamo queda guardado en: `data/prestamos.csv`

---

## 8. Registro de Devoluciones

Esta opcion permite registrar la devolucion de un articulo que fue prestado.

### Pasos

1. El programa pide el documento del usuario.
2. Muestra la lista de prestamos activos de ese usuario con los dias transcurridos.
3. Se selecciona el numero del prestamo a devolver.
4. El programa verifica que no supere los 30 dias.
5. Si todo esta bien cierra el prestamo y devuelve el articulo al inventario.

### Documentos generados

Al registrar una devolucion exitosa el programa genera automaticamente dos archivos:

- Un certificado de devolucion en formato TXT en la carpeta `certificados/`
- Un certificado de devolucion en formato PDF en la carpeta `certificados/`

El nombre del archivo tiene el siguiente formato:

```
NombreUsuario_FechaDevolucion_IDItem.txt
```

Si el prestamo supera los 30 dias el programa avisa que ese caso debe procesarse desde la opcion 4 del menu.

La devolucion queda guardada en: `data/devoluciones.csv`

---

## 9. Items con mas de 30 Dias (Ventas por Mora)

Esta opcion revisa todos los prestamos activos y detecta los que llevan mas de 30 dias sin devolucion.

### Que hace el programa

- Calcula los dias transcurridos desde la fecha de inicio de cada prestamo.
- Muestra en pantalla los prestamos que superaron los 30 dias.
- Calcula el subtotal, el impuesto del 23% (impuesto por conchudez) y el total a cobrar.
- Cierra el prestamo automaticamente.
- Genera una factura de venta en formato TXT y PDF en la carpeta `facturas/`
- Guarda el registro de la venta en `data/ventas.csv`

Si no hay prestamos vencidos el programa lo informa y no realiza ninguna accion.

---

## 10. Consultar Articulos Prestados

Esta opcion muestra todos los prestamos que estan actualmente activos, ordenados de mayor a menor cantidad de dias transcurridos.

La informacion se muestra en pantalla con las columnas ID, nombre del articulo, dias transcurridos y nombre del usuario.

Ademas el programa guarda automaticamente un archivo de reporte en:

```
reportes/estado_prestamos.txt
```

---

## 11. Panel de Administrador

Esta opcion esta protegida con usuario y contrasena. Solo quien tenga las credenciales correctas puede ingresar.

| Campo | Valor |
|-------|-------|
| Usuario | admin |
| Contrasena | 1234 |

### Opciones del panel

1. **Ver metricas generales:** muestra el total de prestamos, devoluciones, ventas y dinero recaudado.
2. **Ver lista de usuarios:** muestra todos los usuarios registrados con su cantidad de prestamos.
3. **Ver usuario con mas y menos prestamos:** identifica los extremos del historial.
4. **Registrar nuevo item:** permite agregar articulos al inventario desde el panel administrativo.

---

## 12. Archivos que Genera el Sistema

El programa crea y organiza automaticamente los siguientes archivos y carpetas:

| Archivo o carpeta | Descripcion |
|-------------------|-------------|
| `data/usuarios.csv` | Usuarios registrados en el sistema |
| `data/items.csv` | Articulos registrados en el inventario |
| `data/prestamos.csv` | Historial de todos los prestamos realizados |
| `data/devoluciones.csv` | Historial de todas las devoluciones |
| `data/ventas.csv` | Historial de ventas generadas por mora |
| `certificados/` | Certificados de devolucion en TXT y PDF |
| `facturas/` | Facturas de venta en TXT y PDF |
| `reportes/` | Reporte de estado de prestamos en TXT |

Todos estos archivos se generan automaticamente. No es necesario crearlos a mano. Si se elimina un archivo CSV el programa simplemente empieza con esa lista vacia la proxima vez que se ejecute.

---

## 13. Recomendaciones de Uso

- Registrar primero los usuarios antes de intentar hacer prestamos.
- Registrar los articulos desde el panel de administrador antes de hacer prestamos.
- Revisar periodicamente la opcion 4 del menu para detectar prestamos vencidos.
- No modificar manualmente los archivos CSV para evitar errores al cargar los datos.
- Hacer copias de la carpeta `data/` si se quiere guardar un respaldo de los registros.
- Para simular un prestamo vencido usar la opcion de fecha manual al registrar el prestamo.

---

## 14. Informacion del Proyecto

Data File Solution

Proyecto academico desarrollado para la asignatura Algoritmia y Programacion.

Universidad de Antioquia — 2026.
