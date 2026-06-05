# main.py
# Archivo principal del sistema Data File Solution
# Desde aqui se inicia todo el programa

# El programa se organiza en modulos gracias a la función import y se comunica con los demas archivos
import os
import csv
import usuarios
import prestamos
import admin


def limpiar_pantalla():
    # Limpia la consola para que el menu se vea ordenado
    os.system('cls' if os.name == 'nt' else 'clear')


def crear_carpetas():
    # Crea las carpetas que el programa necesita para guardar archivos
    # Si ya existen no pasa nada, las ignora
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("certificados"):
        os.makedirs("certificados")
    if not os.path.exists("facturas"):
        os.makedirs("facturas")
    if not os.path.exists("reportes"):
        os.makedirs("reportes")


def cargar_usuarios():
    # Lee el archivodata/usuarios.csv y devuelve la lista de usuarios
    # Si el archivo no existe devuelve una lista vacia
    lista = []
    ruta  = os.path.join("data", "usuarios.csv")

    if not os.path.exists(ruta):
        return lista

    #Encoding utf-8(universal)nos sirve para que el programa pueda leer caracteres especiales como tildes y ñ sin problemas
    with open(ruta, "r", encoding="utf-8") as archivo:  #r significa que se abre el archivo en modo lectura.
        lector = csv.reader(archivo)
        next(lector)  # Saltar encabezados(titulos), para que no se conviertan en un usuario mas de la lista

        for columna in lector: #recorre todos los usuarios guardados en el CSV 
    
           # Se crea una lista nueva con campos entendibles Como nombre, apellido... para poder analizar y leer mejor los datos, es decir se le da nombre a las columnas.
            usuario = {
                "doc":                  columna[1],
                "nombre":               columna[2],
                "apellido":             columna[3],
                "correo":               columna[4],
                "tiempo":               int(columna[5]),
                "prestamos_realizados": 0
            }
            lista.append(usuario) # agrega cada registro a la lista de usuarios del programa para que puedan ser usados

    print("  Usuarios cargados: " + str(len(lista))) # Str convierte el numero a texto para poder imprimirlo junto con el mensaje y len cuenta cuantos usuarios se cargaron en el for. ejemplo: usuarios cargados: 20.
    return lista # devuelve la lista de usuarios para que el programa pueda usarla en otras partes.


def cargar_items():
    # Lee el archivo data/items.csv y devuelve la lista de items
    # Si el archivo no existe devuelve una lista vacia
    lista = []
    ruta  = os.path.join("data", "items.csv")

    if not os.path.exists(ruta):
        return lista

    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Saltar encabezados

        for columna in lector:
            # Columnas: fecha_registro, id, nombre, categoria, precio, estado
            item = {
                "id":         columna[1],
                "nombre":     columna[2],
                "categoria":  columna[3],
                "precio":     float(columna[4]),
                "estado":     columna[5],
                "disponible": True  # Se corrige abajo al revisar prestamos activos
            }
            lista.append(item)

    print("  Items cargados: " + str(len(lista)))
    return lista


def cargar_prestamos():
    # Lee archivo data/prestamos.csv y devuelve la lista de prestamos
    # Todos se cargan como activos al principio, luego se corrigen
    # Si el archivo no existe devuelve una lista vacia
    lista = []
    ruta  = os.path.join("data", "prestamos.csv")

    if not os.path.exists(ruta):
        return lista

    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Saltar encabezados

        for columna in lector:
            # Columnas: fecha_registro, usuario, documento, item_id, item_nombre, precio, dias_pactados, fecha_inicio
            prestamo = {
                "usuario_doc":    columna[2],
                "usuario_nombre": columna[1],
                "item_id":        columna[3],
                "item_nombre":    columna[4],
                "item_precio":    float(columna[5]),
                "dias_pactados":  int(columna[6]),
                "fecha_inicio":   columna[7],
                "activo":         True  # Se corrige abajo al revisar devoluciones y ventas
            }
            lista.append(prestamo)

    print("  Prestamos cargados: " + str(len(lista)))
    return lista


def cargar_ventas(list_prestamos, list_usuarios, list_items):
    # Lee devoluciones.csv y ventas.csv para saber cuales prestamos ya cerraron
    # Tambien corrige el campo disponible de los items y prestamos_realizados de usuarios
    # Devuelve la lista de ventas para que el panel admin pueda mostrar las metricas

    # Marcar prestamos que ya fueron devueltos
    ruta_dev = os.path.join("data", "devoluciones.csv")
    if os.path.exists(ruta_dev):
        with open(ruta_dev, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            next(lector)
            for columna in lector:
                # Columnas: fecha_devolucion, usuario, documento, item_id, item_nombre, dias_usados
                doc_buscado  = columna[2]
                item_buscado = columna[3]
                for p in list_prestamos:
                    if p["usuario_doc"] == doc_buscado and p["item_id"] == item_buscado and p["activo"] == True:
                        p["activo"] = False
                        break

    # Marcar prestamos que se convirtieron en venta y reconstruir lista de ventas
    list_ventas  = []
    ruta_ventas  = os.path.join("data", "ventas.csv")
    if os.path.exists(ruta_ventas):
        with open(ruta_ventas, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            next(lector)
            for columna in lector:
                # Columnas: fecha, usuario, documento, item_id, item_nombre, subtotal, impuesto, total
                doc_buscado  = columna[2]
                item_buscado = columna[3]
                for p in list_prestamos:
                    if p["usuario_doc"] == doc_buscado and p["item_id"] == item_buscado and p["activo"] == True:
                        p["activo"] = False
                        break

                venta = {
                    "usuario":    columna[1],
                    "doc":        columna[2],
                    "item_id":    columna[3],
                    "item_nombre": columna[4],
                    "subtotal":   float(columna[5]),
                    "impuesto":   float(columna[6]),
                    "total":      float(columna[7]),
                    "motivo":     "Excedio el tiempo maximo de prestamo (30 dias)"
                }
                list_ventas.append(venta)

    # Con los prestamos ya corregidos, marcar los items que siguen prestados como no disponibles
    for p in list_prestamos:
        if p["activo"] == True:
            for item in list_items:
                if item["id"] == p["item_id"]:
                    item["disponible"] = False
                    break

    # Recalcular cuantos prestamos ha hecho cada usuario
    for p in list_prestamos:
        for u in list_usuarios:
            if u["doc"] == p["usuario_doc"]:
                u["prestamos_realizados"] = u["prestamos_realizados"] + 1
                break

    print("  Ventas cargadas: " + str(len(list_ventas)))
    return list_ventas


def menu_principal():

    crear_carpetas()

    # Cargar todos los datos guardados en los CSV al arrancar
    print("\n  Cargando datos guardados...")
    list_usuarios  = cargar_usuarios() #recibe la lista nombrada de forma entendible de los usuario guardados en el csv.
    list_items     = cargar_items()
    list_prestamos = cargar_prestamos()
    list_ventas    = cargar_ventas(list_prestamos, list_usuarios, list_items)
    print("  Listo.\n")

    # Ciclo principal del menu
    while True:
        limpiar_pantalla()
        print("===========================================")
        print("        SISTEMA DATA FILE SOLUTION        ")
        print("      Gestion Eficiente de Activos        ")
        print("===========================================")
        print("  1. Registrar Usuario")
        print("  2. Registrar Prestamo")
        print("  3. Registrar Devolucion")
        print("  4. Consultar items con mas de 30 dias")
        print("  5. Consultar articulos prestados")
        print("  6. Administrador")
        print("  0. Salir")
        print("===========================================")

        opcion = input("  Seleccione una opcion: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            usuarios.registrar_usuario(list_usuarios)

        elif opcion == "2":
            limpiar_pantalla()
            prestamos.registrar_prestamo(list_usuarios, list_items, list_prestamos)

        elif opcion == "3":
            limpiar_pantalla()
            prestamos.registrar_devolucion(list_prestamos, list_items)

        elif opcion == "4":
            limpiar_pantalla()
            prestamos.consultar_y_procesar_morosos(list_prestamos, list_items, list_ventas)

        elif opcion == "5":
            limpiar_pantalla()
            prestamos.consultar_estado_general(list_prestamos)

        elif opcion == "6":
            limpiar_pantalla()
            if admin.login_admin():
                admin.menu_admin(list_usuarios, list_items, list_prestamos, list_ventas)

        elif opcion == "0":
            print("\n  Hasta pronto!")
            break

        else:
            print("\n  ERROR: Opcion no valida. Ingrese un numero del 0 al 6.")

        if opcion != "0":
            input("\n  Presione Enter para continuar...")


menu_principal()