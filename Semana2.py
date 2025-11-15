def calcular_descuento_software():
    """
    Función para calcular descuentos en compras de software según la cantidad de licencias.
    - 3 o más licencias: 20% de descuento
    - 5 o más licencias: 30% de descuento
    - Precio base por licencia: $50
    """
    precio_base = 50  # Precio base por licencia en dólares
    
    while True:
        try:
            cantidad_licencias = int(input("Ingrese la cantidad de licencias a adquirir: "))
            if cantidad_licencias <= 0:
                print("La cantidad de licencias debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    precio_total_sin_descuento = cantidad_licencias * precio_base
    
    # Determinar el porcentaje de descuento
    if cantidad_licencias >= 5:
        descuento_porcentaje = 30
    elif cantidad_licencias >= 3:
        descuento_porcentaje = 20
    else:
        descuento_porcentaje = 0
    
    # Calcular el descuento y precio final
    descuento_valor = precio_total_sin_descuento * (descuento_porcentaje / 100)
    precio_final = precio_total_sin_descuento - descuento_valor
    
    # Mostrar resultados
    print(f"\n--- RESUMEN DE COMPRA ---")
    print(f"Cantidad de licencias: {cantidad_licencias}")
    print(f"Precio por licencia: ${precio_base}")
    print(f"Precio total sin descuento: ${precio_total_sin_descuento}")
    
    if descuento_porcentaje > 0:
        print(f"Descuento aplicado: {descuento_porcentaje}%")
        print(f"Valor del descuento: ${descuento_valor:.2f}")
        print(f"PRECIO FINAL CON DESCUENTO: ${precio_final:.2f}")
    else:
        print("No se aplica descuento (se requieren mínimo 3 licencias)")
        print(f"PRECIO FINAL: ${precio_final:.2f}")
    print("-------------------------\n")


def calcular_volumen_esfera():
    """
    Función para calcular el volumen de una esfera.
    Fórmula: Volumen = (4/3) * π * r³
    """
    pi = 3.1416  # Valor aproximado de π
    
    while True:
        try:
            radio = float(input("Ingrese el radio de la esfera: "))
            if radio <= 0:
                print("El radio debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Calcular el volumen usando la fórmula: V = (4/3) * π * r³
    volumen = (4/3) * pi * (radio ** 3)
    
    print(f"\n--- CÁLCULO DEL VOLUMEN ---")
    print(f"Radio de la esfera: {radio}")
    print(f"Volumen de la esfera: {volumen:.4f} unidades cúbicas")
    print("---------------------------\n")


def mostrar_menu():
    """
    Función para mostrar el menú de opciones del programa.
    """
    print("\n" + "="*50)
    print("    SISTEMA DE GESTIÓN MYPRO")
    print("="*50)
    print("1. Calcular descuento en compras de software")
    print("2. Calcular el volumen de una esfera")
    print("3. Salir del programa")
    print("-"*50)


def validar_opcion():
    """
    Función para validar que la opción ingresada sea válida (1, 2 o 3).
    Retorna la opción validada.
    """
    while True:
        opcion = input("Seleccione una opción (1-3): ").strip()
        if opcion in ['1', '2', '3']:
            return opcion
        else:
            print("ERROR: Opción no válida. Por favor, seleccione 1, 2 o 3.")


def main():
    """
    Función principal que controla el flujo del programa.
    """
    print("¡Bienvenido al Sistema de Gestión MyPro!")
    
    while True:
        mostrar_menu()
        opcion = validar_opcion()
        
        if opcion == '1':
            print("\n--- CÁLCULO DE DESCUENTOS ---")
            calcular_descuento_software()
            
        elif opcion == '2':
            print("\n--- CÁLCULO DE VOLUMEN ---")
            calcular_volumen_esfera()
            
        elif opcion == '3':
            print("\n¡Gracias por usar el Sistema de Gestión MyPro!")
            print("¡Hasta luego!")
            break
        
        # Pausa para que el usuario pueda leer los resultados
        input("Presione Enter para continuar...")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()