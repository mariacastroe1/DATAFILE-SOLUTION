import os

def limpiar_pantalla():
    """Limpia la consola para mejorar para que el usuario entienda mejor la app."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():

    while True:
        limpiar_pantalla()
        print("===========================================")
        print("            SISTEMA DATA FILE SOLUTION     ")
        print("        Gestión Eficiente de Activos       ")
        print("===========================================")
        print("  1. Registrar Usuario")
        print("  2. Registrar Ítem (Objeto a prestar)")
        print("  3. Registrar Préstamo")
        print("  4. Registrar y Certificar Devolución")
        print("  5. Consultar Estado General de Préstamos")
        print("  6. Panel de Administración")
        print("  0. Guardar y Salir")
        print("===========================================")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            print("\nSelecciono la función de registrar uusuario")
            
        elif opcion == "2":
            limpiar_pantalla()
            print("\nSelecciono la función de registrar item")
            
        elif opcion == "3":
            limpiar_pantalla()
            print("\nSelecciono la función de registrar prestamo")
            
        elif opcion == "4":
            limpiar_pantalla()
            # Esta función en prestamos.py ahora debe contener la lógica para tu PDF
            print("\nSelecciono la función de registrar la devolución")
            
        elif opcion == "5":
            limpiar_pantalla()
            print("\nSelecciono la función de consultar el estadod general de los prestamos")
            
        elif opcion == "6":
            limpiar_pantalla()
            print("\nSelecciono la función para abrir el panel admin")
                
        elif opcion == "0":
            print("\nAqui deberia de guardar...")
            break
            
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")
        
        # Pausa para que el usuario pueda leer los mensajes antes de limpiar la pantalla
        if opcion != "0":
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()